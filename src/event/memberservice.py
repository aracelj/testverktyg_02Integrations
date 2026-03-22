class MemberService:
    def __init__(self):
        self.members = []

    def add_member(self, name):
        self.members.append(name)
        return f"{name} added"