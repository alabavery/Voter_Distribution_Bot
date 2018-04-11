import json
from modules import gmail_client, utils, data_handling
import config
from secrets import secret


def convert_seen_data_old_to_new_format(old, new=None):
	"""
	Old format was [...{'email_address': str, 'active': str, 'sent_voter_addresses': [...str...]}...]
	New format is {...actual email of volunteer: {'sender': a.e.o.v., 'voters': [...str...], 'active': str}...}
	:param old: some old seen data
	:param new: optionally you can add to an already existing new dataset
	:return: dict()
	"""
	if not new:
		new = dict()

	for volunteer_entry in old:
		reformatted_email = utils.reformat_email_address(volunteer_entry['email_address'])
		new_entry = dict(
			sender=reformatted_email,
			voters=volunteer_entry['sent_voter_addresses'],
			active=volunteer_entry['active']
		)
		if new.get(reformatted_email):
			new[reformatted_email].update(new_entry)
		else:
			new[reformatted_email] = new_entry
	return new


def get_raw_message_by_id(message_id):
	client = gmail_client.get_gmail_client(config.CLIENT_SECRET_FILE_PATH, config.SCOPES, secret.APPLICATION_NAME)
	return client.users().messages().get(userId='me', id=message_id).execute()


def check_if_seen(email):
	email = utils.reformat_email_address(email)
	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'r') as f:
		data = json.loads(f.read())
	return data.get(email)


def run_it(email, num=10, existing=True):
	adds = get_some(num)
	assert len(adds) == num
	assert type(adds[0]) == str

	if existing:
		add_to_existing_record(email, adds)

	else:
		add_new_record(email, adds)

	adds = ".................".join(adds)
	del_some(num)
	return adds


def get_some(num=10):
	with open(config.UNUSED_VOTERS_FILE_PATH, 'r') as f:
		all_addresses = json.loads(f.read())
		return all_addresses[:num]


def del_some(num=10):
	sure = input("Sure?")
	if sure.lower() == 'y':
		with open(config.UNUSED_VOTERS_FILE_PATH, 'r') as f:
			all_addresses = json.loads(f.read())
		del all_addresses[:num]

		with open(config.UNUSED_VOTERS_FILE_PATH, 'w') as f:
			f.write(json.dumps(all_addresses))
	else:
		print("Didn't do anything.")


def add_to_existing_record(email, addresses):
	email = utils.reformat_email_address(email)
	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'r') as f:
		seen_email_data = json.loads(f.read())

	seen_email_data = data_handling.update_for_sent_voters(email, addresses, seen_email_data)
	seen_email_data = data_handling.mark_existing_entry_active(email, seen_email_data)

	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'w') as f:
		f.write(json.dumps(seen_email_data))


def add_new_record(email, addresses):
	email = utils.reformat_email_address(email)
	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'r') as f:
		seen_email_data = json.loads(f.read())

	seen_email_data = data_handling.add_entry(email, addresses, seen_email_data)
	seen_email_data = data_handling.mark_existing_entry_active(email, seen_email_data)

	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'w') as f:
		f.write(json.dumps(seen_email_data))



def unnest_list(potentially_nested_list):
	new_list = []
	for item in potentially_nested_list:
		if type(item) == list:
			unnested = unnest_list(item)
			new_list.extend(unnested)
		else:
			assert type(item) == str
			new_list.append(item)
	return new_list
