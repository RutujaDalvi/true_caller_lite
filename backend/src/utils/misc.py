def validateUserData(user):
    if not 'name' in user:
        return 'Name required'
    if not 'phoneNumber' in user:
        return 'Phone Number required'
    if not 'password' in user:
        return 'password required'
    return None