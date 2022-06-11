from flask import Flask, request
from utils.authenticate import authenticateUser
from utils.database import checkIfUserPresent, insertUser
from utils.misc import validateUserData
app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome"

@app.route('/register', methods=['POST'])
def register():
    try:
        user = request.get_json(force=True)
        resp = validateUserData(user)
        if resp is not None:
            return {'error': resp, 'status': 400}
        if checkIfUserPresent(user):
            return {'error': "User already exists", 'status': 400}
        insertUser(user)
        return {'message': 'User Registered', 'status': 200}
    except Exception as e:
        print("Error", e)
        return {'error':"Internal Server Error", 'status': 500}

app.run(host='localhost',port=8080)