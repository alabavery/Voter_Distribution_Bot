import os

CLIENT_SECRET_FILE_PATH = "secrets/client_secret.json"
SEEN_EMAIL_DATA_FILE_PATH = "data/seen_email_data.json"
UNUSED_VOTERS_FILE_PATH = "data/unused_voters.json"

ERROR_LOG_FILE_PATH = "logs/error_log.txt"
ROUTINE_ACTION_LOG_FILE_PATH = "logs/routine_log.txt"
ABNORMAL_ACTION_LOG_FILE_PATH = "logs/abnormal_log.txt"
IGNORE_LOG_FILE_PATH = "logs/ignored_log.txt"

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.modify']

NUMBER_OF_VOTERS_TO_SEND = 10



def read_file(file_path):
    with open(file_path) as f:
        data = f.read()
    return data

BOT_MESSAGES = dict(
    MESSAGE_FOR_ASKING_IF_PEOPLE_WANT_MORE=read_file('secrets/bot_messages/message_for_asking_if_people_want_more.txt'),
    MESSAGE_WHEN_BOT_DOESNT_UNDERSTAND=read_file('secrets/bot_messages/message_when_bot_doesnt_understand.txt'),
    MESSAGE_WHEN_SENDING_VOTERS=read_file('secrets/bot_messages/message_when_sending_voters.txt'),
    MESSAGE_WHEN_SOMEONE_CANT_MAIL_THEIR_VOTERS=read_file('secrets/bot_messages/message_when_someone_cant_mail_their_voters.txt'),
)