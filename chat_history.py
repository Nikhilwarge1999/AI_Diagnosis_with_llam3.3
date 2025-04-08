class ChatHistory:
    def __init__(self):
        self.history = []

    def add_user_message(self, content):
        self.history.append(("user", content))

    def add_bot_message(self, content):
        self.history.append(("assistant", content))

    def get_all(self):
        return self.history
