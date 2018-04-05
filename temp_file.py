import json

# client = gmail_client.get_gmail_client(config.CLIENT_SECRET_FILE_PATH, config.SCOPES, secret.APPLICATION_NAME)
# # # ids = gmail_handling.get_unread_email_ids(client)
# # # messages = [client.users().messages().get(userId='me', id=i).execute() for i in ids]
# # # j = json.dumps(messages)
# # # with open('temp_file.json', 'w') as f:
# # #     f.write(j)
# #
# #
# response = client.users().messages().list(userId='me').execute()
# messages = []
# messages.extend(response['messages'])
#
# while 'nextPageToken' in response:
#     page_token = response['nextPageToken']
#     response = client.users().messages().list(userId='me', pageToken=page_token).execute()
#     messages.extend(response['messages'])
#
# with open('temp_file.json', 'w') as f:
#     f.write(json.dumps(messages))
#
#
#
# #
# def get_emails(client, email_ids):
#     return [client.users().messages().get(userId='me', id=this_id).execute() for this_id in email_ids]
#
# with open('temp_file.json', 'r') as f:
#     # all_m = json.loads(f.read())
#     # gillians_thread = [thing for thing in all_m if thing['threadId'] == ''
#     ids = [thing['id'] for thing in json.loads(f.read())]
#
# messages = get_emails(client, ids)
# with open('temp_file2.json', 'w') as f:
#     f.write(json.dumps(messages))

with open('temp_file2.json', 'r') as f:
    emails = json.loads()
# response = client.users().messages().list(userId='me', q="from:al.avery.dev@gmail.com is:unread").execute()
# print(response)
# print(client.users().messages().get(userId='me', id='1608142e27795680').execute())
