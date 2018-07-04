import os

def confirm_move_forward(message):
    move_forward = 'n'
    while move_forward.lower() != 'y':
        move_forward = input('{0} (y)'.format(message))


confirm_move_forward('Make bot message files?')
######################################
# MAKE THE BOT MESSAGE AND LOG FILES #
######################################
def make_dir_and_text_files(directory, file_names):
    if os.path.isdir(directory):
        print("Directory already exists!")
        return
    os.makedirs(directory)

    for file_name in file_names:
        with open('{0}/{1}.txt'.format(directory, file_name), 'w') as f:
            f.write("Put your content here.")


# make bot message files
path_to_bot_messages = 'secrets/bot_messages'

bot_message_file_names = [
    'disclaimer_prefix',
    'message_for_asking-if_people_want_more',
    'message_when_bot_doesnt_understand',
    'message_when_sending_voters',
    'message_when_someone_cant_mail_their_voters'
]
make_dir_and_text_files(path_to_bot_messages, bot_message_file_names)

confirm_move_forward('Make log files?')
# make log files
path_to_logs = './logs'
log_file_names = ['abnormal_log', 'error_log', 'ignored_log', 'routine_log']
make_dir_and_text_files(path_to_logs, log_file_names)


confirm_move_forward('Make voter data files? Remember to format the voter file properly before proceeding.')
################################################
# READ THE VOTER FILE AND FORMAT APPROPRIATELY #
################################################
import csv
import json
import config

with open('voter_file.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    assert config.VOTER_DATA_FIELDS == [header.lower() for header in headers]

    voter_data = [{
        config.VOTER_DATA_FIELDS[0]: row[0], # name
        config.VOTER_DATA_FIELDS[1]: row[1], # street address
        config.VOTER_DATA_FIELDS[2]: row[2], # apt number
        config.VOTER_DATA_FIELDS[3]: row[3], # zip
        config.VOTER_DATA_FIELDS[4]: row[4], # city
    } for row in reader]

if not os.path.isdir('data'):
    os.makedirs('data')
with open('data/unused_voters.json', 'w') as f:
    f.write(json.dumps(voter_data))


#####################################
# MAKE A BLANK SEEN_EMAIL_DATA FILE #
#####################################
with open('data/seen_email_data.json', 'w') as f:
    f.write('{}')