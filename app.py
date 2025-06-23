from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello, Devops!"


@app.route('/about')
def about():
	return "This is a test app."
