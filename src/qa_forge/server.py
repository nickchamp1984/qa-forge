from mcp.server.fastmcp import FastMCP

mcp = FastMCP("QA Forge")

# register tools
@mcp.tool()
def hello() -> str:
    """Simple connectivity test."""
    return "Hello from QA Forge!"

def main():
    mcp.run()


if __name__ == "__main__":
    main()