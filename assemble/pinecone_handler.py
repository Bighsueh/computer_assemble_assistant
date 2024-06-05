from pinecone import Pinecone

# 定義 PineconeHandler 類，用於處理 Pinecone 初始化和索引操作
class PineconeHandler:
    def __init__(self, api_key, environment):
        # 初始化 Pinecone 並設定 API 金鑰和環境
        self.pc = Pinecone(api_key=api_key, environment=environment)

    def get_index(self, index_name):
        # 獲取指定名稱的索引
        return self.pc.Index(index_name)
