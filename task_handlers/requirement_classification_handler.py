# 引入基本任務處理器類
from .task_handler import TaskHandler
from gpt_api import call_gpt

# 定義處理需求分類的處理器類
class RequirementClassificationHandler(TaskHandler):
    def handle(self, task, user_input, frame, agenda):
        # 如果當前任務是 requirement_classification，處理用戶輸入
        if task == 'requirement_classification':
            for item in frame.requirement_list_key:
                system_prompt = f"""
                你是一位電腦組裝助理，將協助使用者整理電腦組裝需求。請根據使用者所提供的問題以及答覆，並基於參考資訊的說明，整理出一筆有關{item}的資訊，如果使用者提供的需求不包含相關資訊，則回覆'無'。
                參考資訊:
                "主要用途": 打算如何使用這台電腦？例如，是用來遊戲、工作、學習或是多媒體娛樂？
                "品牌偏好": 是否有特定的品牌偏好？如果使用者表示沒有品牌偏好則填寫'沒有'。
                "預算範圍": 預算大約在多少範圍內？
                "其他需求": 如電腦外觀造型、優惠折扣、運行音量大小等其他需求。如果使用者表示沒有其他需求則填寫'沒有'。
                
                回覆限制:
                1.請按照以下格式回覆:'your content'
                2.只能整理出一筆資訊。
                3.不能加入引導詞或提示詞。
                4.不能回覆問句。
                5.使用繁體中文或英文。
                6.不能回覆多餘內容。
                """
                user_prompt = f"問題:{system_prompt} 答覆:{user_input}"
                reply = call_gpt(system_prompt, user_prompt)
                frame.requirement_list[item].append(reply)
            return "Requirement classified."
        else:
            # 否則，傳遞給下一個處理器
            return super().handle(task, user_input, frame, agenda)
