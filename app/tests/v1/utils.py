class Utils(object):
    def __init__(self):
        pass
    
    ADMIN = {
        'firstname': 'Donald',
        'lastname': 'Duck',
        'othername': 'quack',
        'email': 'admin@app.com',
        'phone_number': '+254726094972',
        'username': 'Kingpin',
        'password': 'password',
        'admin': 'true'
    }

    USER = {
        'firstname': 'Luda',
        'lastname': 'one',
        'othername': 'quack',
        'email': 'user@app.com',
        'phone_number': '+254726094972',
        'username': 'Kingpin',
        'password': 'password',
        'admin': 'false'
    }

    def register_user(self, client, user_type):
        if user_type == 'admin':
            client.post('api/v1/auth/user/register', json=self.ADMIN)
        else:
            client.post('api/v1/auth/user/register', json=self.USER)
        
    def login_user(self, client, user_type):
        if user_type == 'admin':
            data = {
                'email': self.ADMIN['email'],
                'password': self.ADMIN['password']
            }
            client.post('api/v1/auth/user/login', json=data)
        else:
            data = {
                'email': self.USER['email'],
                'password': self.USER['password'],
            }
            client.post('api/v1/auth/user/login', json=data)
