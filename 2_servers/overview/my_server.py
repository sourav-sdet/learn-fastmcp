# CREATING A FASTMCP SERVER
# Provide a name for your server which helps identify it in client applications or logs

from fastmcp import FastMCP 

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

# COMPONENTS OF A MCP SERVER

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

# TAG BASED FILTERING
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
mcp_with_include_filter=FastMCP(include_tags={"public"})

# Hide components marked as internal or admin
mcp_with_exclude_filter=FastMCP(exclude_tags={"internal", "admin"})

# Combine both: show admin tools but hide deprecated ones
mcp_combine_filter=FastMCP(include_tags={"admin"}, exclude_tags={"deprecated"})

