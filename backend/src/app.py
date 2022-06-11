from flask import Flask
import sys
sys.path.insert(0, './utils')
from authenticate import authenticateUser
from database import checkIfUserPresent
from misc import validateUserData
app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    user = request.get_json(force=True)
    if(!checkIfUserPresent(user)):
        return {error: "User already exists", status: 400}
    validateUserData(user)
    return 200

app.run(host='0.0.0.0',port=8080)