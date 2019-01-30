import datetime
from app.tests.v1 import utils

test_utils = utils.Utils()

def test_post_meetup_question(client):
    test_utils.register_user(client, 'admin')
    login_res = test_utils.login_user(client, 'admin')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    test_utils.create_meetup(client, test_utils.MEETUPS[0], headers)

    test_utils.register_user(client, 'user')
    login_res = test_utils.login_user(client, 'user')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    question = {
        'title': 'design',
        'body': 'Why is it so difficult to do web design?'
    }
    response = client.post('api/v1/meetups/1/questions', json=question, headers=headers)
    assert response.status_code == 201

def test_upvote_question(client):
    test_utils.register_user(client, 'admin')
    login_res = test_utils.login_user(client, 'admin')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    test_utils.create_meetup(client, test_utils.MEETUPS[0], headers)

    test_utils.register_user(client, 'user')
    login_res = test_utils.login_user(client, 'user')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    question = {
        'title': 'design',
        'body': 'Why is it so difficult to do web design?'
    }
    client.post('api/v1/meetups/1/questions', json=question, headers=headers)
    response = client.patch('api/v1/meetups/1/questions/1/upvote', headers=headers)

    assert response.status_code == 201

def test_downvote_question(client):
    test_utils.register_user(client, 'admin')
    login_res = test_utils.login_user(client, 'admin')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    test_utils.create_meetup(client, test_utils.MEETUPS[0], headers)
    
    test_utils.register_user(client, 'user')
    login_res = test_utils.login_user(client, 'user')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    question = {
        'title': 'design',
        'body': 'Why is it so difficult to do web design?'
    }
    client.post('api/v1/meetups/1/questions', json=question, headers=headers)
    response = client.patch('api/v1/meetups/1/questions/1/downvote', headers=headers)

    assert response.status_code == 201
    assert response.status_code == 201