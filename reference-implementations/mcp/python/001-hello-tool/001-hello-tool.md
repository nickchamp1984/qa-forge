# 001 - Hello Tool

## Objective

...

## Environment

...

## Repository Structure

```text
reference-implementations/
└── mcp/
    └── python/
        └── 001-hello-tool/
            ├── server.py
            ├── requirements.txt
            └── 001-hello-tool.md
```

## Procedure

### Execution Flow

The implementation was validated using MCP Inspector.

Execution sequence:

```text
python server.py
        ↓
MCP Inspector starts the process
        ↓
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

This confirms that:

- the server starts correctly;
- the tool is successfully discovered;
- the tool invocation completes successfully.

### Virtual Environment Activation

The activation command depends on the shell being used.

PowerShell

.venv\Scripts\Activate.ps1

Command Prompt (cmd)

.venv\Scripts\activate.bat

Git Bash

source .venv/Scripts/activate

Verification

python --version
which python

Expected Result

- (.venv) prefix appears in terminal.
- python --version returns the expected version.
- which python points to .venv/Scripts/python.

---

## Metrics

Environment creation
~20 s

Dependency installation
~3–4 min

Installed packages
32

Python
3.12.6

OS
Windows 11

Notes

- Initial connection to PyPI timed out twice.
- Installation completed successfully after retries.

### SDK Architecture Discovery

The SDK exposes two primary server abstractions:

- FastMCP
- Server

This suggests that the SDK supports both:

- rapid application development (FastMCP)
- lower-level protocol implementation (Server)

The package also separates transports (`stdio`, `sse`, `streamable_http`) from the server implementation.

---

## Engineering Findings

### Virtual Environment
Renaming a project directory after creating `.venv` on Windows breaks `pip.exe` launchers because they store an absolute interpreter path.

### Dependency Installation
Installing `mcp` pulls a substantial dependency tree (~30 packages).

### SDK Architecture
The SDK exposes both high-level (`FastMCP`) and low-level (`Server`) APIs.

### SDK Testing
The official documentation examples are covered by the SDK's automated tests and can be tested in-memory via `Client(mcp)`.

### Documentation Versioning

Initially, the latest online documentation was used by mistake.

The installed SDK version (1.28.1) has its own versioned documentation.

Using documentation that does not match the installed SDK resulted in API mismatches (e.g. `MCPServer` does not exist in v1.28.1).

Lesson:
Always verify that the documentation version matches the installed package version before implementing examples.

---

## Related Documents

Engineering Case:

- `cases/0001-understanding-mcp`

Investigation:

- `reference-implementations/mcp/mcp-inspector-windows-paths.md`

---

## Next Step

The next reference implementation will extend the minimal server and continue exploring additional MCP capabilities.