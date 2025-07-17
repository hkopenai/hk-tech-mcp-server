"""
Module for creating and running the HK OpenAI Tech MCP Server.
This server provides tools for accessing government information security incident data in Hong Kong.
"""

from fastmcp import FastMCP
from .tools import security_incident


def server():
    """Create and configure the MCP server"""
    mcp = FastMCP(name="HK OpenAI tech Server")

    security_incident.register(mcp)

    return mcp
