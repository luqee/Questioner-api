from flask import Blueprint, request, jsonify
from app.api.v1.models import user
from app.api.v1.questioner import QuestionerApp

auth_blue_print = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
questioner_app = QuestionerApp()

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
    

    new_user = user.User(firstname, lastname, username, email, othername, phone_number, password)
    if questioner_app.register_user(new_user) == 'user added':
        # return a response notifying the user that they registered successfully
        response = {
            'status': 201,
            'data':[{'message': 'user registered successfully'}]
        }
        return jsonify(response), 201
    elif questioner_app.register_user(new_user) == 'user already exists':
        # notify the user that an account with the same email is already registered
        response = {
            'status': 200,
            'data':[{'message': 'user already exists'}]
        }
        return jsonify(response), 200
