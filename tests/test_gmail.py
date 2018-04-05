import unittest


#python -m unittest -v test_module
class Gmail__get_unread_email_ids(unittest.TestCase):

	def setUp(self):
		# mock gmail_client.users().messages().list(userId='me',q='is:unread').execute()
		pass




class Gmail__get_all_unread(unittest.TestCase):
	
	def test_reply_to_our_email(self):
		pass

	def test_sender_replies_to_self(self):
		pass

	def test_third_party_replies(self):
		pass
		# this is situation where sender forwards to or cc'tests 3rd party and they
		# send response at some point.  Not even sure what behavior should be here.

class Gmail__mark_as_unread(unittest.TestCase):
	pass


class Gmail__get_sender(unittest.TestCase):
	
	def test_reply_to_our_email(self):
		pass

	def test_sender_replies_to_self(self):
		pass





class Gmail__get_text(unittest.TestCase):
	pass


class Gmail__get_attachment(unittest.TestCase):
	pass


class Gmail__send_email(unittest.TestCase):
	pass