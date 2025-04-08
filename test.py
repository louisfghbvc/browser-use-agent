from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio, os

llm = ChatOpenAI(
    openai_api_base=os.getenv("OPENAI_BASE_URL"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="deepseek/deepseek-chat-v3-0324:free"
)

def test_llm():
    try:
        # 測試簡單問題
        test_message = "What is 1 + 1? Please answer in one word."
        response = llm.invoke(test_message)
        print("測試結果：")
        print(f"問題：{test_message}")
        print(f"回答：{response}")
    except Exception as e:
        print(f"測試時發生錯誤：{str(e)}")

# 執行測試
test_llm()