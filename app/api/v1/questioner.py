import datetime

class QuestionerApp(object):
    def __init__(self):
        self.registered_users = []
        self.online_users = []
        self.meetups = []
    
    def register_user(self, new_user):
        # check if user exists
        for user in self.registered_users:
            if user.email == new_user.email:
                return "user already exists"
        # Add user as they don't exist
        new_user.id = len(self.registered_users) + 1
        self.registered_users.append(new_user)
        return 'user added'
    
    def login_user(self, email, password):
        for user in self.registered_users:
            if user.email == email:
                if user.password == password:
                    #put user in online users list
                    self.online_users.append(user)
                    return 'login success'
        return 'error'
    
    def create_meetup(self, meetup, user_id):
        for user in self.online_users:
            if user.id == user_id:
                # user is logged in
                meetup.user_id = user.id
                meetup.id = len(self.meetups) + 1
                meetup.created_on = datetime.datetime.now()
                self.meetups.append(meetup)
                return 'meetup created'
        return 'error'

    def fetch_meetup(self, meetup_id):
        for meetup in self.meetups:
            if meetup.id == meetup_id:
                return meetup
        return 'error'
    
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
        return 'meetup not found'
    
    def upvote(self, meetup_id, question_id):
        for meetup in self.meetups:
            if meetup.id == meetup_id:
                for q in meetup.questions:
                    if q.id == question_id:
                        #vote on question
                        q.votes += 1
                        return q
                return 'question not found'
        return 'meetup not found'
    
    def downvote(self, meetup_id, question_id):
        for meetup in self.meetups:
            if meetup.id == meetup_id:
                for q in meetup.questions:
                    if q.id == question_id:
                        #vote on question
                        q.votes -= 1
                        return q
                return 'question not found'
        return 'meetup not found'
    
