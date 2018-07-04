
def reformat_email_address(email_address):
	return email_address.strip().replace('<','').replace('>','')


"""
{'apt_number': 'Apartment Number',
 'city': 'City',
 'name': 'Voter name',
 'street': 'Street Name',
 'street_number': 'House Number',
 'zip_code': 'Zip Code'}
"""
def prettify_voter(voter):
	pretty_apt_number = ", #" + voter['apt_number'] if len(voter['apt_number']) > 0 else ""
	pretty_address = "{0} {1}".format(voter['street_address'], pretty_apt_number)

	return "{0}\n{1}\n{2} {3}".format(
		voter['name'],
		pretty_address,
		voter['city'],
		voter['zip_code']
	)


def prettify_voters(voters):
	return "\n\n".join([prettify_voter(voter) for voter in voters])