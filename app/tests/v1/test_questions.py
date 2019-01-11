import datetime
admin = {
    'firstname': 'Donald',
    'lastname': 'Duck',
    'othername': 'quack',
    'email': 'admin@app.com',
    'phone_number': '+254726094972',
    'username': 'Kingpin',
    'password': 'password',
    'admin': 'true'
}

user = {
    'firstname': 'Luda',
    'lastname': 'one',
    'othername': 'quack',
    'email': 'user@app.com',
    'phone_number': '+254726094972',
    'username': 'Kingpin',
    'password': 'password',
    'admin': 'false'
}
def register_user(client, user_type):
    if user_type == 'admin':
        client.post('api/v1/auth/user/register', json=admin)
    else:
        client.post('api/v1/auth/user/register', json=user)
    
def login_user(client, user_type):
    if user_type == 'admin':
        data = {
            'email': admin['email'],
            'password': admin['password']
        }
        client.post('api/v1/auth/user/login', json=data)
    else:
        data = {
            'email': user['email'],
            'password': user['password'],
        }
        client.post('api/v1/auth/user/login', json=data)

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
    register_user(client, 'admin')
    login_user(client, 'admin')
    create_meetup(client)
    question = {
        'title': 'design',
        'body': 'Why is it so difficult to do web design?'
    }
    response = client.post('api/v1/meetups/1/questions', json=question)
    assert response.status_code == 201

def test_upvote_question(client):
    register_user(client, 'user')
    login_user(client, 'user')
    create_meetup(client)
    question = {
        'title': 'design',
        'body': 'Why is it so difficult to do web design?'
    }
    client.post('api/v1/meetups/1/questions', json=question)
    response = client.patch('api/v1/meetups/1/questions/1/upvote')

    assert response.status_code == 201

def test_downvote_question(client):
    register_user(client, 'user')
    login_user(client, 'user')
    create_meetup(client)
    question = {
        'title': 'design',
        'body': 'Why is it so difficult to do web design?'
    }
    client.post('api/v1/meetups/1/questions', json=question)

    response = client.patch('api/v1/meetups/1/questions/1/downvote')

    assert response.status_code == 201