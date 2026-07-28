# Architecture

**Status:** Draft v0.2

> This document describes the architectural structure of QA Forge.
>
> It defines the stable architectural concepts that shape the platform and explains how engineering knowledge flows through the system.
>
> Implementation details are intentionally omitted.
>
> The architecture is expected to evolve together with the platform.

---

# Architectural Philosophy

QA Forge is designed as an engineering knowledge platform.

Its primary purpose is not to execute engineering tasks but to capture, organize and expose engineering knowledge in a form that can be understood by both humans and AI systems.

Every architectural component exists to answer a different engineering question.

Engineering knowledge is considered the primary architectural asset.

---

# Architectural Layers

QA Forge separates engineering concerns into distinct conceptual layers.

```
Vision
    ↓
Architecture
    ↓
Engineering Models
    ↓
Engineering Cases
    ↓
Reference Implementations
```

Each layer builds upon the previous one.

Lower layers should never redefine concepts established above them.

Instead, they demonstrate and refine them.

---

# Runtime Architecture

The runtime architecture follows the flow of engineering knowledge.

```
Repository
        ↓
Knowledge Extraction
        ↓
Canonical Knowledge Model
        ↓
Knowledge Store
        ↓
Knowledge API
        ↓
Clients
```

Engineering knowledge is extracted once.

Every consumer reuses the same knowledge.

Clients may include:

- AI assistants
- MCP servers
- Documentation tools
- Engineering reviews
- Future integrations

The architecture intentionally separates engineering knowledge from the protocols used to access it.

---

# Architectural Principles

## Knowledge First

Engineering knowledge is the primary architectural asset.

Repositories, programming languages, AI models and communication protocols are interchangeable interfaces around that knowledge.

---

## Technology Agnostic

Engineering knowledge should remain valuable even when technologies evolve.

No architectural decision should depend on a specific programming language, framework or AI provider.

---

## Separation of Concerns

The platform separates:

- Knowledge extraction
- Knowledge representation
- Knowledge storage
- Knowledge access
- Client integrations

Each component has a single architectural responsibility.

---

## Incremental Evolution

Architecture is expected to evolve.

Large architectural changes should be documented through Architectural Decision Records (ADRs).

---

# Core Components

## Repository

Contains engineering artifacts.

Examples:

- Vision
- Architecture
- ADRs
- Engineering Models
- Engineering Cases
- Standards
- Reference Implementations
- Source Code

The repository is the source of engineering knowledge.

---

## Knowledge Extraction

Extractors convert engineering artifacts into structured knowledge.

Extractors are technology-specific.

Examples include:

- Markdown Extractor
- Java Extractor
- Python Extractor
- Spring Extractor
- GitHub Extractor

Extractors should never contain engineering business logic.

Their only responsibility is translating artifacts into the canonical knowledge model.

---

## Canonical Knowledge Model

The Canonical Knowledge Model represents engineering knowledge independently from its source.

Typical concepts include:

- Entity
- Relation
- Decision
- Constraint
- Standard
- Pattern
- Risk
- Dependency
- Component

Every extractor produces the same model.

---

## Knowledge Store

The Knowledge Store contains normalized engineering knowledge.

It enables consistent reasoning regardless of where the knowledge originated.

The storage implementation may evolve without affecting higher architectural layers.

---

## Knowledge API

The Knowledge API exposes engineering knowledge to clients.

Examples include:

- MCP
- REST
- GraphQL
- CLI
- Future interfaces

The API should expose knowledge rather than implementation details.

---

## Clients

Clients consume engineering knowledge.

Examples include:

- AI Assistants
- IDE Extensions
- Documentation Tools
- Review Engines
- Future Engineering Platforms

Clients should never need to understand repository internals.

---

# Documentation

Documentation explains the platform.

Documentation itself is part of the engineering knowledge.

Documents describe:

- Vision
- Architecture
- Decisions
- Models
- Standards

Together they provide the context required to understand the platform.

---

# Design Principles

The platform follows several guiding principles.

## Engineering Before Technology

Engineering principles outlive technologies.

Technology serves engineering rather than defining it.

---

## Single Source of Truth

Engineering knowledge should exist once.

Multiple clients should consume the same knowledge instead of rebuilding context independently.

---

## Reusable Knowledge

Engineering decisions should become reusable artifacts.

Knowledge created for one repository should be applicable elsewhere whenever possible.

---

## Explainability

Every architectural decision should be understandable.

The platform should optimize for reasoning rather than complexity.

---

## Evolution

Architecture is expected to evolve.

Major architectural changes should be documented using ADRs.

---

# Future Architecture

Future architectural evolution may include:

- Knowledge Graphs
- Engineering Ontologies
- AI Reasoning Engines
- Distributed Knowledge Stores
- Repository Federation
- Engineering Analytics

Future additions should preserve the architectural principles defined in this document.

---

# Architecture Review

This document should be reviewed after every significant architectural milestone.

Review questions:

- Does the architecture still reflect the Vision?
- Is engineering knowledge still the architectural center?
- Are responsibilities clearly separated?
- Can new technologies be integrated without changing the Core?
- Does every repository still contribute to the shared knowledge model?

Architecture is considered a living engineering artifact.