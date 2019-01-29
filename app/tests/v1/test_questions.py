import datetime
from app.tests.v1 import utils

test_utils = utils.Utils()

def create_meetup(client):
    meetup = {
        'topic': 'Meet of the year',
        'location': 'The I-hub',
        'happeningOn': datetime.datetime.now() + datetime.timedelta(days=2),
        'tags': ['tech', 'gaming'],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitatio'
    }
    client.post('api/v1/meetups', json=meetup)

def test_post_meetup_question(client):
    test_utils.register_user(client, 'admin')
    test_utils.login_user(client, 'admin')
    create_meetup(client)
    question = {
        'title': 'design',
        'body': 'Why is it so difficult to do web design?'
    }
    response = client.post('api/v1/meetups/1/questions', json=question)
    assert response.status_code == 201

def test_upvote_question(client):
    test_utils.register_user(client, 'user')
    test_utils.login_user(client, 'user')
    create_meetup(client)
    question = {
        'title': 'design',
        'body': 'Why is it so difficult to do web design?'
    }
    client.post('api/v1/meetups/1/questions', json=question)
    response = client.patch('api/v1/meetups/1/questions/1/upvote')

    assert response.status_code == 201

def test_downvote_question(client):
    test_utils.register_user(client, 'user')
    test_utils.login_user(client, 'user')
    create_meetup(client)
    question = {
        'title': 'design',
        'body': 'Why is it so difficult to do web design?'
    }
    client.post('api/v1/meetups/1/questions', json=question)

    response = client.patch('api/v1/meetups/1/questions/1/downvote')

    assert response.status_code == 201