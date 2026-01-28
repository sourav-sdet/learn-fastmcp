from fastmcp import FastMCP

mcp = FastMCP("Weather MCP Server")

@mcp.tool
def get_weather() -> str:
    return f"The weather in New York is sunny"

if __name__ == "__main__":
    mcp.run(transport="sse")