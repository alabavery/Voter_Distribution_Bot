from email.mime.text import MIMEText
import base64

def get_unread_email_ids(gmail_client):
    """
    return list of id of unread emails
    """
    # response is [{'id':str, 'threadId':str},...]
    response = gmail_client.users().messages().list(userId='me', q='is:unread').execute()

    if 'messages' in response: # messages key only exists if there are unread messages
        ids = [message['id'] for message in response['messages']]
        ids.reverse() # ids comes most to least recent; we want vice versa
        return ids
    else:
        print("No unread messages...")
        return [] # still return a list since that'tests what caller expects


def get_emails(client, email_ids):
    return [(this_id, client.users().messages().get(userId='me', id=this_id).execute()) for this_id in email_ids]


def mark_as_read(client, email_ids):
    print("Marking the following ids as read: {0}".format(email_ids))
    msg_labels = {'removeLabelIds': ['UNREAD'], 'addLabelIds': []}

    for message_id in email_ids:
        message = client.users().messages().modify(userId='me', id=message_id, body=msg_labels).execute()
        assert 'UNREAD' not in message['labelIds']


def create_message(sender, to, subject, message_text, in_reply_to, references, threadId):
    """Create a message for an email.
    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    to_be_sent = {'raw':base64.urlsafe_b64encode(message.as_bytes()).decode()}
    if references:
        to_be_sent['References'] = references
    if in_reply_to:
        to_be_sent['In-Reply-To'] = in_reply_to
    if threadId:
        to_be_sent['threadId'] = threadId
    return to_be_sent


def send_message(message, client):
    """Send an email message.
    Args:
    client: Authorized Gmail API service instance.
    user_id: User'tests email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.
    Returns:
    Sent Message.
    """
    # try:
    #     message = (client.users().messages().send(userId='me', body=message).execute())
    #     print('Message Id: %tests' % message['id'])
    #     return message
    # except errors.HttpError as error:
    #     print('An error occurred: %tests' % error)
    pass


def send_email(gmail_client, host_email, recipient_email, email_subject, email_body,
               in_reply_to=None, references=None, threadId=None):
    message = create_message(host_email, recipient_email, email_subject, email_body, in_reply_to, references, threadId)
    send_message(message, gmail_client)