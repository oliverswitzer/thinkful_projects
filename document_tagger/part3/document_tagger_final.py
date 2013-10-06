
import re
import sys
import os

title_search = re.compile(r'(title:\s*)(?P<title>.*(\n\s{2}.*)*)', re.IGNORECASE)  #(\n\s{2}.*)* allows regex to match multiple lines for title
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

pattern_dict = dict(title=title_search,
				   author=author_search,
				   translator=translator_search,
				   illustrator=illustrator_search)

def metadata_search(pattern_dict, text):
	"""returns results for metadata search in text"""
	
	results = {}
	for k in pattern_dict:
		result = re.search(pattern_dict[k], text)
		if result:
			results[k] = result.group(k)
		else:
			results[k] = None
	
	return results

def path_creator(directory, fl):
	return os.path.join(directory, fl)  

def file_reader(fl_path):
	with open(fl_path, 'r') as f:         #open the file as f for reading
		full_text = f.read()
	return full_text

def compile_searches(kws):
	"""Returns ditionary of keyword regular expression patterns"""
	result = {kw: re.compile(r'\b' + kw + r'\b') for kw in kws}
	return result

def keyword_count(pattern, text):
    """Returns the number of matches for a keyword in a given text"""
    matches = re.findall(pattern, text)
    return len(matches)

def main_func(path, keywords):

	for fl in os.listdir(path):
		if fl.endswith(".txt"):
			fl_path = path_creator(path, fl)
			text = file_reader(fl_path)
			metad_searches = metadata_search(pattern_dict, text)
			kw_patterns = compile_searches(keywords)
			
			print "Here's the info for {}:".format(fl)
			
			for k in metad_searches:
				print "{0}: {1}".format(k.capitalize(), metad_searches[k])

			print "\n\nKEYWORDS\n\n"

			for kw in kw_patterns:
				key_count = keyword_count(kw, text)
				print "{0}:{1}".format(kw, key_count)

			print "***"*25

def main():
	path = sys.argv[1]
	keywords = sys.argv[2:]
	main_func(path, keywords)

if __name__ == '__main__':
	main()
