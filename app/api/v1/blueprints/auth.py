from flask import Blueprint, request, jsonify
from app.api.v1.models import user
from app import questioner_app

auth_blue_print = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth_blue_print.route('/user/register', methods=['POST'])
def register():
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']
    username = data['username']
    email = data['email']
    othername = data['othername']
    phone_number = data['phone_number']
    password = data['password']
    admin = data['admin']
    

    new_user = user.User(firstname, lastname, username, email, othername, phone_number, password, admin)
    result = questioner_app.register_user(new_user)
    if result == 'user added':
        # return a response notifying the user that they registered successfully
        response = {
            'status': 201,
            'data':[{'message': 'user registered successfully'}]
        }
        return jsonify(response), 201
    elif result == 'user already exists':
        # notify the user that an account with the same email is already registered
        response = {
            'status': 200,
            'data':[{'message': 'user already exists'}]
        }
        return jsonify(response), 200

@auth_blue_print.route('/user/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    result = questioner_app.login_user(email, password)
    if result == 'login success':
        # return a response notifying the user that they logged in successfully
        response = {
            'status': 200,
            'data':[{'message': 'successfull log in'}]
        }
        return jsonify(response), 200
    elif result == 'error':
        # notify the user that there was an error.
        response = {
            'status': 200,
            'data':[{'message': 'error logging in'}]
        }
        return jsonify(response), 200