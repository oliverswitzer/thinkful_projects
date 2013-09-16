from optparse import OptionParser   #import the OptionParser object from this module
 
 
parser = OptionParser()
parser.add_option("-f", "--first", dest="first_arg", help="the first argument",
                    default="something")  #You can use default= to assign a default
                                         # argument which will be used if the user
                                         # doesn't supply an argument at run time
 
parser.add_option("-s", "--second", dest="second_arg", help="the second argument",
                    type="string")
                                        # you can force the argument to be of a certain 
                                        # type by using type="string" (or "int" or "float"), etc.
(options, args) = parser.parse_args() 
 
 
if not (options.first_arg and options.second_arg): 
    parser.error("You need to supply an argument for -s")
# if you want to require one or more of your arguments, you can add an if
# statement that raises an error if a required argumnt is missing
 
 
print "The first argument is '{}'.".format(options.first_arg)
print "The second argument is '{}'.".format(options.second_arg)