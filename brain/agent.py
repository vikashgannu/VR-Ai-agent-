from brain.commands import CommandProcessor
from memory.memory import Memory

class VRAIAgent:
    def __init__(self):
        self.processor = CommandProcessor()
        self.memory = Memory()

    def run(self, command):
        self.memory.save(command)

        result = self.processor.process(command)

        print("Task :", result["task"])
        print("History :", self.memory.show())
