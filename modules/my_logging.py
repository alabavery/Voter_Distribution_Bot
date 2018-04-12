import config
from datetime import datetime
import traceback


def add_to_file(file_path, additional_content):
    with open(file_path, 'r') as f:
        file_content = f.read()
    with open(file_path, 'w') as f:
        f.write(file_content + "\n\n\n" + additional_content)


def log(handler_used, is_expected, rationale, newemail):
    if is_expected:
        if handler_used != None:
            log_file_path = config.ROUTINE_ACTION_LOG_FILE_PATH
            message_intro = "Used'{0}' on new email because {1}".format(handler_used, rationale)
        else:
            assert newemail.should_ignore == True
            log_file_path = config.IGNORE_LOG_FILE_PATH
            message_intro = "Ignored new email because {0}".format(rationale)
    else:
        log_file_path = config.ABNORMAL_ACTION_LOG_FILE_PATH
        message_intro = "Used  '{0}' on new email".format(handler_used)

    logs = "{0}\n".format(datetime.now().strftime("%A %m-%d-%Y at %I:%M:%S"))
    logs += "{0}\n".format(message_intro)

    email_property_logs = ["Sender: {0}   |   Email id: {1}".format(newemail.sender, newemail.email_id)]

    if not newemail.should_ignore:
        addl_props = ['Attach', 'Surrender', 'Asks_For_More', 'From_Seen', 'From_Active', 'Text']
        email_property_logs += ["{0}: {1}".format(prop, getattr(newemail, prop.lower())) for prop in addl_props]

    logs += "   |   ".join(email_property_logs)
    add_to_file(log_file_path, logs)


def error_log(fxn, fxn_params, exception):
    fxn_log = "Function: {0}".format(fxn)
    fxn_params_log = "Function params: {0}".format(str(fxn_params))
    exception_log = "---Exception below---\n{0}".format(traceback.format_exc())
    logs = "\n".join([fxn_log, fxn_params_log, exception_log])
    add_to_file(config.ERROR_LOG_FILE_PATH, logs)
