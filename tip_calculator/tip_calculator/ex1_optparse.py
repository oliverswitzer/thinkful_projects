from optparse import OptionParser   #import the OptionParser object from this module
 
 
parser = OptionParser()     #create an instance of OptionParser that we can
                            #use in this script. We'll learn more about 
                            #objects and instances later in this course.
 
parser.add_option("-f", "--first", dest="first_arg", help="the first argument")
parser.add_option("-s", "--second", dest="second_arg", help="the second argument")
 
#in those two lines above, we're adding two slots in our parser, so that we can
#pass two named arguments from the command line. At the command line, we'll be 
#able to run the following command: python -f "my first argument" -s 2
#which would output "The first argument is my first argument."
#                   "The second argument is 2."
 
(options, args) = parser.parse_args() # this calls the parse_args method on our 
                                      # parser, which will assign the user inputs
                                      # from the command line to the destinations
                                      # we've specified in lines 10 and 11 with
                                      # dest=
 
print "The first argument is '{}'.".format(options.first_arg)
print "The second argument is '{}'.".format(options.second_arg)