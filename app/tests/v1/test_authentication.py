from app.tests.v1 import utils

test_utils = utils.Utils()

def test_user_register(client):
    response = client.post('api/v1/auth/user/register', json=test_utils.USER)
    assert response.status_code == 201

def test_user_login(client):
    test_utils.register_user(client, 'user')
    data = {
        'email': test_utils.USER['email'],
        'password': test_utils.USER['password']
    }
    response = client.post('api/v1/auth/user/login', json=data)
    assert response.status_code == 200