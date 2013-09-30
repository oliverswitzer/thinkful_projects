


import unittest
from task_manager import TaskList, NewTask 


class NewTaskTest(unittest.TestCase):

	def setUp(self):
		self.task = NewTask()
	def test_that_user_cant_enter_empty_task(self):
		self.assertRaises(SyntaxError, self.task, "", "10") 
	def test_that_task_isnt_numerical_value(self):
		self.assertRaises(ValueError, self.task, "10", "4")
	def test_that_user_enters_a_priority_value_to_complete_task(self):
		self.assertRaises(SyntaxError, self.task, "Feed dog", "")
	def test_that_user_enters_a_priority_value_betwn_1_and_10(self):
		self.assertRaises(ValueError, self.task, "feed dog", "12")
	
