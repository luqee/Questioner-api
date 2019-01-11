from flask import Blueprint, request, jsonify
from app.api.v1.models import meetup, rsvp
from app import questioner_app

meetup_blueprint = Blueprint('meetup', __name__, url_prefix='/api/v1')

@meetup_blueprint.route('/meetups', methods=['POST'])
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
            'error': 'An error occurred while creating meetup'
        }
        return jsonify(response), 400

@meetup_blueprint.route('/meetups/<int:meetup_id>', methods=['GET'])
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
            'error': 'No such meetup'
        }
        return jsonify(response), 404

@meetup_blueprint.route('/meetups/upcoming/', methods=['GET'])
def fetch_upcoming_meetups():
    result = questioner_app.fetch_upcoming_meetups()
    if result == []:
        response = {
            'status': 200,
            'data':[]
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 200,
            'data':[]
        }
        for meet in result:
            meetup = {
                'id': meet.id,
                'topic': meet.topic,
                'location': meet.location,
                'happeningOn': meet.happening_on,
                'tags': []
            }
            response['data'].append(meetup)
        return jsonify(response), 200

@meetup_blueprint.route('/meetups/<int:meetup_id>/rsvps', methods=['POST'])
def rsvp_meetup(meetup_id):
    data = request.get_json()
    response = data['response']
    rsvp_item = rsvp.Rsvp(response)
    result = questioner_app.rsvp_to_meetup(rsvp_item, meetup_id, 1)
    if isinstance(result, tuple):
        response = {
            'status': 200,
            'data':[]
        }
        going = {
            'meetup': result[0].meetup,
            'status': result[0].response,
            'topic': result[1].topic
        }
        response['data'].append(going)
        return jsonify(response), 200
    else:
        response = {
            'status': 400,
            'error': 'Could not rsvp.'
        }
        return jsonify(response), 400