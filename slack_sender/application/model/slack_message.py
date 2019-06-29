class SlackMessage:
    def __init__(self, message):
        self.unfurl_links = True
        self.message = message
        self.channel = ""
        self.icon = ""
        self.user_name = ""

    def is_empty(self):
        return self.message is None or len(self.message) == 0
