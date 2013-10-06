from flask import Flask, render_template
import os
from random import choice

randgif_list = []
directory = "static/img/catgifs"

for i, fl in enumerate(os.listdir(directory)): 
	if fl.endswith(".gif"):    
		fl_path = os.path.join(directory, fl)    
	randgif_list.append(fl_path)



cat_gif = choice(randgif_list)   
usable_url = "url_for('static', filename='{}')".format(cat_gif[7:]) #from 7 onwards to get rid of the "static" directory, as this 
										 #is specified in the url_for function with jinja
# print usable_url	
print cat_gif[19:]
