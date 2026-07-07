class Memory:
    def __init__(self):
        self.history = []

    def save(self, command):
        self.history.append(command)

    def show(self):
        return self.history
