from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello, DevOps!"


@app.route('/about')
def about():
	return "This is a test app."
