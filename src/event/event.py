class Event:
    def __init__(self):
        self.members = []
        self.event_log = []

    def sign_up(self, name):
        self.members.append(name)

    def register_new_member(self, name):
        self.sign_up(name)
        self.write_event(f"{name} was registered as a new member")
        return f"{name} successfully registered"

    def write_event(self, msg):
        self.event_log.append(msg)





