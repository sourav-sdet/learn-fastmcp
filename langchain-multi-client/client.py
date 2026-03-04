import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langchain_core.agents import create_react_agent
load_dotenv()

# Initialize the default OpenAI Chat Model
llm = ChatOpenAI() 

async def main():

    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["/Users/ruso/Desktop/learn-fastmcp/learn-fastmcp/langchain-multi-client/server/math_server.py"],
            } ,
            "weather": {
                "url": "http://localhost:8001/sse",
                "transport": "sse",
            }
        }
        
    ) as client:
        agent = create_react_agent(llm, tools=client.tools)
        result = await client.ainvoke({"messages":"What is the weather in Tokyo?"})
        print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())