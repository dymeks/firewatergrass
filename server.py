from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Some-Secret-Key-Goes-Here'

@app.route('/') #This is the root
def index():
	if not ('win' in session):
		session['win'] = 0
		print "session win", session['win']
	if not ('loss' in session):
		session['loss'] = 0
		print "session loss", session['loss']
	if not ('tie' in session):
		session['tie'] = 0	
		print "session tie", session['tie']	

	return render_template('index.html')

@app.route('/rolltype', methods=['POST'])
def rolltype():
	types = ['fire', 'water','grass']
	typegiven = str(request.form['type'])
	serverType = types[random.randint(0,2)]
	messages = {'win':'This was a Win! Yeah!' ,'loss':'This was a Loss Boo!!', 'tie': 'This was a tie, meh.'}
	message = "error"
	print serverType
	if typegiven == serverType:
		session['tie']+=1
		message = str(messages['tie'])
	if typegiven == 'fire' and serverType == 'grass':
		session['win']+=1
		message = str(messages['win'])
	if typegiven == 'water' and serverType == 'fire':
		session['win']+=1
		message = str(messages['win'])
	if typegiven == 'grass' and serverType == 'water':
		session['win']+=1
		message = str(messages['win'])
	if typegiven == 'fire' and serverType == 'water':
		session['loss']+=1
		message = str(messages['loss'])
	if typegiven == 'water' and serverType == 'grass':
		session['loss']+=1
		message = str(messages['loss'])
	if typegiven == 'grass' and serverType == 'fire':
		session['loss']+=1
		message = str(messages['loss'])
	return render_template('index.html', win = session['win'], loss = session['loss'], tie = session['tie'], message = message)

app.run(debug=True)