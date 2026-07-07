from brain.commands import CommandProcessor

class VRAIAgent:
    def __init__(self):
        self.processor = CommandProcessor()

    def run(self, command):
        result = self.processor.process(command)
        print("Task:", result["task"])
