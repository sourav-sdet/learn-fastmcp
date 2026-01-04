from fastmcp import FastMCP 

# To create a FastMCP Server, Instantiate the FastMCP Class
mcp = FastMCP("My First MCP Server")

# Add a tool that returns a simple greeting
# Write a Python function and decorate it with @mcp.tool to register it with the server
@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


# Run MCP Server - 2 ways
# 1- Call its run() method - This lets us run the server with python my_server.py
# Choose between different transports - stdio for local servers or http for remote access

# STDIO TRANSPORT - DEFAULT
if __name__ == "__main__":
    mcp.run()

# HTTP TRANSPORT
# if __name__ == "__main__":
#     mcp.run(transport="http", port=8000)

# 2- Using the FastMCP CLI
# Use the fastmcp run command
# fastmcp run my_server.py:mcp - for default stdio transport
# fastmcp run my_server.py:mcp --transport http --port 8000 - for http transport
