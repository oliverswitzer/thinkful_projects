import re
import sys
import os


directory = sys.argv[1]   #user specifies the path to the directory with the text files that need to be
						  #searched for information

 #current path on my computer: /Users/oliverswitzer/Programming/Python/thinkful_projects/document_tagger/part2/texts

#************* For Matching Document Info ***************

# PREPARE OUR REGEXES FOR METADATA SEARCHES #
# we'll use re.compile() here, which allows you to assign a regex pattern
# to a variable. We'll do this for each our metadata fields.
# 
# Also note how we're using paretheses to create two search groups. Looking
# at title_search, see how we use one group to match on the presence of "title:".
# 
# Also, note how in the second group is a named group -- we use ?p<name> .
# 
# Finally, note that we're passing the re.IGNORECASE flag as an optional
# argument to re.compile. We're doing this because it's human beings who create
# the metadata headers at the top of Project gutenberg docs, and we want to account 
# for possibility of "title: Some Title", "Title: Some Title", and "TITLE: Some Title").

title_search = re.compile(r'(title:\s*)(?P<title>.*(\n\s{2}.*)*)', re.IGNORECASE)  #(\n\s{2}.*)* allows regex to match multiple lines for title
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)



#************* For Keyword Search ***************

# first we need to do something with the user supplied keywords
# which we're getting with sys.argv. Remember, the script name itself
# is at index 0 in sys.argv, so we'll slice everything from index 1 forward. Here we slice from 2 forward
#because index 1 is used for the user-supplied directory path. 

searches = {}

for kw in sys.argv[2:]:
	searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

#************* For loop to return doc info AND keyword info in each iteration ***************

# now iterate over the documents and extract and print output about metadata
# for each one. Note the use of enumerate here, which gives you a counter variable
# (in this case 'i') that keeps track of the index of the list (in this case documents)
# your currently on in your loop. You should memorize how enumerate works, and google it
# if you need more explanation. It's a highly productive built in function, and there are
# common problems that you'll encounter as a programmer that enumerate is great for.

for i, fl in enumerate(os.listdir(directory)):   #not sure if enumerate was entirely necessary here, but I used it anyway
												 #because it was used in the original parsing script.

	if fl.endswith(".txt"):     #we're only interested in the text files in this directory
		
		fl_path = os.path.join(directory, fl)    #joining the user-specified path with the file name

		with open(fl_path, 'r') as f:         #open the file as f for reading
	            full_text = f.read()  			

		title = re.search(title_search, full_text).group('title')	#using compiled regex to search for 
		author = re.search(author_search, full_text).group('author')				#title, author translator and illustrator in each doc
		translator = re.search(translator_search, full_text).group('translator')		#that is iterated over
		illustrator = re.search(illustrator_search, full_text).group('illustrator')

		if author:        #if there is a match for author, set the value author equal to the matched value in the group
			author = author.group('author')
		if translator:
			translator = translator.group('translator')
		if illustrator:
			illustrator = illustrator.group('illustrator')

		print "***" * 25
		print "Here's the info for doc '{}':".format(fl)
		print "Title:  {}".format(title)
		print "Author(s): {}".format(author)
		print "Translator(s): {}".format(translator)
		print "Illustrator(s): {}".format(illustrator)
		print """

		"""
		print "Here's the keyword count info for doc '{}':".format(fl)
		for search in searches: 	# for each keyword in the dictionary searches
			print "\"{0}\": {1}".format(search, len(re.findall(searches[search], full_text))) #print "keyword:#of occurences"
		print "\n"
