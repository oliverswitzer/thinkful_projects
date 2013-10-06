# class Goldfish: 
# 	breathes_in_water = True
# 	skin = "scales"
# 	def move(self, speed):
# 		print "Swimming upright %s!" % speed

# class Flounder:
# 	breathers_in_water = True
# 	skin = "scales"
# 	def move(self, speed):
# 			print "Swimming sideways %s!" % speed

### THE ABOVE CODE IS REDUNDANT AND UNECESSARY: INTRO TO PARENT CLASSES

class Fish(object):    #Parent class. It is always given the parent "object"
					   #object class is the parent of all parents.
	skin = "scales"
	color = "blue"

class Goldfish(Fish):	# Fish specified as parent of this child class
	def move(self, speed):
		print "Moving %s" % speed
	color = "gold"   #this color overrides the parent color

class Flounder(Fish):  #Another child class
	pass

spencer = Goldfish()
susan = Flounder()

print spencer.skin # It has skin from the Fish class


#Classes will inherit all of their parent's behavior and properties

#However, child classes can also override parent's behavior

print susan.color
print spencer.color #spencers color is gold, not blue, because it was specifieid
					  # when it was defined in the Goldfish class. 

# We can test if an instance is a certain class:

print isinstance(spencer, Fish)
print isinstance(spencer, Goldfish)
print isinstance(spencer, Flounder)
