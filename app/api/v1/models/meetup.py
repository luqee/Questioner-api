class Meetup(object):
    def __init__(self, topic, location, happeningOn, description):
        self.topic = topic
        self.location = location
        self.happening_on = happeningOn
        self.tags = []
        self.description = description
        self.questions = []
        self.rsvps = []

class Tag(object):
    def __init__(self, name):
        self.name = name
