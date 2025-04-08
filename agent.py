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

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())