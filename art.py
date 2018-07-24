from flask import Flask, render_template , request
from random import randint

app=Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/draw')
def draw():
	return render_template('drawingAnimation.html')



if __name__=='__main__':
	app.run(port=6006, debug=True)