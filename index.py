import config, secret, gmail_client, gmail_handling, new_email, core_logic, file_io, my_logging

import pprint
pp = pprint.PrettyPrinter(indent=2)

SEEN_EMAIL_DATA_FILE_PATH = config.SEEN_EMAIL_DATA_FILE_PATH
UNUSED_VOTERS_FILE_PATH = config.UNUSED_VOTERS_FILE_PATH
gmail_client = gmail_client.get_gmail_client(
	config.CLIENT_SECRET_FILE_PATH,
	config.SCOPES,
	secret.APPLICATION_NAME
)

def error_harness(seen_email_data, unused_voters, ids_to_mark_read, fxn, *fxn_params):
	"""
	If we error out at some point, we may have already handled some emails and/or sent out
	some voters.  We need to make sure this is kept track of in (1) unused_voters, (2) seen_email_data
	and (3) in terms of marking emails as read.  This is harness to make sure these things get
	accomplished.
	:param seen_email_data: the data from seen_email_data.json
	:param unused_voters: the data from unused_voters.json
	:param ids_to_mark_read: the running list of message ids for those gmails that we have
	handled.  This is list of str.
	:param fxn: The actual function object that this harness is around
	:param fxn_params: the parameters for that function
	:return: the return of the harnessed function (if all goes well, otherwise, raise)
	"""
	try:
		# hopefully this is the only part of the harness that actually has to run
		return fxn(*fxn_params)
	except Exception as e:
		# file_io should never fail, so no need for try/except here
		file_io.write_json(seen_email_data, SEEN_EMAIL_DATA_FILE_PATH)
		file_io.write_json(unused_voters, UNUSED_VOTERS_FILE_PATH)
		# log should never fail, so no need for try/except here
		my_logging.error_log(fxn, fxn_params, e)

		# even within this safety part of the harness, gmail_handling.mark_as_read() could fail,
		# so let's make sure we also catch that
		try:
			gmail_handling.mark_as_read(gmail_client, ids_to_mark_read)
		except Exception as gmail_exception:
			# log should never fail and if it does I'm ok with breaking, so no need for try/except here
			my_logging.error_log(gmail_handling.mark_as_read, (gmail_client, ids_to_mark_read), gmail_exception)
			print("In addition to the exception caught by error_harness, error_harness ran into exception marking emails read -- see error log")
		raise


if __name__ == '__main__':
	# of format {email: [voter, voter,..], email2: [..]}
	seen_email_data = file_io.read_json(SEEN_EMAIL_DATA_FILE_PATH)
	unused_voters = file_io.read_json(UNUSED_VOTERS_FILE_PATH)
	if not seen_email_data:
		raise RuntimeError("Fucked up on line 53")

	unread_email_ids = gmail_handling.get_unread_email_ids(gmail_client)
	raw_unread_email_data = gmail_handling.get_emails(gmail_client, unread_email_ids)

	ids_to_mark_read = []
	for email_id, raw_email_datum in raw_unread_email_data:
		print("\nNext up, email id #{0}".format(email_id))

		# MAKE EMAIL OBJECT
		newemail = new_email.NewEmail()
		error_harness(seen_email_data, unused_voters, ids_to_mark_read, newemail.main, email_id,
								 raw_email_datum, seen_email_data)
		if not seen_email_data:
			raise RuntimeError("Fucked up on line 64")
		# for v in dir(newemail):
		# 	if "__" not in v and v != 'raw':
		# 		print("{0} --- {1}".format(v, getattr(newemail, v)))

		# print("Sender {0}| should ignore {1}".format(newemail.sender, newemail.should_ignore))
		# if not newemail.should_ignore:
		# 	print("Attach {0}| From Seen {1} | From Active {2} | Surrender {3}".format(
		# 		newemail.attach,
		# 		newemail.from_seen,
		# 		newemail.from_active,
		# 		newemail.surrender
		# 	))
        #
		# DECIDE WHAT TO DO NAD GET APPROPRIATE HANDLER BASED ON ATTRIBUTES OF THE NEWLY-CREATED OBJECT
		handler, is_expected = error_harness(
			seen_email_data, unused_voters, ids_to_mark_read, core_logic.decide_what_to_do_with_email, newemail
		)

		# USE HANDLER
		if handler != None:
			seen_email_data, unused_voters = error_harness(
				seen_email_data,
				unused_voters,
				ids_to_mark_read,
				handler,
				newemail, seen_email_data, unused_voters, gmail_client # the params used by all handlers
			)
			# LOG USE OF HANDLER
			my_logging.log(handler, is_expected, newemail)

		else:
			# ALSO LOG IF WE IGNORED AN EMAIL
			my_logging.log(handler, is_expected, newemail)

		# OK TO QUEUE UP TO MARK AS READ NOW
		ids_to_mark_read.append(email_id)

	# SAVE THE DATA
	file_io.write_json(seen_email_data, SEEN_EMAIL_DATA_FILE_PATH)
	file_io.write_json(unused_voters, UNUSED_VOTERS_FILE_PATH)
	# MARK AS READ
	print("Not using error harness for mark_as_read() b/c this is last line of file.")
	gmail_handling.mark_as_read(gmail_client, ids_to_mark_read)
