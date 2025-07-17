"""
Module for testing the MCP server creation and tool registration.
This module contains unit tests to verify the correct setup of the MCP server.
"""

import unittest
from unittest.mock import patch, Mock
from hkopenai.hk_tech_mcp_server.server import server


class TestServer(unittest.TestCase):
    """
    Test class for verifying the functionality of the MCP server application.
    """

    @patch("hkopenai.hk_tech_mcp_server.server.FastMCP")
    @patch("hkopenai.hk_tech_mcp_server.tools.security_incident.register")
    def test_server_startup(self, mock_register_func, mock_fastmcp):
        """
        Test the server startup and tool registration.
        Verifies that the server is created correctly and tools are registered as expected.
        """
        # Setup mocks
        mock_mcp_instance = Mock()
        mock_fastmcp.return_value = mock_mcp_instance

        # Call the server function
        server()

        # Verify FastMCP was instantiated
        mock_fastmcp.assert_called_once_with(name="HK OpenAI tech Server")

        # Verify tool registration
        mock_register_func.assert_called_once_with(mock_mcp_instance)

if __name__ == "__main__":
    unittest.main()
