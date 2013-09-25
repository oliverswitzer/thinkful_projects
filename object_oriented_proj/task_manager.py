import operator


class TaskList:

	def __init__(self):
		self.task_dict = {}

	def addtask(self, Task, priority):
		self.task_dict[Task] = int(priority)   # add a task and priority value to the task dictionary
		if Task == "":   #if task left blank raise syntax error
			raise SyntaxError("Please input a task")
		elif priority == "": #if priority left blank, raise syntax error
			raise SyntaxError("Please input a value for the priority of this task")
		elif not isinstance(Task, str):   #if user doesn't enter a str value for task gives error
			raise ValueError("Please enter a text value for the task")
		elif not isinstance(priority, int):   #if user doesnt enter int value for priority gives error
			raise ValueError("Please enter a integer from 1-10 for the priority of this task")


	def sort_tasks(self, task_dict_input):

		sorted_tasks = sorted(task_dict_input.iteritems(), key=operator.itemgetter(1), reverse = True) #trying to sort the dictionary of 
																									   # tasks according to the numerical priority value of each task
		return sorted_tasks

	
	def printtasks(self, sorted_tasks):  #prints out the task in an ordered list by priority
		for k, v in self.sorted_tasks.iteritems():
			print k,
			print " ",
			print v.rjust(20, '*')    #pads the value of the dictionary by 20 "*"

if __name__ == "__main__":

	examp_task_dict  = TaskList()  #create an instance of a task list
	
	running = True
	while running: 
		task = raw_input("Enter a task you need to complete: ")   #Collect a task value to be placed in task dictionary
		priority = raw_input("From 1-10, how important is this task? ")
		examp_task_dict.addtask(task, priority)  #appends task and corresponding priority number to examp_task_dict dictionary

		print "***" * 25
		quit = raw_input("Quit? Press 'q' to quit and see tasks or press enter to continue: ")
		if quit == "q":
			running = False

	sorted_tasks = examp_task_dict.sort_tasks(examp_task_dict)	#passes the examp_task_dict dictionary to the sort tasks function. Sorts by order of priority
	examp_task_dict.printtasks(examp_task_dict)  #prints the tasks out in order. See printtasks function



	# {'feed dog':'3', 'eat something':'5', 'do math homework':'1'}
	