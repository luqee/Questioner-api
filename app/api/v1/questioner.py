import datetime
from app.api.v1 import models

class QuestionerApp(object):
    def __init__(self):
        self.registered_users = []
        self.online_users = []
        self.meetups = []
    
    def get_user(self, email):
        for user in self.registered_users:
            if user.email == email:
                return user
        return 'Not found'

    def get_online_user(self, user_id):
        for user in self.online_users:
            if user.id == user_id:
                return user
        return 'Not found'
    
    def register_user(self, new_user):
        # check if user exists
        if self.get_user(new_user.email) == 'Not found':
            # Add user as they don't exist
            new_user.id = len(self.registered_users) + 1
            self.registered_users.append(new_user)
            return 'User added'
        else:
            return "User already exists"
    
    def login_user(self, email, password):
        user = self.get_user(email)
        if user == 'Not found':
            return 'Invalid credentials'
        elif isinstance(user, models.user.User):
            if user.password == password:
                #put user in online users list
                self.online_users.append(user)
                # Generate the access token. This will be used as the authorization header
                access_token = user.generate_token()
                return access_token
            else:
                return 'Invalid credentials'
        
    def create_meetup(self, meetup, user_id):
        user = self.get_online_user(user_id)
        if user == 'Not found':
            return 'Login needed'
        elif isinstance(user, models.user.User):
            # user is logged in
            meetup.user_id = user.id
            meetup.id = len(self.meetups) + 1
            meetup.created_on = datetime.datetime.now()
            self.meetups.append(meetup)
            return 'Meetup created'

    def fetch_meetup(self, meetup_id):
        for meetup in self.meetups:
            if meetup.id == meetup_id:
                return meetup
        return 'Not found'
    
    def fetch_upcoming_meetups(self):
        result = []
        for meetup in self.meetups:
            if datetime.datetime.strptime(meetup.happening_on, '%a, %d %b %Y %H:%M:%S %Z') > datetime.datetime.today():
                result.append(meetup)
        return result
    
    def post_question(self, question, meetup_id, user_id):
        for meetup in self.meetups:
            if meetup.id == meetup_id:
                # have found meetup
                question.meetup = meetup_id
                question.created_by = user_id
                question.created_on = datetime.datetime.now()
                question.id = len(meetup.questions) + 1
                meetup.questions.append(question)
                return  question
        return 'Meetup not found'
    
    def upvote(self, meetup_id, question_id):
        meetup = self.fetch_meetup(meetup_id)
        if isinstance(meetup, models.meetup.Meetup):
            for q in meetup.questions:
                if q.id == question_id:
                    #vote on question
                    q.votes += 1
                    return q
            return 'Question not found'
        elif meetup == 'Not found':
            return 'Meetup not found'
    
    def downvote(self, meetup_id, question_id):
        meetup = self.fetch_meetup(meetup_id)
        if isinstance(meetup, models.meetup.Meetup):
            for q in meetup.questions:
                if q.id == question_id:
                    #vote on question
                    q.votes -= 1
                    return q
            return 'Question not found'
        elif meetup == 'Not found':
            return 'Meetup not found'
    
    def rsvp_to_meetup(self, rsvp_item, meetup_id, user_id):
        for meetup in self.meetups:
            if meetup.id == meetup_id:
                rsvp_item.meetup = meetup_id
                rsvp_item.user = user_id
                rsvp_item.id = len(meetup.rsvps) + 1
                meetup.rsvps.append(rsvp_item)
                return rsvp_item, meetup
        return 'no such meetup'
