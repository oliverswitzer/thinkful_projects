import operator


class TaskList:

	def __init__(self):
		self.task_dict = {}

	def addtask(self, Task, priority):
		self.task_dict[Task] = int(priority)   # add a task and priority value to the task dictionary
		if Task == "" or priority == "":
			raise SyntaxError("Please input a task")
		if not isinstance(Task, str):
			raise ValueError("Please enter a text value for the task")

	def sort_tasks(self, task_dict_input):

		sorted_tasks = sorted(task_dict_input.iteritems(), key=operator.itemgetter(1), reverse = True)
		return sorted_tasks

	
	def printtasks(self, sorted_tasks):
		for k, v in self.sorted_tasks.iteritems():
			print k,
			print " ",
			print v.rjust(20, '*')

if __name__ == "__main__":

	examp_task_dict  = TaskList()
	
	running = True
	while running: 
		task = raw_input("Enter a task you need to complete: ")
		priority = raw_input("From 1-10, 10 being the most important and 1 being the least important, how important is this task: ")
		examp_task_dict.addtask(task, priority)

		print "***" * 25
		quit = raw_input("Quit? Press 'q' to quit and see tasks or press enter to continue: ")
		if quit == "q":
			running = False

	sorted_tasks = examp_task_dict.sort_tasks(examp_task_dict)	
	examp_task_dict.printtasks(sorted_tasks)

	# {'feed dog':'3', 'eat something':'5', 'do math homework':'1'}
	