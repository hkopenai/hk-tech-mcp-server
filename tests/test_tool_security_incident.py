"""
Module for testing the security incident data fetching functionality.
This module contains unit tests to verify the correct retrieval of security incident data.
"""

import unittest
from unittest.mock import patch
from hkopenai.hk_tech_mcp_server.tool_security_incident import (
    fetch_security_incident_data,
    get_security_incidents,
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
        result = get_security_incidents()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["year"], 2025)
        self.assertEqual(result[1]["incident"][0]["number"], 3)


if __name__ == "__main__":
    unittest.main()
