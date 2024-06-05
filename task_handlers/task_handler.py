# 定義一個基本的任務處理器類，用於處理任務和設置下一個處理器
class TaskHandler:
    def set_next(self, handler):
        # 設置下一個處理器
        self.next_handler = handler
        return handler

    def handle(self, task, user_input, frame, agenda):
        # 如果當前處理器無法處理任務，將任務傳遞給下一個處理器
        if self.next_handler:
            return self.next_handler.handle(task, user_input, frame, agenda)
        return "我不明白。"
