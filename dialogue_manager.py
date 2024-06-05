# 引入 Frame 和 Agenda 類
from frame import Frame
from agenda import Agenda
# 引入具體任務處理器
from task_handlers.chat_history_control_handler import ChatHistoryControlHandler
from task_handlers.remove_stopwords_handler import RemoveStopwordsHandler
from task_handlers.requirement_classification_handler import RequirementClassificationHandler

from gpt_api import call_gpt

class DialogueManager:
    def __init__(self):
        self.frame = Frame()
        self.agenda = Agenda()
        # 初始化任務列表
        self.agenda.add_task('requirement_classification')
        self.agenda.add_task('chat_history_control')
        self.agenda.add_task('remove_stopwords')

        # 創建任務處理器鏈
        self.handler_chain = RequirementClassificationHandler()
        self.handler_chain.set_next(ChatHistoryControlHandler()).set_next(RemoveStopwordsHandler())

    def handle_input(self, user_input):
        # 獲取當前任務，並通過處理器鏈處理用戶輸入
        current_task = self.agenda.get_next_task()
        return self.handler_chain.handle(current_task, user_input, self.frame, self.agenda)

    def chat(self):
        # 初始系統提示
        system_prompt = """
        請使用者提供組裝電腦的需求，例如他們的使用目的、預算等相關事項。
        回覆限制:
        1.使用繁體中文。
        2.不要和使用者道歉。
        """
        reply = call_gpt(system_prompt)
        self.frame.chat_history.append(f"System: '{reply}'")
        print(reply)

        while True:
            # 使用者回覆
            response = input('Input your message: \n')
            self.frame.chat_history.append(f"User: '{response}'")
            print("\nChatBot:")

            # 需求分類
            self.handle_input(response)

            # 檢查是否完成
            if self.frame.is_filled():
                break

            # 繼續對話
            system_prompt = "請繼續提供其他需求。"
            reply = call_gpt(system_prompt)
            self.frame.chat_history.append(f"System: '{reply}'")
            print(reply)

        return self.frame.requirement_list

if __name__ == "__main__":
    chat = DialogueManager()
    requirement_list = chat.chat()
    print(requirement_list)
