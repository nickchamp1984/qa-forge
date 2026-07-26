"""Health-check tools for the QA Forge MCP server."""


def hello() -> str:
    """Return a simple connectivity greeting."""
    return "Hello from QA Forge!"


def ping() -> str:
    """Return a basic connectivity response."""
    return "pong"
