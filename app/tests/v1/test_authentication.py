def test_user_register(client):
    user = {
        'firstname': 'Luke',
        'lastname': 'Nzang\'u',
        'othername': 'Kanga',
        'email': 'lukey@app.com',
        'phone_number': '+254726094972',
        'username': 'Kingpin',
        'password': 'password'
    }
    response = client.post('api/v1/auth/user/register', json=user)
    assert response.status_code == 201
