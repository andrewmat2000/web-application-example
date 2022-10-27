from flask import Flask
import socket

host = socket.gethostbyname("python_service")

app = Flask(__name__)

@app.route('/get_secret/')
def GetSecret():
    return 'python'

app.run(debug=False, host=host, port=80)