"""
Module for fetching government information security incident data from the Digital Policy Office in Hong Kong.
Provides tools to retrieve incident statistics for analysis.
"""

import requests
from typing import List, Dict
from pydantic import Field
from typing_extensions import Annotated


def fetch_security_incident_data() -> List[Dict]:
    """Fetch security incident data from Digital Policy Office"""
    url = "https://www.govcert.gov.hk/en/incidents.json"
    response = requests.get(url)
    return response.json()


def get_security_incidents() -> List[Dict]:
    """Get number of government information security incidents reported to Digital Policy Office in Hong Kong

    Returns:
        List of incidents by year with type and count details
    """
    return fetch_security_incident_data()
