# CREATING A FASTMCP SERVER
# Provide a name for your server which helps identify it in client applications or logs

from fastmcp import FastMCP 

# -------------------------- CREATING A MCP SERVER -------------------------------------------------

# Create a basic server instance
mcp = FastMCP(name="MyAssistant1")

# You can also add instructions for how to interact with the server
# mcp_with_instructions = FastMCP(
#     name="MyAssistant2",
#     instructions="""
#     This server provides data analysis tools.
#     Call get_average() to get numerical data.
#     """,
# )

# -------------------------------- COMPONENTS OF A MCP SERVER ----------------------------------------

# TOOLS
# Tools are functions that the client can call to perform actions or access external systems
@mcp.tool 
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together"""
    return a * b 


# RESOURCES
# Resources expose data sources that the client can read
@mcp.resource("data://config")
def get_config() -> dict:
    """Provides the application configuration."""
    return {"theme": "dark", "version": "1.0"}

# RESOURCE TEMPLATES
# Resource Templates are parameterized resources that allow client to request specific data
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> dict:
    """Retrieves a user's profile by ID."""
    # The {user_id} in the URI is extracted and passed to this function
    return {"id": user_id, "name": f"User {user_id}", "status": "active"}

# PROMPTS
# Prompts are reusable message templates for guiding LLMs
@mcp.prompt
def analyze_data(data_points: list[float]) -> str:
    """Creates a prompt asking for analysis of numerical data."""
    formatted_data = ", ".join(str(point) for point in data_points)
    return f"Please analyze these data points: {formatted_data}"

# --------------------------------- TAG BASED FILTERING -------------------------------------------
# Selectively expose components based on configurable include excluse tag sets
# Helpful to provide different views of server as per environments or users
# Components can be tagged using the tags parameter
@mcp.tool(tags={"public", "allUsers"})
def public_tool() -> str:
    return "This tool is public"

@mcp.tool(tags={"internal", "admin"})
def internal_tool() -> str:
    return "This tool is for admins only"

# To ensure that a component is never exposed, mark enable=False on the component itself.

# Configure Tag Based Filtering when creating the MCP Server

# Only expose components tagged with public
# mcp=FastMCP(include_tags={"public"})

# Hide components marked as internal or admin
# mcp=FastMCP(exclude_tags={"internal", "admin"})

# Combine both: show admin tools but hide deprecated ones
# mcp=FastMCP(include_tags={"admin"}, exclude_tags={"deprecated"})


# -------------------------------- RUNNING THE SERVER -----------------------------------------
# FastMCP Server need a transport mechanism to communicate with clients
# Start the server by calling mcp.run() on the FastMCP instance
if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    mcp.run()

    # For HTTP Transport Mode
    # mcp.run(transport="http", port=8080)


# ---------------------------- CUSTOM ROUTES --------------------------------------------
#@mcp.custom_route("/health", methods=["GET"])
#async def health_check(request: Request) -> PlainTextResponse:
    #return PlainTextResponse("OK")

#if __name__ == "__main__":
    #mcp.run(transport="http")  # Health check at http://localhost:8000/health

# --------------------------- IMPORTING A SUB SERVER ------------------------------------
# Compose multiple servers together using import_server(static copy) or mount(live link)
main = FastMCP("Main Server")
sub = FastMCP("Sub Server")

@sub.tool()
def hello():
    return "Hello"

# Mount Directly
main.mount(sub, prefix="sub")

# ------------------------- PROXYING SERVERS ----------------------------------------
# FastMCP can act as a proxy for any mcp server (local or remote) using FastMCP.as_proxy, letting to bridge transports
# or acting as a front end for existing servers
# from fastmcp import FastMCP, Client 
# backend = Client("http://example.com/mcp/sse")
#proxy = FastMCP.as_proxy(backend, name="Proxy Server")

# ------------------------ CUSTOM TOOL SERIALIZATION -------------------------------
# By default, FastMCP serializes tool return values to JSON
# This can be customized using tool_serializer when creating the server
# import yaml
# from fastmcp import FastMCP

# Define a custom serializer that formats dictionaries as YAML
# def yaml_serializer(data):
#     return yaml.dump(data, sort_keys=False)

# Create a server with the custom serializer
# mcp = FastMCP(name="MyServer", tool_serializer=yaml_serializer)

# @mcp.tool
# def get_config():
#     """Returns configuration in YAML format."""
#     return {"api_key": "abc123", "debug": True, "rate_limit": 100}

