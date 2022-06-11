from flask import Flask
import sys
sys.path.insert(0, './utils')
from authenticate import authenticateUser
app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register(user):
    user = request.get_json(force=True)
    authenticateUser(user)
    return 200

app.run(host='0.0.0.0',port=8080)