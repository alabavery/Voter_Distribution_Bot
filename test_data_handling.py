import unittest
import data_handling


class DataHandling__update_for_sent_voters(unittest.TestCase):

	def setUp(self):
		self.seen_data = {'an_email@gmail.com':{'sender':'an_email@gmail.com','voters':['a','b','c']}}

	def test_basic_new_entry(self):
		sender = 'another_email@gmail.com'
		some_voters = ['1','2','3']
		found = data_handling.update_for_sent_voters(sender, some_voters, self.seen_data)[sender]
		expected =  {'sender':'another_email@gmail.com', 'voters':['1','2','3']}
		self.assertEqual(found, expected)

	def test_basic_update_existing_entry(self):
		sender = 'an_email@gmail.com'
		some_voters = ['1','2','3']
		found = data_handling.update_for_sent_voters(sender, some_voters, self.seen_data)
		expected = {'an_email@gmail.com':{'sender':'an_email@gmail.com','voters':['a','b','c','1','2','3']}}
		self.assertEqual(found, expected)

	def test_sender_is_type_int(self):
		with self.assertRaises(AssertionError):
			data_handling.update_for_sent_voters(1, ['a'], self.seen_data)

	def test_voters_is_type_str(self):
		with self.assertRaises(AssertionError):
			data_handling.update_for_sent_voters('a', 'new voter', self.seen_data)

	def test_seen_data_is_type_list(self):
		with self.assertRaises(AssertionError):
			data_handling.update_for_sent_voters('a', ['a'], [self.seen_data])

	

# class DataHandling__find_email(unittest.TestCase):

# 	def setUp(self):
# 		self.seen_data_with_no_bracket = {'an_email@gmail.com':{
# 											'voters':[
# 												'a','b','c'
# 											]
# 										}}
# 		self.seen_data_with_bracket = {'<an_email@gmail.com>':{
# 											'voters':[
# 												'a','b','c'
# 											]
# 										}}
# 		self.new_sender_with_bracket = '<an_email@gmail.com>'
# 		self.new_sender_with_no_bracket = 'an_email@gmail.com'

# 	def assert_new_in_seen(self, new, old):
# 		found = data_handling.get_email_index(new, old)
# 		self.assertEqual(found, )

# 	def test_true_new_email(self):
# 		found = data_handling.get_email_index('something new', self.seen_data_with_no_bracket)
# 		expected = False
# 		self.assertEqual(found, expected)

# 	def test_true_seen_email(self):
# 		data = [
# 			{'sender_address':'email0@gmail.com', 'voters':['a','b','c']},
# 			{'sender_address':'email1@gmail.com', 'voters':['a','b','c']},
# 			{'sender_address':'email2@gmail.com', 'voters':['a','b','c']},
# 			{'sender_address':'email3@gmail.com', 'voters':['a','b','c']},
# 		]
# 		found = data_handling.get_email_index('email2@gmail.com', data)
# 		self.assertEqual(found, 2)

# 	def test_new_has_brackets_old_doesnt(self):
# 		self.assert_new_in_seen(self.new_sender_with_bracket, self.seen_data_with_no_bracket)

# 	def test_new_no_brackets_old_does(self):
# 		self.assert_new_in_seen(self.new_sender_with_no_bracket, self.seen_data_with_bracket)

# 	def test_new_has_brackets_old_does_too(self):
# 		self.assert_new_in_seen(self.new_sender_with_bracket, self.seen_data_with_bracket)

# 	def test_new_no_brackets_old_doesnt_either(self):
# 		self.assert_new_in_seen(self.new_sender_with_no_bracket, self.seen_data_with_no_bracket)

# 	def test_duplicate_entries(self):
# 		seen_data = [{'sender_address':'an_email@gmail.com', 'voters':['a','b','c']}, 
# 					{'sender_address':'an_email@gmail.com', 'voters':['b','d']}]
# 		with self.assertRaises(RuntimeError):
# 			data_handling.get_email_index('an_email@gmail.com', seen_data)


# class DataHandling__add_entry(unittest.TestCase):
# 	# make sure it isn't changing structure of data... this was actual problem
# 	def test_that_struct_unchanged(self):
# 		seen_email_data = [
# 			{'sender_address':'email0@gmail.com', 'voters':['a','b','c']},
# 			{'sender_address':'email1@gmail.com', 'voters':['a','b','c']},
# 			{'sender_address':'email2@gmail.com', 'voters':['a','b','c']},
# 			{'sender_address':'email3@gmail.com', 'voters':['a','b','c']},
# 		]
# 		new_sender, some_voters = 'im_new@g.com', ['3','2','1']
# 		seen_email_data = data_handling.add_entry(new_sender, some_voters, seen_email_data)

# 		for entry in seen_email_data:
# 			assert type(entry) == dict
# 			assert type(entry['voters']) == list


# class DataHandling__add_voters_to_entry(unittest.TestCase):

# 	def setUp(self):
# 		self.seen_email_data = [
# 			{'sender_address':'email0@gmail.com', 'voters':['a','b','c']},
# 			{'sender_address':'email1@gmail.com', 'voters':['a','b','c']},
# 			{'sender_address':'email2@gmail.com', 'voters':['a','b','c']},
# 			{'sender_address':'email3@gmail.com', 'voters':['a','b','c']},
# 		]

# 	def test_basic(self):
# 		sender, some_voters = 'email3@gmail.com', ['3','2','1']
# 		seen_email_data = data_handling.add_voters_to_entry(sender, some_voters, self.seen_email_data)
# 		found = sorted(seen_email_data[sender]['voters'])
# 		expected = sorted(['a','b','c'] + ['3','2','1'])
# 		self.assertEqual(found, expected)
	
# 	def test_that_struct_unchanged(self):
# 		sender, some_voters = 'email1@gmail.com', ['3','2','1']
# 		seen_email_data = data_handling.add_voters_to_entry(sender, some_voters, self.seen_email_data)

# 		for entry in seen_email_data:
# 			assert type(entry) == dict
# 			assert type(entry['voters']) == list

# 	def test_with_0_index(self):
# 		sender, some_voters = 'email1@gmail.com', ['3','2','1']
# 		seen_email_data = data_handling.add_voters_to_entry(sender, some_voters, self.seen_email_data)
# 		found = sorted(seen_email_data[sender]['voters'])
# 		expected = sorted(['a','b','c'] + ['3','2','1'])
# 		self.assertEqual(found, expected)


# class DataHandling__remove_from_unused(unittest.TestCase):
# 	pass


