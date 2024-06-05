import mysql.connector

# 定義 GetMessageHandler 類，用於從 MySQL 數據庫中獲取留言
class GetMessageHandler:
    def get_message(self, link):
        # MySQL 配置
        mysql_config = {
            'host': '140.115.126.110',
            'port': 3306,
            'user': 'root',
            'password': 'ncu1234',
            'database': 'ptt'  # 請確保已經在 MySQL 中創建了這個資料庫
        }

        # 連接 MySQL 數據庫
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        cursor.execute('SELECT 網址, 內容 FROM 留言')
        rows = cursor.fetchall()

        message = ''

        # 匹配指定連結的留言內容
        for row in rows: 
            if row[0] == link[0]:
                message += row[1]

        conn.close()

        return message
