# By Amos Satterlee, edited by Oliver Switzer


def hello():
    print 'Hello!'
 
def rect_area(width, height):
    return width * height

def sqr_area(x):
	return x ** 2

def circ_area(radius):
	return 3.141 * radius ** 2
 
def print_welcome(name):
    print 'Welcome,', name

def help():
	print 'Hotkeys to find the area of different things:'
	print '		"r" --> Find the area of a rectangle if given the width and height dimensions'
	print '		"s" --> Find the area of a square if given the length of one side'
	print '		"c" --> Find the area of a circle if given the radius'
	print 'Press "q" to quit the program'
	print 'Press "h" to display this help message'



name = raw_input('Your Name: ')
hello(),
print_welcome(name)

choice = "h"

while choice != "q":

	if choice == "r":
		print
		print "Finding the area of a rectangle:"

		w = input ('Width ')
		
		while w <= 0:
		    print 'Must be a positive number'
		    w = input('Width: ')
 
		h = input('Height: ')
		while h <= 0:
		    print 'Must be a positive number'
		    h = input('Height: ')

 		print 'Width =', w, 'Height =', h, 'so Area =', rect_area(w, h)
 		print "***" * 25

 	if choice == "s":
 		print
 		print "Finding the area of a square:"

		x = input('Length of one side: ')

		while x <= 0:
			print 'Must be a positive number'
			x = input('Width: ')
		# while type(x) != int:
		# 	print 'Must be an integer'

		print 'Side of one side =', x, 'so Area =', sqr_area(x)
		print "***" * 25

	if choice == "c":
		print
		print "Finding the area of a circle:"

		r = input('Radius: ')

		while r <= 0:
			print 'Must be a positive number'
			r = input('Radius: ')

		print "Radius of circle =", r, "so Area =", circ_area(r)
		print "***" * 25

	if choice =="h":
		print
		help()
		print "***" * 25

	elif choice != "q":
		help()

	choice = raw_input("Option: ")


