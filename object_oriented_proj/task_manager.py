

class Task:

	task_dict = {}

	def addtask(self, Task, time):
		self.task_dict[Task] = time
		if Task == None or time == None:
			raise SyntaxError("Please input a task")

