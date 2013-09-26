import operator


class TaskList:

	def __init__(self):
		self.task_dict = {}
	
	def sort_tasks(self):
		self.sorted_tasks = sorted(self.task_dict.iteritems(), key=operator.itemgetter(1), reverse = True) #trying to sort the dictionary of 

	def printtasks(self):  #prints out the task in an ordered list by priority
		
		print "___" * 25
		print """


		"""
	
		print "Your tasks in order of priority, monsieur:"
		for task, priority in self.sorted_tasks:
			print task,
			# print " *** ",
			string_priority = " " + str(priority) 
			print string_priority.rjust(20, '*') 
			   #pads the value of the dictionary by 20 "*"
		print """
		
		
		"""
		print "___" * 25

	def addtask(self, Task, priority):
		self.task_dict[Task] = int(priority)

class NewTask:

	def __init__(self):
		self.task = raw_input("Please input a task: ")
		self.priority = int(raw_input("Please input a value for the priority of this task: "))
		if self.task == "":   #if task left blank raise syntax error
			raise SyntaxError("Please input a task")
		elif self.priority == "": #if priority left blank, raise syntax error
			raise SyntaxError("Please input a value for the priority of this task")
		elif not isinstance(self.task, str):   #if user doesn't enter a str value for task gives error
			raise ValueError("Please enter a text value for the task")
		elif not isinstance(self.priority, int):   #if user doesnt enter int value for priority gives error
			raise ValueError("Please enter a integer from 1-10 for the priority of this task")

		
if __name__ == "__main__":

	examp_task_dict  = TaskList()  #create an instance of a task list
	
	running = True
	while running: 
		task_input = NewTask()  #Create new task instance value to be placed in task dictionary
		examp_task_dict.addtask(task_input.task, task_input.priority)  #appends task and corresponding priority number to examp_task_dict dictionary

		quit = raw_input("*** Quit? Press 'q' to quit and see tasks or press enter to continue: ")
		if quit == "q":
			running = False

	examp_task_dict.sort_tasks()  #passes the examp_task_dict dictionary to the sort tasks function. Sorts by order of priority
	examp_task_dict.printtasks()  #prints the tasks out in order. See printtasks function



	# {'feed dog':'3', 'eat something':'5', 'do math homework':'1'}
	