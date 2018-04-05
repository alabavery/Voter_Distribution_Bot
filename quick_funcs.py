import json
import gmail_client, gmail_handling
import config, secret


def get_raw_message_by_id(message_id):
	client = gmail_client.get_gmail_client(config.CLIENT_SECRET_FILE_PATH, config.SCOPES, secret.APPLICATION_NAME)
	return client.users().messages().get(userId='me', id=message_id).execute()


def check_if_seen(email):
	email = email.replace('<','').replace('>','')
	with open('seen_email_data.json', 'r') as f:
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
	with open('unused_addresses.json', 'r') as f:
		all_addresses = json.loads(f.read())
		return all_addresses[:num]


def del_some(num=10):
	sure = input("Sure?")
	if sure.lower() == 'y':
		with open('unused_addresses.json', 'r') as f:
			all_addresses = json.loads(f.read())
		del all_addresses[:num]

		with open('unused_addresses.json', 'w') as f:
			f.write(json.dumps(all_addresses))
	else:
		print("Didn't do anything.")

def add_to_existing_record(email, addresses):
	email = email.replace('<','').replace('>','')
	with open('seen_email_data.json', 'r') as f:
		data = json.loads(f.read())
	record_index = [i for i, record in enumerate(data) if record['email_address'] == '<' + email + '>']
	record_index = record_index[0]
	data[record_index]['sent_voter_addresses'].append(addresses)
	
	with open('seen_email_data.json', 'w') as f:
		f.write(json.dumps(data))

def add_new_record(email, addresses):
	email = email.replace('<','').replace('>','')
	record = {'sent_voter_addresses':addresses, 'active': 'y', 'email_address':'<'+email+'>'}

	with open('seen_email_data.json', 'r') as f:
		data = json.loads(f.read())
		data.append(record)
	with open('seen_email_data.json', 'w') as f:
		f.write(json.dumps(data))