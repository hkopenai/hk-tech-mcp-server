"""Live integration test for the government information security incident feed.

These tests hit the real Digital Policy Office endpoint
(https://www.govcert.gov.hk/en/incidents.json) and are intentionally not
mocked. They are skipped unless the RUN_LIVE_TESTS environment variable is
set, and they share the throttle autouse fixture from ``conftest.py`` so
running them back-to-back does not trip the upstream rate-limiter.
"""

import os
import unittest

from hkopenai.hk_tech_mcp_server.tools.security_incident import (
    _get_security_incidents,
)


@unittest.skipUnless(
    os.environ.get("RUN_LIVE_TESTS") == "true",
    "set RUN_LIVE_TESTS=true to run live integration tests",
)
class TestSecurityIncidentLive(unittest.TestCase):
    """Live integration test against the Digital Policy Office feed."""

    def test_returns_non_empty_list(self):
        """The live feed should return at least one year of incidents."""
        result = _get_security_incidents()
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0, "expected at least one year of incidents")

    def test_each_entry_has_year_and_incident_list(self):
        """Each entry should expose a numeric `year` and a non-empty `incident` list."""
        result = _get_security_incidents()
        self.assertIsInstance(result, list)
        for entry in result:
            self.assertIn("year", entry)
            self.assertIsInstance(entry["year"], int)
            self.assertIn("incident", entry)
            self.assertIsInstance(entry["incident"], list)
            self.assertTrue(
                len(entry["incident"]) > 0,
                f"year {entry['year']} has no incident rows",
            )

    def test_incident_rows_have_type_and_number(self):
        """Each incident row should have a non-empty `type` and integer `number`."""
        result = _get_security_incidents()
        self.assertIsInstance(result, list)
        for entry in result:
            for row in entry["incident"]:
                self.assertIn("type", row)
                self.assertIsInstance(row["type"], str)
                self.assertTrue(row["type"], "incident type must not be empty")
                self.assertIn("number", row)
                self.assertIsInstance(row["number"], int)
                self.assertGreaterEqual(row["number"], 0)


if __name__ == "__main__":
    unittest.main()
