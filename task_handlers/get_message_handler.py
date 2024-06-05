# 引入基本任務處理器類
from .task_handler import TaskHandler
import mysql.connector

# 定義處理獲取消息的處理器類
class GetMessageHandler(TaskHandler):
    def handle(self, task, user_input, frame, agenda):
        # 如果當前任務是 get_message，處理用戶輸入
        if task == 'get_message':
            link = user_input
            mysql_config = {
                'host': '140.115.126.110',
                'port': 3306,
                'user': 'root',
                'password': 'ncu1234',
                'database': 'ptt'  # 請確保已經在 MySQL 中創建了這個資料庫
            }

            conn = mysql.connector.connect(**mysql_config)
            cursor = conn.cursor()
            cursor.execute('SELECT 網址, 內容 FROM 留言')
            rows = cursor.fetchall()

            message = ''

            for row in rows:
                if row[0] == link[0]:
                    message += row[1]

            conn.close()

            return message
        else:
            # 否則，傳遞給下一個處理器
            return super().handle(task, user_input, frame, agenda)
