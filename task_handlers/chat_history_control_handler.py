# 引入基本任務處理器類
from .task_handler import TaskHandler

# 定義處理聊天歷史記錄控制的處理器類
class ChatHistoryControlHandler(TaskHandler):
    def handle(self, task, user_input, frame, agenda):
        # 如果當前任務是 chat_history_control，處理用戶輸入
        if task == 'chat_history_control':
            max_length = 15
            current_length = len(frame.chat_history)
            if current_length > max_length:
                excess_count = current_length - max_length
                frame.chat_history = frame.chat_history[excess_count:]
            return "聊天歷史已更新。"
        else:
            # 否則，傳遞給下一個處理器
            return super().handle(task, user_input, frame, agenda)
