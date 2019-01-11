import datetime
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
        'happeningOn': datetime.datetime.now() - datetime.timedelta(days=2),
        'tags': ['tech', 'gaming'],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
    }
    response = client.post('api/v1/meetups', json=meetup)
    assert response.status_code == 201
def create_meetup(client):
    meetup = {
        'topic': 'Meet of the year',
        'location': 'The I-hub',
        'happeningOn': datetime.datetime.now() - datetime.timedelta(days=2),
        'tags': ['tech', 'gaming'],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
    }
    client.post('api/v1/meetups', json=meetup)

def test_fetch_specific_meetup(client):
    register_admin(client)
    login_admin(client)
    create_meetup(client)
    response = client.get('api/v1/meetups/1')
    assert response.status_code == 200

def create_meetups(client):
    meetup1 = {
        'topic': 'Meet of the year',
        'location': 'The I-hub',
        'happeningOn': datetime.datetime.today() - datetime.timedelta(days=2),
        'tags': ['tech', 'gaming'],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
    }
    client.post('api/v1/meetups', json=meetup1)
    meetup2 = {
        'topic': 'Meet of the year',
        'location': 'The I-hub',
        'happeningOn': datetime.datetime.now() - datetime.timedelta(days=4),
        'tags': ['tech', 'gaming'],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
    }
    client.post('api/v1/meetups', json=meetup2)
    meetup3 = {
        'topic': 'Meet of the year',
        'location': 'The I-hub',
        'happeningOn': datetime.datetime.now() - datetime.timedelta(days=5),
        'tags': ['tech', 'gaming'],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
    }
    client.post('api/v1/meetups', json=meetup3)
    meetup4 = {
        'topic': 'Meet of the year',
        'location': 'The I-hub',
        'happeningOn': datetime.datetime.now() + datetime.timedelta(days=2),
        'tags': ['tech', 'gaming'],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
    }
    client.post('api/v1/meetups', json=meetup4)
    meetup5 = {
        'topic': 'Meet of the year',
        'location': 'The I-hub',
        'happeningOn': datetime.datetime.now() + datetime.timedelta(days=5),
        'tags': ['tech', 'gaming'],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
    }
    client.post('api/v1/meetups', json=meetup5)

def test_fetch_upcoming_meetups(client):
    register_admin(client)
    login_admin(client)
    create_meetups(client)
    response = client.get('api/v1/meetups/upcoming/')
    assert response.status_code == 200

def test_rsvp_to_meetup(client):
    register_admin(client)
    login_admin(client)
    create_meetup(client)
    response = client.post('api/v1/meetups/1/rsvps')
    assert response.status_code == 200