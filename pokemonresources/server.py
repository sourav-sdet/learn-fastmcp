"""
Mini Pokédex Lite - FastMCP 2.0 Resources Demo (Async Version)

This demo teaches MCP resources by providing a simple Pokédex interface.
It demonstrates:
- Static resource listing with @mcp.resource (async)
- Dynamic resource templates with URI parameters (async)
- External API integration with PokeAPI (async httpx)
- Error handling and JSON responses
- Proper async/await patterns

Usage:
    python server.py

MCP Resources provided:
- poke://pokemon/1 (Bulbasaur)
- poke://pokemon/4 (Charmander) 
- poke://pokemon/7 (Squirtle)
- poke://pokemon/{id} (Any Pokémon by ID)
"""

import httpx
from fastmcp import FastMCP
from fastmcp.exceptions import ResourceError

mcp = FastMCP("Mini Pokédex Lite")



# Starter Pokemon Data for Demonstration
STARTERS = [
    {"1", "Bulbasaur"},
    {"4", "Charmander"},
    {"7", "Squirtle"},
]


# STATIC RESOURCE
@mcp.resource("poke://starters")
async def list_starters() -> dict:
    """ List all Starter Pokemon available """
    return{
        "starters": [
            {
                "id": pid,
                "name": name.capitalize(),
            "uri": f"poke://pokemon/{pid}"
            }
            for pid, name in STARTERS.items()
        ]
        "total": len(STARTERS)
    }

