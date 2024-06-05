# Computer Assemble Assistant

## 簡介
Computer Assemble Assistant 是一個基於對話的電腦組裝助手系統。該系統通過與用戶的對話，了解用戶的需求，並根據需求提供電腦零組件推薦清單。系統包括需求收集、需求分類、與 Pinecone 和 GPT-API 交互等功能，並使用了責任鏈設計模式來管理不同的任務處理器。

## 目錄結構

```
(base) hsueh@q computer-assemble-assistant % tree
.
root
├── agenda.py
├── frame.py
├── gpt_api.py
├── main.py
└── task_handlers
    ├── __init__.py
    ├── ask_genai_handler.py
    ├── chat_history_control_handler.py
    ├── get_message_handler.py
    ├── last_check_handler.py
    ├── read_input_handler.py
    ├── remove_stopwords_handler.py
    ├── requirement_classification_handler.py
    └── task_handler.py
```

## 主要模塊

### 1. `task_handlers`

此文件夾包含所有任務處理器，每個處理器負責處理特定任務：

- `task_handler.py`：基本任務處理器類。
- `chat_history_control_handler.py`：處理聊天歷史記錄控制的處理器。
- `remove_stopwords_handler.py`：處理刪除停用詞的處理器。
- `requirement_classification_handler.py`：處理需求分類的處理器。
- `read_input_handler.py`：處理讀取用戶輸入的處理器。
- `get_message_handler.py`：處理從數據庫中獲取消息的處理器。
- `ask_genai_handler.py`：處理詢問 GPT 的處理器。
- `last_check_handler.py`：處理最後檢查的處理器。

### 2. `frame.py`

定義 `Frame` 類，用於存儲對話狀態信息，包括用戶需求列表和組裝的電腦零組件清單。

### 3. `agenda.py`

定義 `Agenda` 類，用於管理對話任務列表。

### 4. `dialogue_manager.py`

定義 `DialogueManager` 類，負責管理整個對話流程，創建和管理任務處理器鏈，處理用戶輸入和對話邏輯。

### 5. `main.py`

主程序入口，初始化對話管理器，收集用戶需求，與 Pinecone 和 GPT 交互，獲取電腦零組件推薦清單，並進行最後檢查。

## 安裝與運行

### 依賴項目

請確保已安裝以下 Python 庫：

- pinecone-client
- sentence-transformers
- mysql-connector-python
- textwrap

### 運行步驟

1. 克隆或下載此存儲庫到本地。
2. 安裝所需的 Python 庫：
   ```bash
   pip install pinecone-client sentence-transformers mysql-connector-python
   ```
3. 配置 Pinecone API 密鑰和 MySQL 資料庫連接信息。
4. 運行 `main.py` 開始對話：
   ```bash
   python main.py
   ```

## 系統流程

1. 用戶啟動對話，系統提示用戶提供組裝電腦的需求。
2. 系統通過責任鏈模式依次處理用戶輸入，分類需求，並控制對話歷史記錄。
3. 系統從 Pinecone 中查詢相關信息，並使用 GPT 生成電腦零組件推薦清單。
4. 系統進行最後檢查，確保推薦清單滿足用戶需求和預算。
5. 向用戶返回最終的電腦零組件推薦清單。

