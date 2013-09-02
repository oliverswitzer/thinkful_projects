
import re
import sys
import os


def path_creator(directory, fl):
	return os.path.join(directory, fl)  

def file_reader(fl_path):
	with open(fl_path, 'r') as f:         #open the file as f for reading
        full_text = f.read()

def compile_searches(keywords):
	for kw in keywords:
		searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
	return searches

def keyword_count(pattern, text):
    """Returns the number of matches for a keyword in a given text"""
    matches = re.findall(pattern, text)
    return len(matches)

def main_func(path, keywords):
	title_search = re.compile(r'(title:\s*)(?P<title>.*(\n\s{2}.*)*)', re.IGNORECASE)  #(\n\s{2}.*)* allows regex to match multiple lines for title
	author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
	translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
	illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

	for fl in path:
		if fl.endswith(."txt"):
			fl_path = path_creator(path, fl)
			text = file_reader(fl_path)
			


def main():
