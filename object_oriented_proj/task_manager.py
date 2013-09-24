import operator

class Task:

	task_dict = {}

	def addtask(self, Task, priority):
		self.task_dict[Task] = int(priority)
		if Task == "" or priority == "":
			raise SyntaxError("Please input a task")

	def sort_tasks(self, task_dict):

		x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
		sorted_tasks = sorted(task_dict.iteritems(), key=operator.itemgetter(1), reverse = True)
		return sorted_tasks

	
	def printtasks(self):
		for k, v in self.task_dict.iteritems():
			print k,
			print " ",
			print v.rjust(20, '*')

if __name__ == "__main__":
	task_dict  = {'feed dog':'3', 'eat something':'5', 'do math homework':'1'}
	print sort_tasks(task_dict)
