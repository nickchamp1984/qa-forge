# MCP Inspector v1.0.0 (Windows) – Investigation Notes

## Environment

- OS: Windows
- Python: 3.12
- MCP SDK: 1.28.1
- MCP Inspector: 1.0.0
- Transport: STDIO

Server:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Hello Tool")

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

mcp.run()
```

---

## Initial problem

The MCP server failed to start when using standard Windows absolute paths.

Example error:

```text
C:\Python312\python.exe: can't open file
'C:\\Users\\nickp\\Desktop\\qa_forge\\UsersnickpDesktopqa_forgereference-implementationsmcppython001-hello-toolserver.py'
```

Observed behavior:

- global Python was started;
- `server.py` path became corrupted;
- the second part of the path lost all backslashes.

---

## Exploratory testing

Only **one variable was changed per experiment**.

| # | Command | Arguments | Result |
|---|---------|-----------|--------|
| 1 | `C:\...\python.exe` | `C:\...\server.py` | ❌ Fail |
| 2 | `C:\...\python.exe` | `C:\\...\server.py` | ✅ Pass |
| 3 | `C:\\...\python.exe` | `C:\\...\server.py` | ✅ Pass |
| 4 | `C:\\...\python.exe` | `C:\...\server.py` | ❌ Fail |
| 5 | `C:/.../python.exe` | `C:/.../server.py` | ✅ Pass |
| 6 | `C:\...\python.exe` | `C:/.../server.py` | ✅ Pass |

---

## Findings

### Arguments field

The issue is reproducible only when **Arguments** contains Windows paths using single backslashes (`\`).

Working alternatives:

```text
C:\\Users\\...
```

or

```text
C:/Users/...
```

---

### Command field

No evidence was found that **Command** has the same issue.

The executable path works correctly with standard Windows backslashes.

---

## Workarounds

Recommended configuration:

**Command**

```text
C:\Users\...\python.exe
```

**Arguments**

```text
C:/Users/.../server.py
```

Alternative:

```text
C:\\Users\\...\\server.py
```

Both successfully complete:

```text
initialize
    ↓
tools/list
    ↓
tools/call
    ↓
hello("Nick")
    ↓
Hello, Nick!
```

---

## Notes

The root cause has not yet been identified.

Current evidence suggests that the issue occurs during processing of the **Arguments** field somewhere between MCP Inspector UI and process creation.

Further investigation should focus on:

- argument parsing;
- Windows path escaping;
- process spawning implementation.

---

## Related Documents

Reference Implementation:

- `reference-implementations/mcp/python/001-hello-tool`

Engineering Case:

- `cases/0001-understanding-mcp`