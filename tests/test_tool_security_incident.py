"""
Module for testing the security incident tool functionality.

This module contains unit tests for fetching and processing security incident data.
"""

import unittest
from unittest.mock import patch, MagicMock

from hkopenai.hk_tech_mcp_server.tools.security_incident import (
    _get_security_incidents,
    register,
)


class TestSecurityIncident(unittest.TestCase):
    """
    Test class for verifying security incident functionality.

    This class contains test cases to ensure the data fetching and processing
    for security incident data work as expected.
    """

    def test_get_security_incidents(self):
        """
        Test the retrieval of security incidents data.

        This test verifies that the function correctly fetches and returns data,
        and handles error cases.
        """
        # Mock the JSON data
        mock_json_data = [
            {"year": 2020, "type": "Malware", "count": 10},
            {"year": 2020, "type": "Phishing", "count": 5},
            {"year": 2021, "type": "Malware", "count": 12},
        ]

        with patch(
            "hkopenai.hk_tech_mcp_server.tools.security_incident.fetch_json_data"
        ) as mock_fetch_json_data:
            # Setup mock response for successful data fetching
            mock_fetch_json_data.return_value = mock_json_data

            # Test successful data retrieval
            result = _get_security_incidents()
            self.assertEqual(len(result), 3)
            self.assertEqual(result[0]["year"], 2020)
            self.assertEqual(result[0]["type"], "Malware")

            # Test error handling when fetch_json_data returns an error
            mock_fetch_json_data.return_value = {"error": "JSON fetch failed"}
            result = _get_security_incidents()
            self.assertEqual(result, {'error': 'JSON fetch failed'})

    def test_register_tool(self):
        """
        Test the registration of the get_security_incidents tool.

        This test verifies that the register function correctly registers the tool
        with the FastMCP server and that the registered tool calls the underlying
        _get_security_incidents function.
        """
        mock_mcp = MagicMock()

        # Call the register function
        register(mock_mcp)

        # Verify that mcp.tool was called with the correct description
        mock_mcp.tool.assert_called_once_with(
            description="Number of Government information security incidents reported to Digital Policy Office in Hong Kong"
        )

        # Get the mock that represents the decorator returned by mcp.tool
        mock_decorator = mock_mcp.tool.return_value

        # Verify that the mock decorator was called once (i.e., the function was decorated)
        mock_decorator.assert_called_once()

        # The decorated function is the first argument of the first call to the mock_decorator
        decorated_function = mock_decorator.call_args[0][0]

        # Verify the name of the decorated function
        self.assertEqual(decorated_function.__name__, "get_security_incidents")

        # Call the decorated function and verify it calls _get_security_incidents
        with patch(
            "hkopenai.hk_tech_mcp_server.tools.security_incident._get_security_incidents"
        ) as mock_get_security_incidents:
            decorated_function()
            mock_get_security_incidents.assert_called_once()
