from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
    return 'Hello world!'

@app.route('/')
def index():
    return 'Hello world!'

app.run(app.run(host='0.0.0.0', port=5000))