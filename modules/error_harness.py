import file_io, my_logging, gmail_handling, gmail_client, config

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
		file_io.write_json(seen_email_data, config.SEEN_EMAIL_DATA_FILE_PATH)
		file_io.write_json(unused_voters, config.UNUSED_VOTERS_FILE_PATH)
		# log should never fail, so no need for try/except here
		my_logging.error_log(fxn, fxn_params, e)

		# even within this safety part of the harness, gmail_handling.mark_as_read() could fail,
		# so let'tests make sure we also catch that
		try:
			gmail_handling.mark_as_read(gmail_client, ids_to_mark_read)
		except Exception as gmail_exception:
			# log should never fail and if it does I'm ok with breaking, so no need for try/except here
			my_logging.error_log(gmail_handling.mark_as_read, (gmail_client, ids_to_mark_read), gmail_exception)
			print("In addition to the exception caught by error_harness, error_harness ran into exception marking emails read -- see error log")
		raise