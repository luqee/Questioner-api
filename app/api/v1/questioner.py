class QuestionerApp(object):
    def __init__(self):
        self.registered_users = []
    
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
    
    def get_user(self, email):
        # check if user exists
        for user in self.registered_users:
            if user.email == email:
                return user
        return 'user does not exist'