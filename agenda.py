# 定義 Agenda 類，用於管理對話任務
class Agenda:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # 添加新任務到任務列表
        self.tasks.append(task)

    def get_next_task(self):
        # 獲取並移除下一個任務
        return self.tasks.pop(0) if self.tasks else None
