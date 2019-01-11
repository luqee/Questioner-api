from flask import Blueprint, request, jsonify
from app.api.v1.models import user, meetup
from app import questioner_app

meetup_blue_print = Blueprint('meetup', __name__, url_prefix='/api/v1')

@meetup_blue_print.route('/meetups', methods=['POST'])
def create_meetup():
    data = request.get_json()
    topic = data['topic']
    location = data['location']
    happeningOn = data['happeningOn']
    tags = data['tags']
    description = data['description']

    new_meetup = meetup.Meetup(topic, location, happeningOn, description)
    for t in tags:
        tag = meetup.Tag(t)
        new_meetup.tags.append(tag)
    
    result = questioner_app.create_meetup(new_meetup,1)
    if result == 'meetup created':
        response = {
            'status': 201,
            'data':[{'message': 'Meetup record created successfully.'}]
        }
        return jsonify(response), 201
    elif result == 'error':
        response = {
            'status': 400,
            'data':[{'message': 'An error occurred while creating meetup'}]
        }
        return jsonify(response), 400

@meetup_blue_print.route('/meetups/<int:meetup_id>', methods=['GET'])
def fetch_meetup(meetup_id):
    result = questioner_app.fetch_meetup(meetup_id)
    if isinstance(result, meetup.Meetup):
        response = {
            'status': 200,
            'data':[]
        }
        meet = {
            'id': result.id,
            'topic': result.topic,
            'location': result.location,
            'happeningOn': result.happening_on,
            'tags': []
        }
        for tag in result.tags:
            meet['tags'].append(tag.name)
        
        response['data'].append(meet)
        return jsonify(response), 200
    else:
        response = {
            'status': 404,
            'data':[{'error': 'No such meetup'}]
        }
        return jsonify(response), 404
