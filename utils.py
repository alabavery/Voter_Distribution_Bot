
def reformat_email_address(email_address):
	return email_address.strip().replace('<','').replace('>','')


def pretty_format_voters(voters):
	return "\n".join(voters)