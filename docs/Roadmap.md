# Roadmap

**Status:** Draft v0.2

> This document describes the long-term evolution of QA Forge.
>
> It defines strategic engineering milestones rather than implementation details.
>
> The roadmap evolves together with the platform and reflects its architectural direction.

---

# Roadmap Philosophy

QA Forge evolves incrementally.

Every release should introduce a meaningful engineering capability.

Every Epic should move the platform closer to its long-term vision of becoming an AI-native engineering knowledge platform.

The roadmap is a planning artifact rather than a fixed commitment.

---

# Product Strategy

QA Forge evolves through three major stages.

## Stage 1 — Knowledge Foundation

The first milestone is creating a stable Engineering Knowledge Layer.

The Foundation includes:

- Engineering Documentation
- Knowledge Extraction
- Canonical Knowledge Model
- Knowledge Store
- Knowledge API

This stage establishes engineering knowledge as the central asset of the platform.

---

## Stage 2 — Engineering Services

Once the Knowledge Layer becomes stable, QA Forge introduces engineering services that consume the shared knowledge.

Examples include:

- Repository Navigation
- Engineering Review
- Documentation Services
- Architecture Review
- AI Context Generation

All services consume the same engineering knowledge.

---

## Stage 3 — Engineering Ecosystem

The final stage expands QA Forge through integrations and community contributions.

Examples include:

- MCP
- GitHub
- Jira
- TestRail
- Programming Language Toolkits
- IDE Extensions
- Community Packages

Integrations extend the platform without changing the Core.

---

# Versioning Strategy

QA Forge follows Semantic Versioning.

Major versions represent significant architectural milestones.

Minor versions introduce new engineering capabilities.

Patch versions improve existing capabilities without changing the architecture.

Engineering milestones are more important than release dates.

---

# Completed Milestones

## v0.1.x — Foundation

Completed:

- Vision
- Architecture
- Roadmap
- ADR Framework
- Architectural Decision Records
- Documentation conventions
- Initial repository structure
- Initial engineering direction

---

# Current Milestone

## Epic 3 — Knowledge Layer

Objective:

Build the Engineering Knowledge Layer that becomes the foundation of the entire platform.

The goal is to transform engineering artifacts into structured knowledge that can be reused by humans and AI alike.

---

# Planned Releases

## v0.2.0

Knowledge Model

Deliverables:

- Canonical Knowledge Model
- Core Entities
- Core Relations
- Initial architecture

---

## v0.2.1

Knowledge Extraction

Deliverables:

- Markdown Extractor
- Vision Extractor
- ADR Extractor
- Architecture Extractor

---

## v0.2.2

Knowledge Store

Deliverables:

- Internal representation
- Persistence layer
- Repository indexing
- Knowledge serialization

---

## v0.3.x

Knowledge API

Deliverables:

- Query API
- Search
- Entity navigation
- Relationship traversal

---

## v0.4.x

Engineering Services

Deliverables:

- Documentation Review
- Architecture Review
- Repository Review
- Knowledge Validation

---

## v0.5.x

MCP Adapter

Deliverables:

- MCP Server
- MCP Tools
- AI Context API
- AI Repository Navigation

At this stage MCP becomes one of several clients of the Knowledge API.

---

## v0.6.x

Repository Integrations

Examples:

- GitHub
- Git
- Playwright
- Java
- Python
- Spring

These integrations enrich the Knowledge Layer without modifying its architecture.

---

## v0.7.x

AI Engineering

Deliverables:

- AI Engineering Assistant
- Architecture Reasoning
- Engineering Recommendations
- Decision Support
- Repository Intelligence

---

# Long-Term Vision

QA Forge evolves from a documentation repository into an Engineering Knowledge Platform.

Engineering knowledge is extracted once.

It is represented using a canonical model.

Every engineering service, AI assistant and integration consumes the same shared knowledge.

Knowledge becomes the stable foundation.

Technologies become interchangeable adapters.

---

# Success Criteria

The roadmap is successful when:

- Engineering knowledge is independent of repository structure.
- New technologies integrate without changing the Core.
- AI systems consume the same engineering knowledge as humans.
- Engineering decisions become reusable assets.
- Repository intelligence is generated rather than manually recreated.

---

# Roadmap Review

This roadmap should be reviewed after every major milestone.

Review questions:

- Does the roadmap still support the Vision?
- Does it remain aligned with the Architecture?
- Has a new architectural capability emerged?
- Should priorities change?
- Are engineering knowledge and reasoning still the platform's primary focus?

The roadmap is considered a living engineering artifact.