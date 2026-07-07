from brain.commands import CommandProcessor
from memory.memory import Memory
from tasks.task_manager import TaskManager

class VRAIAgent:

    def __init__(self):

        self.processor = CommandProcessor()
        self.memory = Memory()
        self.task = TaskManager()

    def run(self, command):

        self.memory.save(command)

        result = self.processor.process(command)

        self.task.execute(result["task"])

        print("History :", self.memory.show())
