import asyncio
from dotenv import load_dotenv
from fastmcp import Client

load_dotenv()


# Client for Math MCP Server
# Provide the absolute path of the server.py file
math_client = Client("/Users/ruso/Desktop/learn-fastmcp/learn-fastmcp/langchain-mcp-client/server/math_server.py") 


async def main():

    # Connection established here
    async with math_client:

        print(f"Connected: {math_client.is_connected()}")

        # Initialization already happened automatically
        print(f"Server: {math_client.initialize_result.serverInfo.name}")
        print(f"Version: {math_client.initialize_result.serverInfo.version}")
        print(f"Instructions: {math_client.initialize_result.instructions}")
        print(f"Capabilities: {math_client.initialize_result.capabilities.tools}")

        # Basic server interaction to verify if server is reachable
        await math_client.ping()

        # List Available Tools
        mcp_tools = await math_client.list_tools()
        print(f"Tools: {mcp_tools}")

        # Execute Tools
        result = await math_client.call_tool("add", {"a": 1, "b": 2})
        print(f"Executing Tool 'add' with result: {result}")

        # Connection closed automatically here
        print(f"Connected: {math_client.is_connected()}")

if __name__ == "__main__":
    asyncio.run(main())