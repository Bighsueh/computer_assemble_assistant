from dialogue_manager import DialogueManager
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

if __name__ == "__main__":
    # 初始化對話管理器
    chat = DialogueManager()
    requirement_list = chat.chat()
    print(requirement_list)

    # 初始化 Pinecone 和嵌入模型
    pc = Pinecone(
        api_key='17b40179-a748-4043-a0bb-678205f52116',
        environment='gcp-starter'
    )

    index_name = 'menu'
    index = pc.Index(index_name)
    embedding_model = SentenceTransformer('thenlper/gte-large-zh')

    # 讀取需求
    purpose, brand, price = chat.handle_input(None, 'read_input')

    query = 'purpose: ' + ', '.join(purpose) + ', prefer brand: ' + ', '.join(brand) + ', budget: ' + ', '.join(price)
    embed_query = embedding_model.encode(purpose)
    max_query_result_vectors = 50

    # 查詢 Pinecone
    matches = index.query(
        vector=embed_query.tolist(),
        top_k=max_query_result_vectors,
        include_values=False,
        filter={}
    )

    retrival_data = []
    document_vectors = []

    for item in matches['matches']:
        result = index.fetch([item['id']])
        retrival_data.append(result['vectors'][item['id']]['metadata'])
        document_vectors.append(result['vectors'][item['id']]['values'])

    final_data = retrival_data[0]
    final_len = len(final_data)

    link = [final_data['url']]
    content = final_data['title'] + final_data['purpose'] + final_data['menu'] + final_data['price'] + final_data['time']

    message = chat.handle_input(link, 'get_message')

    # 存儲組裝的電腦零組件清單
    chat.frame.component_menu = chat.handle_input((content, message, query), 'ask_genai')
    
    # 最後檢查
    final_check_result = chat.handle_input(None, 'last_check')
    print(final_check_result)
