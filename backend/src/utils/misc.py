def validateUserData(user):
    if (user.name !='' and user.password !='' and user.phoneNumber != ''):
        return True
    return False