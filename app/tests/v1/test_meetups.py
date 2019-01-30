import datetime
from app.tests.v1 import utils

test_utils = utils.Utils()

def test_meetup_creation(client):
    test_utils.register_user(client, 'admin')
    login_res = test_utils.login_user(client, 'admin')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    response = client.post('api/v1/meetups', json=test_utils.MEETUPS[0], headers=headers)
    assert response.status_code == 201

def test_fetch_specific_meetup(client):
    test_utils.register_user(client, 'admin')
    login_res = test_utils.login_user(client, 'admin')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    test_utils.create_meetup(client, test_utils.MEETUPS[0], headers)
    response = client.get('api/v1/meetups/1')
    assert response.status_code == 200

def test_fetch_upcoming_meetups(client):
    test_utils.register_user(client, 'admin')
    login_res = test_utils.login_user(client, 'admin')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    test_utils.create_meetups(client, headers)
    response = client.get('api/v1/meetups/upcoming/')
    assert response.status_code == 200

def test_rsvp_to_meetup(client):
    test_utils.register_user(client, 'admin')
    login_res = test_utils.login_user(client, 'admin')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    test_utils.create_meetup(client, test_utils.MEETUPS[0], headers=headers)

    test_utils.register_user(client, 'user')
    login_res = test_utils.login_user(client, 'user')
    headers = {
        'Authorization': 'Bearer {0}'.format(login_res.get_json()['data'][0]['auth_token'])
    }
    data ={
        'response': 'Maybe'
    }
    response = client.post('api/v1/meetups/1/rsvps', json=data, headers=headers)
    assert response.status_code == 200