# 引入基本任務處理器類
from .task_handler import TaskHandler
from frame import Frame

# 定義處理讀取輸入的處理器類
class ReadInputHandler(TaskHandler):
    def handle(self, task, user_input, frame, agenda):
        # 如果當前任務是 read_input，處理用戶輸入
        if task == 'read_input':
            purpose = []
            brand = []
            price = []

            row = frame.requirement_list

            purpose.append(''.join(row["主要用途"]) + ''.join(row["其他需求"]))
            brand.append(''.join(row["品牌偏好"]))
            price.append(''.join(row["預算範圍"]))

            return purpose, brand, price
        else:
            # 否則，傳遞給下一個處理器
            return super().handle(task, user_input, frame, agenda)
