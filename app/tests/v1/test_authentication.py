def test_user_register(client):
    user = {
        'firstname': 'Luke',
        'lastname': 'Nzang\'u',
        'othername': 'Kanga',
        'email': 'lukey@app.com',
        'phone_number': '+254726094972',
        'username': 'Kingpin',
        'password': 'password',
        'admin': 'false'
    }
    response = client.post('api/v1/auth/user/register', json=user)
    assert response.status_code == 201

def register_user(client):
    user = {
        'firstname': 'Luke',
        'lastname': 'Nzang\'u',
        'othername': 'Kanga',
        'email': 'lukey@app.com',
        'phone_number': '+254726094972',
        'username': 'Kingpin',
        'password': 'password',
        'admin': 'true'
    }
    client.post('api/v1/auth/user/register', json=user)

def test_user_login(client):
    register_user(client)
    user = {
        'email': 'lukey@app.com',
        'password': 'password'
    }
    response = client.post('api/v1/auth/user/login', json=user)
    assert response.status_code == 200