from utils.database import validateUser

def authenticateUser(user):
    # connect to data base
    return validateUser(user)