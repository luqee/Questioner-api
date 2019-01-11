from flask import Flask
from instance.config import app_config
from app.api.v1.questioner import QuestionerApp

questioner_app = QuestionerApp()

def create_app(config_name):
    app = Flask('__name__')
    app.config.from_object(app_config[config_name])

    from app.api.v1.blueprints import auth, meetups
    app.register_blueprint(auth.auth_blue_print)
    app.register_blueprint(meetups.meetup_blue_print)
    
    return app