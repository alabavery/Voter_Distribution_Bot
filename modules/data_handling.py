from modules import utils

class MyDataHandlingError(Exception):
	pass


def update_for_sent_voters(sender, voters_to_add, seen_email_data):
	sender = utils.reformat_email_address(sender) # note that it was probably already reformatted by NewEmail
	entry = seen_email_data.get(sender)

	if entry:
		seen_email_data[sender] = add_voters_to_entry(voters_to_add, seen_email_data[sender])
	else:
		seen_email_data = add_entry(sender, voters_to_add, seen_email_data)
	return seen_email_data


def mark_existing_entry_active(sender, seen_email_data):
	seen_email_data[sender]['active'] = 'y'
	return seen_email_data


def mark_existing_entry_inactive(sender, seen_email_data):
	seen_email_data[sender]['active'] = 'n'
	return seen_email_data


def add_voters_to_entry(voters_to_add, entry):
	print("Adding to entry: {0}".format(voters_to_add))

	for voter in voters_to_add:
		if voter in entry['voters']:
			msg = "Already added voter '{0}' to entry for {1}".format(voter, entry['sender'])
			raise MyDataHandlingError(msg)
		entry['voters'].append(voter)
	return entry


def add_entry(new_sender, voters_to_add, seen_email_data):
	new_entry = {'sender':new_sender, 'voters':voters_to_add}
	seen_email_data[new_sender] = new_entry
	return seen_email_data


def get_voters(unused_voters, num, demo=False):
	if demo:
		return ['fake voter name{0}; fake voter address{0}'.format(i) for i in range(num)]

	if num > len(unused_voters):
		raise MyDataHandlingError("\n\n\nHoly crap, we don't have enough voters left to send!\n\n\n")
	return unused_voters[:num]


def delete_voters(unused_voters, voters_to_delete):
	before = len(unused_voters)
	updated_unused_voters = [voter for voter in unused_voters if voter not in voters_to_delete]
	assert before - len(voters_to_delete) == len(updated_unused_voters)
	return updated_unused_voters