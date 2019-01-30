from flask import request, abort, g
from functools import wraps
from app.api.v1.models import user
from app import questioner_app

def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Get the access token from the header
        auth_header = request.headers.get('Authorization')
        access_token = auth_header.split(" ")[1]
        if access_token:
            # Attempt to decode the token and get the User ID
            user_id = user.User.decode_token(access_token)
            print(user_id)
            if not isinstance(user_id, str):
                # Go ahead and handle the request, the user is authenticated
                current_user = questioner_app.get_user_by_id(user_id)
                g.user = current_user
                return f(*args, **kwargs)       
            else:
                abort(401)
    return wrapper