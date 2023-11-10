from .closeSystem import CloseSystemSkill


class Skills:
    def __init__(self):
        self.skills = [
            CloseSystemSkill()
        ]

    def handle(self, message):
        for skill in self.skills:
            return skill.handle(message)
