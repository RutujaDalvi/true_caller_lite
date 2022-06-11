from flask import Flask
import sys
sys.path.insert(0, './utils')
from authenticate import authenticateUser
app = Flask(__name__)

@app.route('/register')
def register(user):
    authenticateUser(user)
    if(!)

app.run(host='0.0.0.0',port=8080)