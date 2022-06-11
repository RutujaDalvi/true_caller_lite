def check_if_user_present(user):
    whereClause = "where phone_number="+user.phoneNumber+";"
    return None

def validate_user(user):
    phoneNumber = user.phoneNumber
    whereClause = "where phone_number="+user.phoneNumber+";"
    # check for this phone number in database
    response = {}
    if user.password == response.password:
        return True
    else:
        return False

def insert_user(user):
    return True