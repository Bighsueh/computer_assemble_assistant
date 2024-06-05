from sentence_transformers import SentenceTransformer

# 定義 SentenceTransformerHandler 類，用於處理句子編碼
class SentenceTransformerHandler:
    def __init__(self, model_name):
        # 初始化 SentenceTransformer 模型
        self.model = SentenceTransformer(model_name)

    def encode(self, text):
        # 使用模型編碼給定文本
        return self.model.encode(text)
