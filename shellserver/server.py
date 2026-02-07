from fastmcp import FastMCP
import subprocess

# Create FastMCP server instance
mcp = FastMCP("Terminal Server")

@mcp.tool
def terminal_tool(command: str) -> str:
    """
    Execute a terminal command and return the output.
    
    Args:
        command: The terminal command to execute
        
    Returns:
        The stdout and stderr output from the command
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = result.stdout
        if result.stderr:
            output += f"\n[stderr]\n{result.stderr}"
            
        if result.returncode != 0:
            output += f"\n[exit code: {result.returncode}]"
            
        return output if output else f"Command executed successfully (exit code: {result.returncode})"
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 30 seconds"
    except Exception as e:
        return f"Error executing command: {str(e)}"

@mcp.resource("file:///mcpreadme")
async def mcpreadme() -> str:
    """
    Expose mcpreadme.md from the user's project directory
    
    Returns:
        The contents of mcpreadme.md as a string
    """
    file_path = Path.home() / "Desktop" / "learn-fastmcp" / "learn-fastmcp" / "shellserver"
    readme_path = file_path / "mcpreadme.md"
    
    try:
        with open(readme_path, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading mcpreadme.md: {str(e)}"

@mcp.prompt
def get_research_prompt(topic: str) -> str:
    """
    Create a prompt asking for research on a given topic.
    
    Args:
        topic: The topic to research
        
    Returns:
        A prompt asking for research on the given topic
    """
    return f"Research the following topic: {topic}"

if __name__ == "__main__":
    mcp.run()