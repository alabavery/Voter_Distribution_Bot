
def reformat_email_address(email_address):
	return email_address.strip().replace('<','').replace('>','')


def prettify_voters(voters):
	"""Presumably more will be done here eventually"""
	return "\n".join(voters)