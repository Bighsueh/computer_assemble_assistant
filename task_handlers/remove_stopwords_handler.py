# 引入基本任務處理器類
from .task_handler import TaskHandler

# 定義處理刪除停用詞的處理器類
class RemoveStopwordsHandler(TaskHandler):
    def handle(self, task, user_input, frame, agenda):
        # 如果當前任務是 remove_stopwords，處理用戶輸入
        if task == 'remove_stopwords':
            stopwords = ['是', '的', '了']  # 示例停用詞
            for stopword in stopwords:
                user_input = user_input.replace(stopword, "")
            return user_input
        else:
            # 否則，傳遞給下一個處理器
            return super().handle(task, user_input, frame, agenda)
