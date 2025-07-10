"""
Module for creating and running the HK OpenAI Tech MCP Server.
This server provides tools for accessing government information security incident data in Hong Kong.
"""

import argparse
from typing import Dict, List
from fastmcp import FastMCP
from hkopenai.hk_tech_mcp_server import tool_security_incident


def create_mcp_server():
    """Create and configure the MCP server"""
    mcp = FastMCP(name="HK OpenAI tech Server")

    @mcp.tool(
        description="Number of Government information security incidents reported to Digital Policy Office in Hong Kong"
    )
    def get_security_incidents() -> List[Dict]:
        return tool_security_incident.get_security_incidents()

    return mcp


def main(args):
    """
    Main function to run the Tech MCP Server.
    Args:
        args: Command line arguments passed to the function.
    """
    server = create_mcp_server()

    if args.sse:
        server.run(transport="streamable-http", host=args.host, port=args.port)
        print(f"Tech MCP Server running in SSE mode on port {args.port}, bound to {args.host}")
    else:
        server.run()
        print("Tech MCP Server running in stdio mode")


if __name__ == "__main__":
    main()
