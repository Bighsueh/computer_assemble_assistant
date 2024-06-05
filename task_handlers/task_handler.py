class TaskHandler:
    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, task, user_input, frame, agenda):
        if self.next_handler:
            return self.next_handler.handle(task, user_input, frame, agenda)
        return "I don't understand."