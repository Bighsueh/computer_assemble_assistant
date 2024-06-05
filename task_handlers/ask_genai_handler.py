# 引入基本任務處理器類
from .task_handler import TaskHandler
import textwrap
from gpt_api import call_gpt

# 定義處理詢問 GenAI 的處理器類
class AskGenAIHandler(TaskHandler):
    def handle(self, task, user_input, frame, agenda):
        # 如果當前任務是 ask_genai，處理用戶輸入
        if task == 'ask_genai':
            content, message, query = user_input
            greeting = '你是一個電腦組裝的助理，了解電腦零件、品牌等相關知識。'
            greeting += '以下有一個連結網頁的文章以及文章下的網友留言。'
            greeting += '請根據閱讀網頁的文章(CONTENT)及留言(MESSAGE)後，提供一個電腦組裝的菜單。'
            greeting += '這些菜單應符合使用者的電腦組裝需求(QUERY)，例如用途、偏好品牌、預算等。'
            greeting += '請盡量以年份較近的產品優先。'
            greeting += '零件包括CPU、主機板、記憶體、顯示卡、散熱器、固態硬碟(SSD)、硬碟(HDD)、電源供應器以及機殼。'

            notice = '接下來請你仔細看注意事項。'
            notice += '提供菜單時請條列式並正確換行，只要包含廠牌以及型號等資訊。'
            notice += '你還需要提供最後的總價。'
            notice += '請以json格式表示最後的結果。'
            notice += "格式為: [{'cpu': ''}, {'主機板': ''}, {'記憶體': ''}, {'顯示卡': ''}, {'散熱器': ''}, {'固態硬碟(SSD)': ''}, {'硬碟(HDD)': ''}, {'電源供應器': ''}, {'機殼': ''}, {'總價': ''}]"

            prompt = textwrap.dedent("""  
                '{greeting}'                  
                QUERY: '{query}'
                CONTENT: '{content}'
                MESSAGE: '{message}'
                '{notice}'                             
                """).format(greeting=greeting, query=query, content=content, message=message, notice=notice)

            answer = call_gpt(prompt)
            
            frame.component_menu = answer
            return answer
        else:
            # 否則，傳遞給下一個處理器
            return super().handle(task, user_input, frame, agenda)
