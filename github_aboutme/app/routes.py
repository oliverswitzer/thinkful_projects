from flask import Flask, render_template
import os
from random import choice


app = Flask(__name__)

@app.route("/")
def home():
	return render_template('about.html')

@app.route("/cats")
def cats():
	randgif_list = []  #init a list that will be filled with path's to gifs of cats 
	directory = "static/img/catgifs"  #specify the directory to look for these gifs

	for i, fl in enumerate(os.listdir(directory)): #for each file in the listed directory
		if fl.endswith(".gif"):    #if file is a .gif
			randgif_list.append(fl)  #add this gif to the list randgif_list

	cat_gif = choice(randgif_list)   #select random gif from list using choice function imported from random
	
	return render_template('catgifpage.html', catgif = cat_gif)

if __name__ == '__main__':
	app.run(debug='True')