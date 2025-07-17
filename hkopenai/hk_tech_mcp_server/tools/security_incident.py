"""
Module for fetching government information security incident data from the Digital Policy Office in Hong Kong.
Provides tools to retrieve incident statistics for analysis.
"""

from typing import List, Dict
from hkopenai_common.json_utils import fetch_json_data


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


def _get_security_incidents() -> List[Dict] | Dict:
    """Get number of government information security incidents reported to Digital Policy Office in Hong Kong

    Returns:
        List of incidents by year with type and count details
    """
    url = "https://www.govcert.gov.hk/en/incidents.json"
    data = fetch_json_data(url)
    return data
