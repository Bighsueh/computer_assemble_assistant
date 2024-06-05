# 引入基本任務處理器類
from .task_handler import TaskHandler
from gpt_api import call_gpt

# 定義處理最後檢查的處理器類
class LastCheckHandler(TaskHandler):
    def handle(self, task, user_input, frame, agenda):
        # 如果當前任務是 last_check，處理用戶輸入
        if task == 'last_check':           
            # 構建提示信息
            prompt = f"""請依照判斷電腦零組件推薦清單是否滿足下方列示之條件，若條件皆滿足則回傳電腦推薦清單，若不滿足則說明未達條件的原因。
            條件：
            1. 電腦零組件清單必須滿足使用者需求
            2. 若使用者需求中未提及則不需要列入判斷條件中
            
            使用者需求：
            {frame.requirement_list}
            
            電腦零組件清單：
            {frame.component_menu}
            """
            print(prompt)
            
            answer = call_gpt(prompt)
            
            print(answer)
            return answer
        else:
            # 否則，傳遞給下一個處理器
            return super().handle(task, user_input, frame, agenda)
