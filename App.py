from brain.agent import VRAIAgent

def main():
    print("=== VR AI Agent ===")
    agent = VRAIAgent()

    while True:
        command = input("You> ")

        if command.lower() == "exit":
            print("Bye!")
            break

        agent.run(command)

if __name__ == "__main__":
    main()
