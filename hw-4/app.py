from flask import Flask, redirect
app = Flask(__name__, static_folder="public_html/static")

@app.route('/home')
def load_home():
	content = "<html><head></head><body><h1>HOME</h1></body></html>"
	return content, 200

if __name__ == "__main__":
	app.run()