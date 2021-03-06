from flask import current_app as app
from datetime import datetime, timedelta
import jwt

class User(object):
    def __init__(self, **kwargs):
        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.othername = kwargs.get('othername')
        self.phoneNumber = kwargs.get('phone_number')
        self.password = kwargs.get('password')
        self.is_admin = kwargs.get('is_admin')

    def generate_token(self):
        """ Generates the access token"""

        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=5),
                'iat': datetime.utcnow(),
                'sub': self.id
            }
            # create the byte string token using the payload and the SECRET key
            jwt_string = jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
            print(jwt_string)
            print(type(jwt_string))
            return jwt_string

        except Exception as e:
            # return an error in string format if an exception occurs
            print('Something bad')
            return str(e)

    @staticmethod
    def decode_token(token):
        """Decodes the access token from the Authorization header."""
        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, app.config.get('SECRET_KEY'), algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return "Invalid token. Please register or login"
