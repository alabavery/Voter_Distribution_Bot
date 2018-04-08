import config
from secrets import secret
from modules import gmail_client, file_io, gmail_handling, new_email, error_harness, core_logic, my_logging
error_harness = error_harness.error_harness

import pprint
pp = pprint.PrettyPrinter(indent=2)

gmail_client = gmail_client.get_gmail_client(
	config.CLIENT_SECRET_FILE_PATH,
	config.SCOPES,
	secret.APPLICATION_NAME
)


if __name__ == '__main__':
	# seen_email_data is of format {email: [voter, voter,..], email2: [..]}
	seen_email_data = file_io.read_json(config.SEEN_EMAIL_DATA_FILE_PATH)
	# unused voters is of format ...
	unused_voters = file_io.read_json(config.UNUSED_VOTERS_FILE_PATH)

	unread_email_ids = gmail_handling.get_unread_email_ids(gmail_client)
	raw_unread_email_data = gmail_handling.get_emails(gmail_client, unread_email_ids)

	ids_to_mark_read = []
	for email_id, raw_email_datum in raw_unread_email_data:
		print("\nNext up, email id #{0}".format(email_id))

		# MAKE EMAIL OBJECT
		newemail = new_email.NewEmail()
		error_harness(seen_email_data, unused_voters, ids_to_mark_read, newemail.main, email_id,
								 raw_email_datum, seen_email_data)

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

		print("\n\n")
		print(newemail)
		print("\nUsing handler {0} (but not actually sending email)".format(handler))

		cont = input("Go to next one?")
		while cont != 'y':
			cont = input("Go to next one?")
    #
	# # SAVE THE DATA
	# file_io.write_json(seen_email_data, config.SEEN_EMAIL_DATA_FILE_PATH)
	# file_io.write_json(unused_voters, config.UNUSED_VOTERS_FILE_PATH)
	# # MARK AS READ
	# print("Not using error harness for mark_as_read() b/c this is last line of file.")
	# gmail_handling.mark_as_read(gmail_client, ids_to_mark_read)
