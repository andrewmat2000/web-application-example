from flask import Flask

print ("Hi there")

app = Flask(__name__)

@app.route('/get_secret/')
def GetSecret():
    return 'python'

app.run(debug=False, host='0.0.0.0', port=80)