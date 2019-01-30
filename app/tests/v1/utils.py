import datetime

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

    MEETUPS = [
        {
            'topic': 'Meet of the year',
            'location': 'The I-hub',
            'happeningOn': datetime.datetime.today() - datetime.timedelta(days=2),
            'tags': ['tech', 'gaming'],
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
        },
        {
            'topic': 'Hottest Meet',
            'location': 'KICC',
            'happeningOn': datetime.datetime.now() - datetime.timedelta(days=4),
            'tags': ['outdoors', 'gaming'],
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
        },
        {
            'topic': 'Workshop',
            'location': 'Kasarani',
            'happeningOn': datetime.datetime.now() - datetime.timedelta(days=5),
            'tags': ['tech', 'gaming'],
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
        },
        {
            'topic': 'Arts Gala',
            'location': 'The I-hub',
            'happeningOn': datetime.datetime.now() + datetime.timedelta(days=2),
            'tags': ['graphics', 'art'],
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
        },
        {
            'topic': 'Painters Haven',
            'location': 'Ruai mall',
            'happeningOn': datetime.datetime.now() + datetime.timedelta(days=5),
            'tags': ['tech', 'gaming'],
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
        }
    ]

    def create_meetups(self, client, headers):
        for meetup in self.MEETUPS:
            client.post('api/v1/meetups', json=meetup, headers=headers)
    
    def create_meetup(self, client, meetup, headers):
        client.post('api/v1/meetups', json=meetup, headers=headers)

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
            return client.post('api/v1/auth/user/login', json=data)
        else:
            data = {
                'email': self.USER['email'],
                'password': self.USER['password'],
            }
            return client.post('api/v1/auth/user/login', json=data)
