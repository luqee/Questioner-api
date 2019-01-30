from flask import Blueprint, request, jsonify, g
from app.api.v1.models import question
from app import questioner_app
from app.api.v1.blueprints.decorators import authenticate

questions_blueprint = Blueprint('question', __name__, url_prefix='/api/v1')

@questions_blueprint.route('/meetups/<int:meetup_id>/questions', methods=['POST'])
@authenticate
def post_question(meetup_id):
    data = request.get_json()
    title = data['title']
    body = data['body']

    new_question = question.Question(title, body)
    result = questioner_app.post_question(new_question, meetup_id, g.user)
    if isinstance(result, question.Question):
        response = {
            'status': 201,
            'data':[]
        }
        data = {
            'user': result.created_by,
            'meetup': result.meetup,
            'title': result.title,
            'body': result.body
        }
        response['data'].append(data)
        return jsonify(response), 201
    elif result == 'meetup not found':
        response = {
            'status': 400,
            'error': 'The meetup does not exist'
        }
        return jsonify(response), 400

@questions_blueprint.route('/meetups/<int:meetup_id>/questions/<int:question_id>/upvote', methods=['PATCH'])
@authenticate
def upvote(meetup_id, question_id):
    res = questioner_app.upvote(meetup_id, question_id, g.user)
    return return_voting__results(res)

@questions_blueprint.route('/meetups/<int:meetup_id>/questions/<int:question_id>/downvote', methods=['PATCH'])
@authenticate
def downvote(meetup_id, question_id):
    res = questioner_app.downvote(meetup_id, question_id, g.user)
    return return_voting__results(res)
    
def return_voting__results(res):
    if isinstance(res, question.Question):
        response = {
            'status': 201,
            'data':[]
        }
        data = {
            'meetup': res.meetup,
            'title': res.title,
            'body': res.body,
            'votes': res.votes
        }
        response['data'].append(data)
        return jsonify(response), 201
    else:
        response = {
            'status': 400,
            'error': 'something went wrong'
        }
        return jsonify(response), 400