import json
from modules import gmail_client, utils
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
	email = email.replace('<','').replace('>','')
	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'r') as f:
		data = json.loads(f.read())
	record_indices = [i for i, record in enumerate(data) if record['email_address'] == '<' + email + '>']
	if len(record_indices) > 0:
		return [data[record_index] for record_index in record_indices]
	else:
		return False


def run_it(email, num=10, existing=True):
	adds = get_some(num)
	assert len(adds) == num
	assert type(adds[0]) == str
	#assert num < 150

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
	email = email.replace('<','').replace('>','')
	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'r') as f:
		data = json.loads(f.read())
	record_index = [i for i, record in enumerate(data) if record['email_address'] == '<' + email + '>']
	record_index = record_index[0]
	data[record_index]['sent_voter_addresses'].append(addresses)
	
	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'w') as f:
		f.write(json.dumps(data))

def add_new_record(email, addresses):
	email = email.replace('<','').replace('>','')
	record = {'sent_voter_addresses':addresses, 'active': 'y', 'email_address':'<'+email+'>'}

	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'r') as f:
		data = json.loads(f.read())
		data.append(record)
	with open(config.SEEN_EMAIL_DATA_FILE_PATH, 'w') as f:
		f.write(json.dumps(data))