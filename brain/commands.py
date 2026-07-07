class CommandProcessor:
    def process(self, command):
        command = command.lower()

        if "short" in command or "video" in command:
            return {
                "task": "create_video",
                "count": 1
            }

        if "upload" in command:
            return {
                "task": "upload_video"
            }

        return {
            "task": "unknown"
        }
