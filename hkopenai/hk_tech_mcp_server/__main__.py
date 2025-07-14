"""
Entry point module for the HK OpenAI Tech MCP Server.
This module serves as the main executable to start the server.
"""

from hkopenai_common.cli_utils import cli_main
from . import server

if __name__ == "__main__":
    cli_main(server.main, "HK Tech MCP Server")
