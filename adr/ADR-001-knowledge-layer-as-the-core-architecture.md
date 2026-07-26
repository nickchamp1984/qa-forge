# ADR-001 — Knowledge Layer as the Core Architecture

**Status:** Accepted

**Date:** 2026-07-26

---

# Context

QA Forge was initially designed around a collection of tools that allowed AI assistants to interact with engineering repositories.

In this architecture, repository access was considered the primary capability. Every AI interaction required the repository to be explored again, relevant files to be selected, and engineering context to be reconstructed from raw artifacts.

While this approach worked, it revealed several architectural limitations.

Engineering knowledge became tightly coupled to repository traversal.

Different AI models could interpret the same repository differently.

The same engineering context had to be reconstructed repeatedly, increasing both computational cost and inconsistency.

At the same time, the project vision consistently emphasized that engineering knowledge—not frameworks or technologies—is the primary asset of QA Forge.

---

# Decision

QA Forge adopts a **Knowledge Layer architecture**.

The architectural center of the platform is no longer repository access.

Instead, repositories are transformed into structured engineering knowledge through a dedicated ingestion process.

AI assistants interact with engineering knowledge rather than reconstructing repository understanding during every session.

The Knowledge Layer becomes the stable interface between repositories and AI systems.

Repository integrations, programming languages, documentation formats and AI providers are treated as replaceable adapters around this layer.

---

# Consequences

## Positive

- Engineering knowledge becomes reusable across all AI platforms.
- Repository understanding is generated once and reused many times.
- AI models become interchangeable clients.
- Repository-specific complexity is isolated from reasoning.
- Engineering knowledge becomes an explicit architectural asset.

## Negative

- Repository ingestion becomes a first-class subsystem.
- Extractors require ongoing maintenance.
- Knowledge synchronization introduces additional complexity.
- More infrastructure is required before AI interaction becomes possible.

---

# Architectural Impact

Previous architecture:

```text
Repository
    ↓
MCP
    ↓
LLM
```

Target architecture:

```text
Repository
    ↓
Knowledge Extraction
    ↓
Knowledge Layer
    ↓
Knowledge API
    ↓
AI Client
```

---

# Rationale

The objective of QA Forge is not to help AI read repositories more efficiently.

The objective is to make engineering knowledge explicit, reusable and independent of any particular AI model.

---

# Related Documents

- Vision
- Architecture
- ADR-002