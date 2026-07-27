# ADR-002 — Repository Explains Itself to AI

**Status:** Accepted

**Date:** 2026-07-26

---

# Context

Large Language Models possess strong reasoning capabilities but no persistent understanding of individual software projects.

Without additional architectural support, every AI session requires the repository to be analyzed again in order to reconstruct project context.

This creates repeated work, inconsistent interpretations and unnecessary dependency on prompt engineering.

As QA Forge evolved, it became clear that repository understanding should not be reconstructed by every AI session independently.

---

# Decision

QA Forge adopts the following architectural principle:

> **A repository should explain itself once to AI instead of AI relearning it every session.**

Engineering knowledge is extracted from repository artifacts and represented in a structured form that can be consumed by any AI client.

The responsibility for describing the project belongs to the repository through the Knowledge Layer, not to the AI model.

---

# Consequences

## Positive

- Engineering context becomes deterministic.
- AI sessions become faster and more consistent.
- Repository knowledge survives changes of AI providers.
- Engineering documentation gains executable value.
- AI reasoning focuses on engineering decisions rather than repository exploration.

## Negative

- Repository metadata becomes part of the engineering process.
- Knowledge extraction quality directly affects AI performance.
- Repository maintainers assume additional responsibility for knowledge quality.

---

# Design Principle

Repository artifacts should answer questions such as:

- What does this system do?
- Why was this decision made?
- Which components are related?
- Which business concepts exist?
- Which architectural constraints apply?
- Which risks are already known?

The AI should consume these answers instead of inferring them repeatedly.

---

# Philosophy

Engineering knowledge is the long-lived asset.

Repositories evolve.

Programming languages evolve.

AI models evolve.

Engineering knowledge remains.

---

# Related Documents

- Vision
- Architecture
- ADR-001