class User(object):
    def __init__(self, firstname, lastname, username, email, othername, phone_number, password, is_admin):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.othername = othername
        self.phoneNumber = phone_number
        self.password = password
        self.is_admin = is_admin
