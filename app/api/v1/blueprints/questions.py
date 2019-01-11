from flask import Blueprint, request, jsonify
from app.api.v1.models import question
from app import questioner_app

questions_blueprint = Blueprint('question', __name__, url_prefix='/api/v1')

@questions_blueprint.route('/meetups/<int:meetup_id>/questions', methods=['POST'])
def post_question(meetup_id):
    data = request.get_json()
    title = data['title']
    body = data['body']

    new_question = question.Question(title, body)
    result = questioner_app.post_question(new_question, meetup_id, 1)
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
def upvote(meetup_id, question_id):
    res = questioner_app.upvote(meetup_id, question_id)
    if isinstance(res, question.Question):
        response = {
            'status': 201,
            'data':[]
        }
        data = {
            'user': res.created_by,
            'meetup': res.meetup,
            'title': res.title,
            'body': res.body
        }
        response['data'].append(data)
        return jsonify(response), 201
    else:
        response = {
            'status': 400,
            'error': 'something went wrong'
        }
        return jsonify(response), 400

@questions_blueprint.route('/meetups/<int:meetup_id>/questions/<int:question_id>/downvote', methods=['PATCH'])
def downvote(meetup_id, question_id):
    res = questioner_app.downvote(meetup_id, question_id)
    if isinstance(res, question.Question):
        response = {
            'status': 201,
            'data':[]
        }
        data = {
            'user': res.created_by,
            'meetup': res.meetup,
            'title': res.title,
            'body': res.body
        }
        response['data'].append(data)
        return jsonify(response), 201
    else:
        response = {
            'status': 400,
            'error': 'something went wrong'
        }
        return jsonify(response), 400