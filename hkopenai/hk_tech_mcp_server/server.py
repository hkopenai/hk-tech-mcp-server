"""
Module for creating and running the HK OpenAI Tech MCP Server.
This server provides tools for accessing government information security incident data in Hong Kong.
"""

from fastmcp import FastMCP
from hkopenai.hk_tech_mcp_server import tool_security_incident


def create_mcp_server():
    """Create and configure the MCP server"""
    mcp = FastMCP(name="HK OpenAI tech Server")

    tool_security_incident.register(mcp)

    return mcp


def main(host: str, port: int, sse: bool):
    """
    Main function to run the Tech MCP Server.
    Args:
        args: Command line arguments passed to the function.
    """
    server = create_mcp_server()

    if sse:
        server.run(transport="streamable-http", host=host, port=port)
        print(
            f"Tech MCP Server running in SSE mode on port {port}, bound to {host}"
        )
    else:
        server.run()
        print("Tech MCP Server running in stdio mode")
