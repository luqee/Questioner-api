class User(object):
    def __init__(self, **kwargs):
        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.othername = kwargs.get('othername')
        self.phoneNumber = kwargs.get('phone_number')
        self.password = kwargs.get('password')
        self.is_admin = kwargs.get('is_admin')
