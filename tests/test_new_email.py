import unittest
from modules.new_email import extract_part_of_snippet, find_email_substring, EmailValueNotPresent


"""
MAY ALSO WANT TO TEST YOUR EMAIL EXPECTATIONS WITH REAL DATA! FOR INSTANCE, TEST THAT SNIPPET NEVER BEGINS WITH ON APR 5, 2018...
"""


class NewEmail__extract_part_of_snippet(unittest.TestCase):

	def setUp(self):
		self.basic_raw = dict(snippet='snippet')

	def test_gets_snippet(self):
		self.assertEqual('snippet', extract_part_of_snippet('', '', self.basic_raw))

	def test_finds_heading_without_weekday(self):
		raw = dict(snippet="Here is the text before On Apr 15, 2018, at 10:51 AM and here is the text after")
		found = extract_part_of_snippet('', '', raw)
		expected = "Here is the text before "
		self.assertEqual(found, expected)

	def test_finds_heading_with_weekday(self):
		raw = dict(snippet="Here is the text before On Wed, Jul 5, 2018, at 10:51 AM and here is the text after")
		found = extract_part_of_snippet('', '', raw)
		expected = "Here is the text before "
		self.assertEqual(found, expected)

	def test_both_headings_present(self):
		raw = dict(snippet="Here is the text before On Wed, Apr 15, 2018, at here's some more On May 5, 2018")
		found = extract_part_of_snippet('', '', raw)
		expected = "Here is the text before "
		self.assertEqual(found, expected)

	def test_both_headings_present2(self):
		raw = dict(snippet="Here is the text before On Apr 5, 2018, at here's some more On Wed, Apr 5, 2018")
		found = extract_part_of_snippet('', '', raw)
		expected = "Here is the text before "
		self.assertEqual(found, expected)

	def test_raises_when_no_snippet(self):
		raw = dict(not_snippet='something else')
		with self.assertRaises(EmailValueNotPresent):
			extract_part_of_snippet('', '', raw)


class NewEmail__find_email_substring(unittest.TestCase):

	def test_true_positive(self):
		sender_string = "email email email a@b"
		found = find_email_substring(sender_string)
		self.assertEqual("a@b", found)

	def test_no_false_positive(self):
		sender_string = "email email email"
		found = find_email_substring(sender_string)
		self.assertEqual(False, found)


class NewEmail__find_email_substring(unittest.TestCase):

