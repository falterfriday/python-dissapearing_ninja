from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<name>')
def show_user_profile(name):
	if name != 'blue' and name != 'red' and name != 'purple' and name != 'orange' and name != 'ninja':
		name = 'dead'
	return render_template("index.html", name=name)
app.run(debug=True)