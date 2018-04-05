import os

CLIENT_SECRET_FILE_PATH = "client_secret.json"
SEEN_EMAIL_DATA_FILE_PATH = "seen_email_data.json"
UNUSED_VOTERS_FILE_PATH = "unused_voters.json"

ERROR_LOG_FILE_PATH = "logs/error_log.txt"
ROUTINE_ACTION_LOG_FILE_PATH = "logs/routine_log.txt"
ABNORMAL_ACTION_LOG_FILE_PATH = "logs/abnormal_log.txt"
IGNORE_LOG_FILE_PATH = "logs/ignored_log.txt"

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.modify']

BOT_MESSAGES = dict()
for bot_message_file in os.listdir('Bot_Messages'):
    with open('Bot_Messages/{0}'.format(bot_message_file), 'r') as f:
        BOT_MESSAGES[bot_message_file[:-4]] = f.read()

NUMBER_OF_VOTERS_TO_SEND = 10