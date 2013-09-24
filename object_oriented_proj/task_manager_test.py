


import unittest
from task_manager import Task
 
class TaskManagerTest(unittest.TestCase):


	def setUp(self):
		self.task = Task()

	def test_that_user_cant_enter_empty_task(self):
		self.assertRaises(SyntaxError, self.task.addtask, None, "10:30") 

	def test_that_user_enters_a_time_to_complete_task(self):
		self.assertRaises(SyntaxError, self.task.addtask, "Feed dog", None)

	
