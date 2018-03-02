#blog.py controller

#imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
    
#configuration
DATABASE = "blog.db"
USERNAME = "admin"
PASSWORD = "admin"
SECRET_KEY = "hard_to_guess"

app = Flask(__name__)

#pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

#function used for connecting to the database
def connect_db ():
	return sqlite3.connect(app.config["DATABASE"])
	
@app.route("/", methods = ["GET","POST"])
def login():
	error = none
	status_code = 200
	if request.method == "POST":
		if request.form["username"] != app.config["USERNAME"] or \
		        request.form["password"] != app.config["PASSWORD"]:
			error = "Invalid Credentials. Please try again."
			status_code = 401
		else:
			session["logged_in"] = True
			return redirect(url_for("main"))
	return render_template("login.html", error=error), status_code
	
@app.route("/main")
def main():
	return render_template("main.html")
	
@app.route("/logout")
def log_out():
	session.pop("logged in", None)
	flash("You were logged out")
	return redirect_url(url_for("login"))

if __name__ == "__main__":
	app.run(debug = True)
