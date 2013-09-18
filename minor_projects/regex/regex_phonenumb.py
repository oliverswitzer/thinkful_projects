import re


phonePattern1 = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')  #search for a number with format:
														  #(347)-(555)-(1089)
 
s1 = phonePattern1.search('800-555-1212')

s2 = phonePattern1.search('800-555-1212').groups()  	  #returns each number group in a tuple:
														  #>>>(800, 555, 1212)

phonePattern2 = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')  #now search for a number with an 
																#extension

s3 = phonePattern2.search('800-555-1212-1234').groups()

#s4 = phonePattern2.search('800-555-1212').groups() #oops, now we cant parse phone numbers WITHOUT an 												 	 #extension because the extension wasnt optional

phonePattern3 = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')  #the \D means any non-digit. + means 1 or more

s5 = phonePattern3.search('800 555 1212 1234').groups()  #can now search for numbers 
														 #with no dashes in between them
s6 = phonePattern3.search('800-555 1212 1234').groups()  #can print with or without dashes

phonePattern4 = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')  #using *, we can now search phone numbers that 
																	  #have no spaces between them. * means
																	  #0 or more. Also, our regex string now allows their to be 
																	  #no extension with the * substituted for the + after
																	  #\d.

s7 = phonePattern4.search('8005559874').groups()

s8 = phonePattern4.search('800.555.1212 x1234').groups()  			  # our regex search can now handle non-space/non dash 
																	  # seperators. 

phonePattern5 = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')  #Now the regex string can handle searching 
																		  # a leading non-digit (e.g. "+" or "(")

s9 = phonePattern5.search('(800)5551212 ext. 1234').groups() #( before 800 at the beginning now searchable


phonePattern6 = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')  #if we had a +1 before the number in the old regex,
																	 #it wouldn't recognize it and would return none becuase 
																	 #we had a non-digit recognizer, \D*. If we remove the 
																	 #^ indicating the beginning of the string, we can let the regex
																	 # do the work of finding where the string begins (e.g. with the group 
																	 # recognizer indicators "(" and ")")

s10 = phonePattern6.search('work 1-(800) 555.1212 #1234').groups() 



print s1
print s2
print s3
#print s4
print s5
print s6
print s7
print s8
print s9
print s10

the verbose expression

phonePattern7 = re.compile(r'''

                # don't match beginning of string with carrot, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
''', re.VERBOSE)



#print s4