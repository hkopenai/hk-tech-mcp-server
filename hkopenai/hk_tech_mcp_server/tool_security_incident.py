"""
Module for fetching government information security incident data from the Digital Policy Office in Hong Kong.
Provides tools to retrieve incident statistics for analysis.
"""

from typing import List, Dict
import requests


def fetch_security_incident_data() -> List[Dict]:
    """Fetch security incident data from Digital Policy Office"""
    url = "https://www.govcert.gov.hk/en/incidents.json"
    response = requests.get(url)
    return response.json()


def register(mcp):
    """Registers the security incident tool with the FastMCP server."""

    @mcp.tool(
        description="Number of Government information security incidents reported to Digital Policy Office in Hong Kong"
    )
    def get_security_incidents() -> List[Dict]:
        """Get number of government information security incidents reported to Digital Policy Office in Hong Kong

        Returns:
            List of incidents by year with type and count details
        """
        return _get_security_incidents()


def _get_security_incidents() -> List[Dict]:
    """Get number of government information security incidents reported to Digital Policy Office in Hong Kong

    Returns:
        List of incidents by year with type and count details
    """
    return fetch_security_incident_data()
