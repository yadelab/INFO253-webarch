from flask import Flask, request, redirect, make_response
from subprocess import check_output
app = Flask(__name__, static_folder="public_html/static")
import pprint

# Demo in class: dictionary that holds variables we store
demo_dict = dict()

# Demo in class: POST
@app.route('/demo/wiki', methods=["POST", "PUT"])
def load_demo_post():

	post_id = request.form.get("id")
	post_title = request.form.get("title")
	demo_dict[post_id] = post_title
	
	content = '''
	<html>
		<head>
			<title>Demo for class today</title>
		</head>
		<body>
			<h1>Stored wiki entry: ''' + post_id + ''' => ''' + post_title + '''</h1>
		</body>
	</html>'''
	return content, 200

# Demo in class: GET
@app.route('/demo/wiki', methods=["GET"])
def load_demo_get():
		
	content = '''
	<html>
		<head>
			<title>Demo for class today</title>
		</head>
		<body>
			<pre>''' + pprint.pformat(demo_dict) + '''</pre>
		</body>
	</html>'''
	return content, 200

###############################################################

# HW 5 content

# Variable that holds current redirect path
redirect_path = "http://ischool.berkeley.edu"

# When you type http://127.0.0.1:5000/home in your browser, this
# piece of code is run
@app.route('/home', methods=["GET"])
def load_home():
	content = '''
<html>
	<head>
		<title>INFO 253: Web Architecture</title>
	</head>
	<body>
		<h1>''' + request.args.get('name') + '''</h1>
	</body>
</html>'''

	return content, 200

# When you type http://127.0.0.1:5000/school in your browser, this
# piece of code is run
@app.route('/redirect', methods=["GET", "POST", "PUT"])
def load_redirect():
	global redirect_path


	if request.method == "GET":
		return redirect(redirect_path, code=302)
	else: # If the method is either POST or PUT
		
		# Change the redirect path to the parameter named "name"
		redirect_path = request.form.get('location').strip()
		
		content = '''
	<html>
		<head>
			<title>Redirect path changed</title>
		</head>
		<body>
			<h1>/redirect now points to: ''' + request.form.get('location') + '''</h1>
		</body>
	</html>'''
	return content, 200

# When you type http://127.0.0.1:5000/image in your browser, this
# piece of code is run
@app.route('/image')
def image():
	"""Returns a PNG image"""

	in_file = open("public_html/static/logo_home", "rb")
	data = in_file.read()
	in_file.close()

	resp = make_response(data);
	# Comment in to set header below
	#resp.headers['Content-Type'] = ""

	return resp

if __name__ == "__main__":
	app.run(debug=True)