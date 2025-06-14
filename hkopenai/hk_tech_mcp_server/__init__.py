"""Hong Kong tech MCP Server package."""
from .app import main
from .tool_security_incident import get_security_incidents

__version__ = "0.1.0"
__all__ = ['main', 'get_security_incidents']
