from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Hello Tool")


@mcp.tool()
def hello(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"

mcp.run()