import datetime
from app.tests.v1 import utils

test_utils = utils.Utils()

def test_meetup_creation(client):
    test_utils.register_user(client, 'admin')
    test_utils.login_user(client, 'admin')
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
    test_utils.register_user(client, 'admin')
    test_utils.login_user(client, 'admin')
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
    test_utils.register_user(client, 'admin')
    test_utils.login_user(client, 'admin')
    create_meetups(client)
    response = client.get('api/v1/meetups/upcoming/')
    assert response.status_code == 200

def test_rsvp_to_meetup(client):
    test_utils.register_user(client, 'admin')
    test_utils.login_user(client, 'admin')
    create_meetup(client)
    data ={
        'response': 'Maybe'
    }
    response = client.post('api/v1/meetups/1/rsvps', json=data)
    assert response.status_code == 200