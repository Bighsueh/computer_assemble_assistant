from frame import Frame

# 定義 ReadInputHandler 類，用於讀取使用者輸入需求
class ReadInputHandler:
    def read_input(self):
        purpose = []
        brand = []
        price = []

        # 獲取需求列表
        row = Frame().requirement_list

        # 將需求添加到對應的列表中
        purpose.append(row['主要用途'])
        brand.append(row['品牌偏好'])
        price.append(row['預算範圍'])

        return purpose, brand, price
