from mcp.server.fastmcp import FastMCP
from qa_forge.tools.health import hello, ping

mcp = FastMCP("QA Forge")

# Register tools.
mcp.tool()(hello)
mcp.tool()(ping)


def main():
    mcp.run()


if __name__ == "__main__":
    main()
