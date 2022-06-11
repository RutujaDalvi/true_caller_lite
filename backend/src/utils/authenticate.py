from utils.database import validate_user

def authenticate_user(user):
    # connect to data base
    return validate_user(user)