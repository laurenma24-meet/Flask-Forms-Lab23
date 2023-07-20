from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "lauren"
password = "123"
facebook_friends=["Ola","Khaled","Avigail", "George", "Fouad", "Ali"]

  
#@app.route('/home')
#def go_home():
	#return redirect(url_for('home',facebookfriend = facebook_friends))




@app.route('/',methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		un=request.form['username']
		passwrd=request.form['password']
		if un==username and passwrd==password :
			return render_template('home.html',list=facebook_friends)
		else : 
			return render_template('login.html')
	else :
		return render_template('login.html')


@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/friend_exists/<string>:name')
def friend_exists(name):
	name1=""
	for name in facebook_friends:
		if name1="true":
	return render_template("friend_exists.html", name2=name1)
else:
	if name1="false":
	return render_template("friend_exists.html", name2=name1)




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
