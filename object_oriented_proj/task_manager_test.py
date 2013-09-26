


import unittest
from task_manager import Task


class TaskManagerTest(unittest.TestCase):

	def setUp(self):
		self.task = Task()

	def test_that_user_cant_enter_empty_task(self):
		self.assertRaises(SyntaxError, self.task.addtask, "", "10") 
	def test_that_task_isnt_numerical_value(self):
		self.assertRaises(ValueError, self.task.addtask, "10", "4")
	def test_that_user_enters_a_priority_value_to_complete_task(self):
		self.assertRaises(SyntaxError, self.task.addtask, "Feed dog", "")
	
