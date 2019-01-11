def register_admin(client):
    user = {
        'firstname': 'Donald',
        'lastname': 'Duck',
        'othername': 'quack',
        'email': 'duck@app.com',
        'phone_number': '+254726094972',
        'username': 'Kingpin',
        'password': 'password',
        'admin': 'true'
    }
    client.post('api/v1/auth/user/register', json=user)
def login_admin(client):
    user = {
        'email': 'duck@app.com',
        'password': 'password',
    }
    client.post('api/v1/auth/user/login', json=user)

def test_meetup_creation(client):
    register_admin(client)
    login_admin(client)
    meetup = {
        'topic': 'Meet of the year',
        'location': 'The I-hub',
        'happeningOn': '13th August 2019',
        'tags': ['tech', 'gaming'],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
    }
    response = client.post('api/v1/meetups', json=meetup)
    assert response.status_code == 201