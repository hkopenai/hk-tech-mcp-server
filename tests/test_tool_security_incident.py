"""
Module for testing the security incident data fetching functionality.
This module contains unit tests to verify the correct retrieval of security incident data.
"""

import unittest
from unittest.mock import patch, MagicMock

from hkopenai.hk_tech_mcp_server.tool_security_incident import (
    fetch_security_incident_data,
    _get_security_incidents,
    register,
)


class TestSecurityIncident(unittest.TestCase):
    """
    Test class for verifying the functionality of security incident data retrieval.
    """
    JSON_DATA = [
        {
            "year": 2025,
            "incident": [
                {"type": "Web defacement", "number": 1},
                {"type": "Loss of mobile devices", "number": 2},
            ],
        },
        {
            "year": 2024,
            "incident": [
                {"type": "Compromise of systems", "number": 3},
                {"type": "Ransomware", "number": 1},
            ],
        },
    ]

    def setUp(self):
        self.mock_requests = patch("requests.get").start()
        mock_response = self.mock_requests.return_value
        mock_response.json.return_value = self.JSON_DATA
        self.addCleanup(patch.stopall)

    def test_fetch_security_incident_data(self):
        """
        Test the fetching of security incident data from the Digital Policy Office.
        Verifies that the data structure and content are as expected.
        """
        result = fetch_security_incident_data()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["year"], 2025)
        self.assertEqual(len(result[0]["incident"]), 2)
        self.assertEqual(result[1]["incident"][1]["type"], "Ransomware")

    def test_get_security_incidents(self):
        """
        Test the retrieval of security incidents reported to the Digital Policy Office.
        Verifies that the data returned matches the expected structure and content.
        """
        result = _get_security_incidents()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["year"], 2025)
        self.assertEqual(result[1]["incident"][0]["number"], 3)

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
            "hkopenai.hk_tech_mcp_server.tool_security_incident._get_security_incidents"
        ) as mock_get_security_incidents:
            decorated_function()
            mock_get_security_incidents.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
