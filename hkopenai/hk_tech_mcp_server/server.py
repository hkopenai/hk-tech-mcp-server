"""
Module for creating and running the HK OpenAI Tech MCP Server.
This server provides tools for accessing government information security incident data in Hong Kong.
"""

from fastmcp import FastMCP
from hkopenai.hk_tech_mcp_server.tools import security_incident


def server(host: str, port: int, sse: bool):
    """Create and configure the MCP server"""
    mcp = FastMCP(name="HK OpenAI tech Server")

    security_incident.register(mcp)

    if sse:
        mcp.run(transport="streamable-http", host=host, port=port)
        print(f"Tech MCP Server running in SSE mode on port {port}, bound to {host}")
    else:
        mcp.run()
        print("Tech MCP Server running in stdio mode")
