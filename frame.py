# 定義 Frame 類，用於存儲對話狀態信息
class Frame:
    def __init__(self):
        self.chat_history = []
        self.requirement_list = {
            "主要用途": [],
            "品牌偏好": [],
            "預算範圍": [],
            "其他需求": []
        }
        self.requirement_list_key = list(self.requirement_list.keys())
        self.component_menu = ""

    def fill_slot(self, slot, value):
        # 填充指定的槽位
        self.requirement_list[slot].append(value)

    def get_slot(self, slot):
        # 獲取指定槽位的值
        return self.requirement_list.get(slot, None)

    def is_filled(self):
        # 檢查所有槽位是否都已填充
        return all(self.requirement_list[slot] for slot in self.requirement_list_key)
