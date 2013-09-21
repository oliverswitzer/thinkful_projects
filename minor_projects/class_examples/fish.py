# see this presentation for a guide to this code http://slid.es/jasonmyers/learnpython-classes


class Goldfish:
	breathes_in_water = True
	skin = "scales"

	def move(self, speed):
		print self.name + " is moving " + speed + "!"  #prints out "name_of_the_fish_instance is moving speed_argument_passed"

	def __init__(self, fish_name):
		print "Fish init!" #When you want code to run whenever you create an instance of a Fish class,
						   # use __init__(self). This prints Fish init whenever you create a fish instance.
		self.name = fish_name   # Any parameters you pass into Fish() when you define an instance
						   		# Will be automatically passed into __init__()

class Flounder

myfish = Fish("Spencer")

#a = Fish()
#b = Fish()
#print a == b   #Two instances of the fish class are NOT the same

#myfish = Fish()   #Set an instance of the fish class
print myfish.skin   #print the variable 'skin' that is part of the fish class for myfish

if myfish.breathes_in_water:  #this will be true because the variable is defined as true in the Fish class
	print "Glug glug!" 

myfish.name = "Bob" #Redefines a variable for spencer called name and gives it value "bob". This gets called in the function move()
print myfish.move("fast") #move is a function defined in the Fish class. It takes "speed" as an input variable and prints 
						  #out that speed.

# Python automatically puts "myfish" into the "self" variable that was used in the function move (Defined in Fish class)
# So, really when the function move is called it looks like move(myfish, "fast")

# To customize your fish, you can put
# any variable on the instance you define.

myfish.color = "Gold" #define this fish instance's color

myotherfish = Fish("Susan")

myotherfish.color = "Blue"





