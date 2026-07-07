class Brain:
    def __init__(self):
        self.name = "VR AI Agent"

    def start(self):
        print(f"{self.name} Brain Started!")

    def think(self, command):
        print(f"Command Received: {command}")


brain = Brain()
brain.start()
brain.think("Create 3 motivational YouTube Shorts")
