from brain.agent import VRAIAgent

print("=================================")
print("      VR AI Agent v1.0")
print("=================================")

agent = VRAIAgent()

while True:
    command = input("You: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    agent.run(command)
