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


if __name__ == "__main__":
    mcp.run()