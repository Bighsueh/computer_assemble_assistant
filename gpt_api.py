import requests
import json

def call_gpt(system_prompt: str = " ", user_prompt:str = " "):
    # 定義請求的URL
    url = "http://ml.hsueh.tw/callapi/"

    # 定義請求的主體
    payload = {
        "engine": "gpt-35-turbo",
        "temperature": 0.7,
        "max_tokens": 200,
        "top_p": 0.95,
        "top_k": 5,
        "roles": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            },
        ],
        "frequency_penalty": 0,
        "repetition_penalty": 1.03,
        "presence_penalty": 0,
        "stop": "",
        "past_messages": 10,
        "purpose": "web人工智慧期末報告"
    }

    # 設置請求頭
    headers = {
        "Content-Type": "application/json"
    }

    # 發送POST請求
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print(response.json())
    # 取得回覆內容
    result = response.json()['choices'][0]['message']['content']
    
    return result