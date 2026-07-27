# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for QA Forge.

An ADR captures a significant architectural decision together with its context, rationale and consequences.

ADRs serve as historical records of architectural evolution.

## Principles

- ADRs describe architectural decisions, not implementation details.
- ADRs are immutable once accepted.
- If a decision changes, a new ADR supersedes the previous one.
- Every ADR should explain **why** the decision was made, not only **what** was decided.

## Standard Structure

Each ADR should contain:

- Status
- Context
- Decision
- Consequences
- Related Documents

Additional sections may be introduced when necessary.

## Naming

ADR files follow the convention:

ADR-XXX-short-kebab-case-title.md

Examples:

- ADR-001-knowledge-layer-as-the-core-architecture.md
- ADR-002-repository-explains-itself-to-ai.md

## Relationship to Other Documents

| Document | Purpose |
|----------|---------|
| Vision | Why the project exists |
| Architecture | How the platform is organized |
| ADR | Why a particular architectural decision was made |
| Engineering Models | Reusable engineering thinking |
| Engineering Cases | Analysis of real engineering situations |
| Reference Implementations | Practical implementation examples |