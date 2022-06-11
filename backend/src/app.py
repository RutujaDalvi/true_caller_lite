from flask import Flask, request
from utils.authenticate import authenticate_user
from utils.database import check_if_user_present, insert_user
from utils.misc import validate_user_data
app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome"

@app.route('/register', methods=['POST'])
def register():
    try:
        user = request.get_json(force=True)
        resp = validate_user(user)
        if resp is not None:
            return {'error': resp, 'status': 400}
        if check_if_user_present(user):
            return {'error': "User already exists", 'status': 400}
        insert_user(user)
        return {'message': 'User Registered', 'status': 200}
    except Exception as e:
        print("Error", e)
        return {'error':"Internal Server Error", 'status': 500}

app.run(host='localhost',port=8080)