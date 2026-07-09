# Engineering Case #0001

# Understanding MCP by Building One

**Status:** Draft v0.1

---

## Summary

This Engineering Case explores **Model Context Protocol (MCP)** from an engineering perspective.

Rather than studying the specification first, we intentionally build the smallest possible implementation to understand:

- what problem MCP solves;
- why it exists;
- where it fits into modern software architecture;
- when it should (and should not) be used.

This document is technology-independent.

The accompanying Reference Implementation demonstrates one possible implementation in Python.

---

# Problem

Large Language Models excel at reasoning but cannot directly interact with external systems.

They cannot:

- query databases;
- execute test frameworks;
- create Jira issues;
- call internal services;
- access proprietary business systems.

Without a common integration mechanism, every AI application must implement custom integrations for every external tool.

This creates duplicated engineering effort and tightly couples AI systems to implementation details.

The engineering challenge is not connecting AI to a database.

The challenge is designing a common interface between AI systems and external capabilities.

---

# Context

A typical engineering environment contains many independent systems.

Examples include:

- GitHub
- Jira
- Slack
- CI/CD pipelines
- Test frameworks
- Monitoring systems
- Databases
- Internal APIs

Each exposes a different interface.

Each requires a different client.

As the ecosystem grows, integration complexity increases.

---

# Engineering Question

Can a single protocol standardize communication between AI systems and engineering tools without requiring the language model to understand every individual API?

---

# Traditional Approach

```
LLM
 │
 ├── GitHub API
 ├── Jira REST API
 ├── Slack API
 ├── SQLite Driver
 ├── Internal REST API
 └── ...
```

Each integration is implemented independently.

Adding new systems requires additional custom engineering work.

---

# MCP Approach

```
                +-------------------+
                |      LLM          |
                +---------+---------+
                          |
                          | MCP
                          |
                +---------v---------+
                |    MCP Server     |
                +---------+---------+
                          |
          +---------------+---------------+
          |               |               |
      GitHub          SQLite          Jira
```

The language model communicates through a single protocol.

The MCP server becomes responsible for interacting with external systems.

Business logic remains outside the model.

---

# Why This Case?

This case is not about learning another technology.

It is about recognising an architectural pattern.

The implementation itself is intentionally small.

The engineering ideas behind it are considerably more important than the amount of code.

---

# Hypothesis

If AI systems communicate through a standard protocol,

then engineers can:

- reduce integration complexity;
- reuse engineering components;
- expose existing systems without changing the language model;
- separate business logic from AI reasoning.

---

# Decision

Instead of starting with the MCP specification,

we start with the smallest possible implementation.

Building a minimal server allows us to observe:

- protocol messages;
- client responsibilities;
- server responsibilities;
- tool discovery;
- tool invocation;
- response flow.

The specification will be studied afterwards.

---

# Reference Implementation

```
reference-implementations/
└── mcp/
    └── python/
        └── 001-hello-tool/
```

The implementation intentionally contains only the minimum functionality required to understand the protocol.

---

# Expected Learning Outcomes

After completing this Engineering Case, the reader should understand:

- why MCP exists;
- which engineering problem it solves;
- when MCP is appropriate;
- when a traditional API is sufficient;
- the responsibilities of an MCP client;
- the responsibilities of an MCP server;
- how an LLM interacts with external capabilities.

---

# Related Documents

- `docs/Vision.md`
- `docs/Architecture.md`

Reference Implementation:

- `reference-implementations/mcp/python/001-hello-tool`

---

# Lessons Learned

_To be completed after the implementation is finished._

---

# Review Status

This Engineering Case is expected to evolve.

Review after:

- completion of Reference Implementation #0001;
- introduction of additional MCP examples;
- significant architectural discoveries.

Engineering Cases document engineering thinking.

They should evolve together with engineering understanding.