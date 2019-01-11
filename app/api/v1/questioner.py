class QuestionerApp(object):
    def __init__(self):
        self.registered_users = []
        self.online_users = []
        self.meetups = []
    
    def register_user(self, new_user):
        if len(self.registered_users) == 0:
            new_user.id = 1
            self.registered_users.append(new_user)
            return 'user added'
        else:
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
                self.meetups.append(meetup)
                return 'meetup created'
        return 'error'

    def fetch_meetup(self, meetup_id):
        for meetup in self.meetups:
            if meetup.id == meetup_id:
                return meetup
        return 'error'
    # def get_user(self, email):
    #     # check if user exists
    #     for user in self.registered_users:
    #         if user.email == email:
    #             return user
    #     return 'user does not exist'
    
    
