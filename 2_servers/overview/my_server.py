# CREATING A FASTMCP SERVER
# Provide a name for your server which helps identify it in client applications or logs

from fastmcp import FastMCP 

# Create a basic server instance
mcp = FastMCP(name="MyAssistant1")

# You can also add instructions for how to interact with the server
mcp_with_instructions = FastMCP(
    name="MyAssistant2",
    instructions="""
    This server provides data analysis tools.
    Call get_average() to get numerical data.
    """,
)

