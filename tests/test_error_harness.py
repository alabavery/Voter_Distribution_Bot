import index
import unittest
import unittest.mock


# when error in subject function
#     - should log to error log
#     - should write seen email and unused
#     - should mark stuff as read
#         - if error here, log to error log as well
# Should work with function with any num of args

class TestErrorHarness(unittest.TestCase):
    def make_an_error(self):
        int("not int-able")

    def dont_make_an_error(self):
        return "here'tests the return"

    def dont_make_an_error_w_args(self, arg1, arg2):
        return "here'tests the return"

    def setUp(self):
        self.seen_email_data = ['some seen email data']
        self.unused_voters = ['some voters']
        self.ids_to_mark_read = ['an id']


    def test_no_args(self):
        found = index.error_harness(self.seen_email_data, self.unused_voters, self.ids_to_mark_read, self.dont_make_an_error)
        self.assertEqual(found, self.dont_make_an_error())

    def test_multiple_args(self):
        found = index.error_harness(self.seen_email_data, self.unused_voters, self.ids_to_mark_read,
                                    self.dont_make_an_error_w_args, "arg1", "arg2")
        self.assertEqual(found, "here'tests the return")

    @unittest.mock.patch('index.file_io.write_json')
    @unittest.mock.patch('index.gmail_handling.mark_as_read')
    @unittest.mock.patch('index.my_logging.error_log')
    def test_all_get_called_when_error(self, json_patch, mark_as_read_patch, error_log_patch):
        index.error_harness(self.seen_email_data, self.unused_voters, self.ids_to_mark_read,
                                    self.make_an_error)
        json_patch.assert_called()
        mark_as_read_patch.assert_called()
        error_log_patch.assert_called()