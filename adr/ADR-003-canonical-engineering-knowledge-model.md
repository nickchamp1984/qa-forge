# ADR-003

# Canonical Engineering Knowledge Model

**Status:** Accepted

---

# Context

QA Forge is designed as an Engineering Knowledge Platform.

Engineering knowledge originates from many different sources, including:

- Vision documents
- Architectural documentation
- ADRs
- Engineering standards
- Source code
- Repository metadata
- External engineering systems

These artifacts differ in format and structure, yet they all describe engineering knowledge.

If every extractor produces its own internal representation, the Core becomes tightly coupled to specific technologies and document formats.

The platform requires a single canonical representation that is independent of the original source.

---

# Decision

QA Forge adopts a Canonical Engineering Knowledge Model.

The Core operates exclusively on canonical entities and relations.

Source-specific concepts are translated into the canonical model by extractors.

The Core never processes Markdown, Java, GitHub, or other technologies directly.

Instead, it processes engineering knowledge expressed through a shared representation.

---

# Canonical Concepts

The Canonical Engineering Knowledge Model is intentionally minimal.

It defines only two fundamental concepts.

## Entity

Represents a meaningful engineering object.

Examples include:

- Vision
- Architecture
- ADR
- Component
- Service
- Repository
- Class
- Interface
- Standard
- Test
- Requirement

Entities describe *what exists*.

---

## Relation

Represents a relationship between two entities.

Examples include:

- CONTAINS
- REFERENCES
- IMPLEMENTS
- DEPENDS_ON
- JUSTIFIES
- SATISFIES
- DEFINES

Relations describe *how entities are connected*.

---

# Supporting Concepts

The following concepts support the knowledge model but are not part of its canonical ontology.

## Properties

Properties enrich entities without introducing new engineering concepts.

Examples include:

- Repository
- Author
- Version
- Timestamp
- Language
- Confidence

Properties provide additional context without changing the engineering meaning.

---

## Traceability

Engineering knowledge must remain traceable to its original source.

Typical sources include:

- Markdown document
- ADR
- Source code
- Commit
- Pull Request

Traceability is a platform capability rather than a canonical concept.

---

# Consequences

Positive:

- One internal representation for every engineering artifact.
- Extractors remain independent from the Core.
- New technologies require only new extractors.
- AI systems receive consistent engineering knowledge.
- Future reasoning engines operate on a stable model.

Negative:

- Initial modeling requires additional design effort.
- Extractors must translate source artifacts into the canonical model.
- The canonical model becomes an important long-term architectural asset.

---

# Related Documents

- Vision.md
- Architecture.md
- ADR-001 Knowledge Layer as the Core Architecture
- ADR-002 Repository Explains Itself to AI