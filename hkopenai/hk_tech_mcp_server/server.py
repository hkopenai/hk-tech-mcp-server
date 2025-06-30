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
    parser = argparse.ArgumentParser(description='HKO MCP Server')
    parser.add_argument('-s', '--sse', action='store_true',
                       help='Run in SSE mode instead of stdio')
    args = parser.parse_args()

    server = create_mcp_server()
    
    if args.sse:
        server.run(transport="streamable-http")
        print("HKO MCP Server running in SSE mode on port 8000")
    else:
        server.run()
        print("HKO MCP Server running in stdio mode")

if __name__ == "__main__":
    main()
