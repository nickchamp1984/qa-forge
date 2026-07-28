# ADR-004

# Knowledge Layer Responsibilities

**Status:** Proposed

---

# Context

ADR-001 establishes the Knowledge Layer as the architectural core of QA Forge.

ADR-002 defines the principle that repositories should explain themselves to AI.

ADR-003 introduces the Canonical Engineering Knowledge Model.

The next architectural decision is to define the responsibilities and boundaries of the Knowledge Layer.

Without explicit boundaries, knowledge extraction, storage, reasoning, and AI orchestration may become tightly coupled, making the platform difficult to evolve.

---

# Decision

The Knowledge Layer is responsible for representing, storing, and exposing engineering knowledge.

It is not responsible for source parsing, AI reasoning, or workflow orchestration.

The Knowledge Layer serves as the stable engineering knowledge backbone of the platform.

---

# Responsibilities

The Knowledge Layer SHALL:

- maintain the canonical engineering knowledge model;
- store entities and relations;
- preserve traceability to original engineering artifacts;
- provide a technology-independent API for knowledge access;
- remain independent of AI providers and LLM implementations.

---

# Non-Responsibilities

The Knowledge Layer SHALL NOT:

- parse Markdown documents;
- parse source code directly;
- call LLM APIs;
- perform autonomous reasoning;
- execute engineering workflows;
- generate documentation;
- implement repository-specific logic.

These responsibilities belong to extractors, AI agents, or higher-level orchestration components.

---

# Architectural Boundaries

Engineering artifacts

↓

Extractors

↓

Knowledge Layer

↓

AI Agents

↓

Applications

The Knowledge Layer is intentionally positioned between data acquisition and intelligent reasoning.

It provides structured engineering knowledge while remaining independent of both.

---

# Consequences

Positive:

- Clear separation of concerns.
- Stable platform architecture.
- Independent evolution of extractors and AI agents.
- Easier testing.
- Reduced coupling between engineering knowledge and AI technologies.

Negative:

- Requires well-defined interfaces between layers.
- Some information must be translated before entering the Knowledge Layer.

---

# Related Documents

- Vision.md
- Architecture.md
- ADR-001 Knowledge Layer as the Core Architecture
- ADR-002 Repository Explains Itself to AI
- ADR-003 Canonical Engineering Knowledge Model