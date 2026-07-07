class TaskManager:

    def execute(self, task):

        if task == "create_video":
            print("Creating YouTube Video...")

        elif task == "upload_video":
            print("Uploading to YouTube...")

        else:
            print("Unknown Task")
