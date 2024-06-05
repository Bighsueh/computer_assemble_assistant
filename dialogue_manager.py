from frame import Frame
from agenda import Agenda
from task_handlers.ask_name_handler import AskNameHandler
from task_handlers.ask_age_handler import AskAgeHandler
from task_handlers.confirm_info_handler import ConfirmInfoHandler

class DialogueManager:
    def __init__(self):
        self.frame = Frame()
        self.agenda = Agenda()
        self.agenda.add_task('ask_name')
        self.agenda.add_task('ask_age')
        self.agenda.add_task('confirm_info')

        # Create the chain of handlers
        self.handler_chain = AskNameHandler()
        self.handler_chain.set_next(AskAgeHandler()).set_next(ConfirmInfoHandler())

    def handle_input(self, user_input):
        current_task = self.agenda.get_next_task()
        return self.handler_chain.handle(current_task, user_input, self.frame, self.agenda)

# Example interaction
if __name__ == "__main__":
    dialogue_manager = DialogueManager()

    # Simulating user interaction
    inputs = ["Alice", "30", "yes"]
    for user_input in inputs:
        response = dialogue_manager.handle_input(user_input)
        print(f"User: {user_input}")
        print(f"Bot: {response}\n")
