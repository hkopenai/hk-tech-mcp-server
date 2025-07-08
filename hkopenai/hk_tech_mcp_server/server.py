"""
Module for creating and running the HK OpenAI Tech MCP Server.
This server provides tools for accessing government information security incident data in Hong Kong.
"""

import argparse
from fastmcp import FastMCP
from hkopenai.hk_tech_mcp_server import tool_security_incident
from typing import Dict, List, Annotated, Optional
from pydantic import Field


def create_mcp_server():
    """Create and configure the MCP server"""
    mcp = FastMCP(name="HK OpenAI tech Server")

    @mcp.tool(
        description="Number of Government information security incidents reported to Digital Policy Office in Hong Kong"
    )
    def get_security_incidents() -> List[Dict]:
        return tool_security_incident.get_security_incidents()

    return mcp


def main():
    """
    Main function to run the HC Tech MCPServer.
    Parses command line arguments to determine the mode of operation (SSE or stdio).
    """
    parser = argparse.ArgumentParser(description="HC Tech MCPServer")
    parser.add_argument(
        "-s", "--sse", action="store_true", help="Run in SSE mode instead of stdio"
    )
    parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="Host to bind the server to"
    )
    args = parser.parse_args()

    server = create_mcp_server()

    if args.sse:
        server.run(transport="streamable-http", host=args.host)
        print(f"HC Tech MCPServer running in SSE mode on port 8000, bound to {args.host}")
    else:
        server.run()
        print("HC Tech MCPServer running in stdio mode")


if __name__ == "__main__":
    main()
