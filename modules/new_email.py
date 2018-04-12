import re
import copy

from secrets import secret
from modules import utils


class EmailValueNotPresent(Exception):
    pass


def extract_part_of_snippet(email_id, sender, raw):
    """
    We are going to use snippet as a proxy for message text.  However, in replies, the
    snippet can (always does?) contain some of the previous messages' text.  If that previous
    message has a key phrase we are looking for in this one, that'tests a problem. But, these
    previous messages will be proceeded by a date header (e.g. 'On Tue, Jan 19 at 12:30).
    May God grant us the grace of making that heading always be there.
    :return: the part of the raw message snippet before the first date/time heading
    """
    snippet = raw.get('snippet')
    if not snippet:
        raise EmailValueNotPresent('No snippet on email {0} from sender {1}'.format(email_id, sender))

    # example 'On Apr 5, 2018, at 10:51 AM'
    pattern_with_no_weekday = re.compile("On [a-zA-Z]{3}\s\d{1,2},\s\d{4},\sat")
    found_pattern1_heading = pattern_with_no_weekday.search(snippet)
    pattern_with_weekday = re.compile("On [a-zA-Z]{3},\s[a-zA-Z]{3}\s\d{1,2}")
    found_pattern2_heading = pattern_with_weekday.search(snippet)

    if found_pattern1_heading != None or found_pattern2_heading != None:
        if found_pattern1_heading != None and found_pattern2_heading != None:
            return snippet[:min(found_pattern1_heading.start(), found_pattern2_heading.start())]
        if found_pattern1_heading != None:
            return snippet[:found_pattern1_heading.start()]
        if found_pattern2_heading != None:
            return snippet[:found_pattern2_heading.start()]
    else:
        return snippet


def extract_sender(raw):
    headers = raw['payload']['headers']
    return_path = [header for header in headers if header['name'].lower() == 'return-path']
    if return_path:
        sender = return_path[0]['value']
    else:
        sender = [header for header in headers if header['name'].lower() == 'from'][0]['value']

    sender = find_email_substring(sender)
    if sender:
        return utils.reformat_email_address(sender)
    else:
        return None


def find_email_substring(email_string):
    substrings = email_string.split(' ')
    email_substring = [ss for ss in substrings if '@' in ss]
    if len(email_substring) == 1:
        return email_substring[0]
    return False


def find_key_phrase(text, key_phrase):
    lower_text = text.lower()
    lower_kp = key_phrase.lower()
    found = False
    if lower_kp in lower_text:
        print("Found 1st:{0} in text: {1}".format(lower_kp, lower_text))
        found = True
    if lower_kp.replace(' ', '-') in lower_text:
        print("Found 2nd:{0} in text: {1}".format(lower_kp.replace(' ', '-'), lower_text))
        found = True
    if lower_kp.replace(' ', '') in lower_text:
        print("Found 3rd:{0} in text: {1}".format(lower_kp.replace(' ', ''), lower_text))
        found = True
    return found


def check_if_this_is_just_a_demo(text):
    for thing in ['testing-bot', 'testing bot', 'test-bot', 'test bot']:
        if thing in text[:15].lower():
            return True
    return False


class NewEmail:

    def __str__(self):
        d = copy.deepcopy(self.__dict__)
        d['raw'] = 'Not gonna print raw...'
        s = '\n\n' + '\n'.join(['{0}: {1}'.format(key, val) for key, val in list(d.items())])
        return s


    def main(self, email_id, raw_email_datum, seen_email_data):
        self.email_id = email_id
        self.raw = raw_email_datum
        self.sender = extract_sender(raw_email_datum)
        if not self.sender:
            raise EmailValueNotPresent("No sender on message {0}".format(email_id))

        self.should_ignore = self.should_we_ignore()

        if not self.should_ignore: # just skip these if we're ignoring it anyway

            self.threadId = self.raw.get('threadId')
            if not self.threadId:
                raise EmailValueNotPresent("No threadId on message {0} from {1}".format(email_id, self.sender))

            self.RFC_message_id = self.get_raw_header_val('message-id')
            if not self.RFC_message_id:
                raise EmailValueNotPresent("No RFC on message {0} from {1}".format(email_id, self.sender))

            # NEED TO REVISIT THIS -- WHAT HAPPENS WHEN YOU TRY TO REPLY WITH THIS SUBJECT?
            self.subject = self.get_raw_header_val('subject')
            if not self.subject:
                self.subject = ""

            self.attach = self.extract_attach()
            self.text = extract_part_of_snippet(self.email_id, self.sender, self.raw)
            self.surrender = find_key_phrase(self.text, secret.SURRENDER_KEY_PHRASE)
            self.asks_for_more = find_key_phrase(self.text, secret.ASK_FOR_MORE_KEY_PHRASE)
            self.from_seen = self.determine_if_seen(seen_email_data)
            self.from_active = self.is_from_active(seen_email_data)
            self.use_demo_data = check_if_this_is_just_a_demo(self.text)


    def get_raw_header_val(self, val):
        try:
            return [header['value'] for header in self.raw['payload']['headers'] if header['name'].lower() == val.lower()][0]
        except IndexError:
            return None


    def should_we_ignore(self):
        return (self.sender == secret.THE_EMAIL) or ('google' in self.sender)


    def extract_attach(self):
        parts = self.raw['payload'].get('parts')
        if not parts:
            return False
        return len([part for part in parts if part['mimeType'] == 'image/jpeg']) > 0


    def determine_if_seen(self, seen_email_data):
        return self.sender in seen_email_data.keys()


    def is_from_active(self, seen_email_data):
        if seen_email_data.get(self.sender):
            return seen_email_data[self.sender]['active']
        else:
            return False