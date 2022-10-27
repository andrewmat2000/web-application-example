from flask import Flask
app = Flask(__name__)

@app.route('/get_secret/')
def hello_world():
    return 'python'
