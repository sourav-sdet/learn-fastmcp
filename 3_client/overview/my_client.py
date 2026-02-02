# The FastMCP Client

import asyncio
from fastmcp import Client, FastMCP

# In-memory server (ideal for testing)
client_memory = Client(FastMCP("TestServer"))

# HTTP server
client_http = Client("https://api.example.com/mcp")

# Python stdio transport
client_script = Client("./server.py") 


# Configuration Based Client
config = {
    "mcpServers": {
        "weather": {"url": "https://weather-api.example.com/mcp"},
        "assistant": {"command": "python", "args": ["./assistant_server.py"]}
    }
}
client_config = Client(config)


# Disable automatic initialization
client_manual = Client("my_mcp_server.py", auto_initialize=False)

async with client_manual:
    # Connection established, but not initialized yet
    print(f"Connected: {client.is_connected()}")
    print(f"Initialized: {client.initialize_result is not None}")  # False

    # Initialize manually with custom timeout
    result = await client.initialize(timeout=10.0)
    print(f"Server: {result.serverInfo.name}")


async with client_config:
    # Tools are prefixed with server names
    weather_data = await client_config.call_tool("weather_get_forecast", {"city": "London"})
    response = await client_config.call_tool("assistant_answer_question", {"question": "What's the capital of France?"})
    
    # Resources use prefixed URIs
    icons = await client_config.read_resource("weather://weather/icons/sunny")
    templates = await client_config.read_resource("resource://assistant/templates/list")



async def main():
    async with client:

        # Initialization already happened automatically
        print(f"Server: {client.initialize_result.serverInfo.name}")
        print(f"Version: {client.initialize_result.serverInfo.version}")
        print(f"Instructions: {client.initialize_result.instructions}")
        print(f"Capabilities: {client.initialize_result.capabilities.tools}")

        # Basic server interaction to verify if server is reachable
        await client.ping()


        
        # List available operations to see what tools, resources, and prompts are available
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        # Execute operations
        result = await client.call_tool("example_tool", {"param": "value"})
        print(result)


asyncio.run(main())