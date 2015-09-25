from flask import Flask, request, redirect, make_response, render_template
from subprocess import check_output
app = Flask(__name__, static_folder="public_html/static")
import pprint
import shelve

# Creating a database for our server. This way even if our server shuts down 
# we dcan save information
demo_db = shelve.open("demo_db.db")

# Demo in class: POST
@app.route('/demo/wiki', methods=["POST", "PUT"])
def load_demo_post():

	post_id = request.form.get("id")
	post_title = request.form.get("title")
	demo_db[post_id] = post_title
	
	return render_template("wiki_post.html", id=post_id, title=post_title)

# Demo in class: GET
@app.route('/demo/wiki', methods=["GET"])
def load_demo_get():

	all_data = pprint.pformat(demo_db)
	return render_template("wiki_get.html", data=all_data)

###############################################################

# HW 5 content

# Creating database to store redirect
redirect_db = shelve.open("redirect.db")

# When you type http://127.0.0.1:5000/home in your browser, this
# piece of code is run
@app.route('/home', methods=["GET"])
def load_home():
	name = request.args.get('name', 'This should say your name')
	return render_template("home.html", name=name)

# When you type http://127.0.0.1:5000/school in your browser, this
# piece of code is run
@app.route('/redirect', methods=["GET", "POST", "PUT"])
def load_redirect():
	global redirect_path

	if request.method == "GET":
		return redirect(redirect_db["location"], code=302)
	else: # If the method is either POST or PUT
		# Change the redirect path to the parameter named "name"
		redirect_db["location"] = request.form.get('location', "http://ischool.berkeley.edu").strip() # Remove newline at end of telnet requests
		
		return render_template("redirect.html", location=redirect_db["location"])

# When you type http://127.0.0.1:5000/image in your browser, this
# piece of code is run
@app.route('/image')
def image():
	"""Returns an image"""

	in_file = open("public_html/static/logo_home", "rb")
	data = in_file.read()
	in_file.close()

	resp = make_response(data);
	# Comment in to set header below
	#resp.headers['Content-Type'] = ""

	return resp

if __name__ == "__main__":
	app.run(debug=True)