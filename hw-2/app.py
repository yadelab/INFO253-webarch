from flask import Flask
app = Flask(__name__)

@app.route('/')
def load_root():
    f = open('public_html/index.html', 'r')
    raw_data = f.read()
    return raw_data

@app.route('/<path:name>')
def load_file(name=None):
    f = open('public_html/' + name, 'r')
    raw_data = f.read()
    return raw_data

if __name__ == "__main__":
    app.run()