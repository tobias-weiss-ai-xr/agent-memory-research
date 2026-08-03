# Related Work Analysis: Evolutionary Knowledge Graph Schema Adaptation

## Research Question
Can a knowledge graph schema evolve autonomously, modeled on biological evolution principles, where data patterns create selection pressure, an LLM acts as a directed mutation engine, and an epigenetic layer governs provisional vs. permanent schema changes?

## Methodology
Searched arXiv (20+ queries), agent-memory-research repo (1,047 papers), and Google Patents. Fetched full abstracts for 15 critical papers. Below: ranked relevance analysis.

---

## Tier 1: Directly Overlapping (Must Read — Highest Relevance)

### 1. SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory
- **arXiv**: 2605.12061v1 (May 2026)
- **Relevance**: ⭐⭐⭐⭐⭐ — MOST RELEVANT
- **Overlap**: SAGE models graph memory as a dynamic substrate with a "memory writer" that incrementally constructs structured graph memory and evolves it through downstream feedback. This is the closest existing work to our schema evolution concept.
- **Gap vs. our idea**: SAGE focuses on *associative memory retrieval* — evolving the graph *content* (connections, weights) for better retrieval. Our idea focuses on evolving the *schema itself* (entity types, relationship types, constraints). SAGE evolves the *phenotype*; we propose evolving the *genotype*.

### 2. MemPro: Agentic Memory Systems as Evolvable Programs
- **arXiv**: 2606.00619v1 (Jun 2026)
- **Relevance**: ⭐⭐⭐⭐⭐ — HIGHLY RELEVANT
- **Overlap**: MemPro treats the entire memory construction-retrieval pipeline as an "evolvable program" — components can be mutated, recombined, and selected. This directly parallels our genetic representation idea.
- **Gap vs. our idea**: MemPro evolves the *pipeline components* (extractor, indexer, retriever). We propose evolving the *schema/ontology* specifically, with biological mechanisms (epigenetic layer, homeostasis, speciation) that MemPro doesn't address.

### 3. Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems
- **arXiv**: 2605.04264v1 (May 2026)
- **Relevance**: ⭐⭐⭐⭐⭐ — CONCEPTUALLY KEY
- **Overlap**: Frames memory governance as a *selection regime* — which memories persist, become shared, or are rejected. This is directly analogous to natural selection on the schema level. Distinguishes natural/artificial selection on memory variants.
- **Gap vs. our idea**: This is a *viewpoint/design philosophy paper*, not a system implementation. They propose the framing but don't implement fitness functions, genetic representation, or epigenetic mechanisms.

### 4. Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents (DCPM)
- **arXiv**: 2606.09483v1 (Jun 2026)
- **Relevance**: ⭐⭐⭐⭐½ — HIGHLY RELEVANT
- **Overlap**: Reorganizes memory along a *cognitive capability hierarchy* ascending from atomic facts → diachronic belief trajectories → domain schemas → cross-domain patterns. The "domain schemas" layer is close to our schema evolution concept.
- **Gap vs. our idea**: DCPM has fixed hierarchy levels. Our schema evolution would dynamically *create new hierarchy levels* through speciation. DCPM is more about cognitive architecture; we add evolutionary dynamics.

### 5. FluxMem / Rethinking Memory as Continuously Evolving Connectivity
- **arXiv**: 2605.28773v1 (May 2026)
- **Relevance**: ⭐⭐⭐⭐½ — HIGHLY RELEVANT
- **Overlap**: Models memory as a heterogeneous graph that *progressively refines its topology* through feedback-driven refinement and long-term consolidation. Repairs missing links, prunes interference, aligns abstraction granularity.
- **Gap vs. our idea**: FluxMem evolves graph *topology* (edges/weights). We propose evolving the *type system* (node labels, relationship types, constraints) — a meta-level above topology evolution.

### 6. HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution
- **arXiv**: 2605.09942v1 (May 2026)
- **Relevance**: ⭐⭐⭐⭐ — RELEVANT
- **Overlap**: Uses reinforcement learning to evolve *edge weights* in a multi-relational memory graph. Each edge has a trainable relation feature vector encoding multiple relational signals.
- **Gap vs. our idea**: HAGE evolves *edge weights* via RL. We propose evolving the *schema types and constraints* — the structure that defines what edges can exist at all.

---

## Tier 2: Strongly Related (Important Context)

### 7. Prism: An Evolutionary Memory Substrate for Multi-Agent Open-Ended Discovery
- **arXiv**: 2604.19795v1 (Apr 2026)
- **Relevance**: ⭐⭐⭐⭐ — STRONG CONCEPTUAL OVERLAP
- **Overlap**: "Evolutionary memory substrate" — uses *entropy-gated stratification* to assign memories to skill/note/attempt hubs. Has eight interconnected subsystems under a decision-theoretic framework.
- **Gap vs. our idea**: Prism is about memory *classification and retrieval* for multi-agent discovery. Our schema evolution is about the *ontology/type system* that structures the graph itself.

### 8. Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback
- **arXiv**: 2602.02369v1 (Feb 2026)
- **Relevance**: ⭐⭐⭐⭐ — STRONG OVERLAP
- **Overlap**: Online self-evolving memory that learns from a *stream of incoming data*. Decouples "what happened" (Experience Bank) from "how to use it" (Method Bank).
- **Gap vs. our idea**: Live-Evo evolves *memories* (content). We evolve the *schema* (structure/type system). The Experience Bank → Method Bank split is interesting and could inspire our epigenetic layer.

### 9. SSGM Framework: Governing Evolving Memory in LLM Agents
- **arXiv**: 2603.11768v2 (Mar 2026)
- **Relevance**: ⭐⭐⭐½ — RELEVANT (GOVERNANCE)
- **Overlap**: Addresses *semantic drift* and memory corruption in dynamic environments. Proposes stability and safety constraints for evolving memory.
- **Gap vs. our idea**: SSGM focuses on *security/governance*. Our homeostatic regulation concept parallels their stability concerns but operates at the schema level rather than content level.

### 10. Memory as Metabolism: A Design for Companion Knowledge Systems
- **arXiv**: 2604.12034v1 (Apr 2026)
- **Relevance**: ⭐⭐⭐½ — CONCEPTUAL AFFINITY
- **Overlap**: Frames memory as a *metabolic process* — energy-efficient storage, processing, and retrieval. This is very close to our biological analogy.
- **Gap vs. our idea**: This is a design philosophy piece. It proposes the metabolic framing but doesn't implement schema evolution mechanisms.

### 11. From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents
- **arXiv**: 2607.00233v1 (Jul 2026)
- **Relevance**: ⭐⭐⭐½ — NICHE CONSTRUCTION PARALLEL
- **Overlap**: Studies how *memory architecture shapes emergent behavior* — the bidirectional feedback between structure and content. This parallels our niche construction feedback loop.

---

## Tier 3: Adjacent (Background Context)

### 12. SEVerA: Verified Synthesis of Self-Evolving Agents
- **arXiv**: 2603.25111v2 (Mar 2026)
- Self-evolving agents with formal verification. No schema evolution component.

### 13. Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense
- **arXiv**: 2606.05743 (Jun 2026)
- Self-evolving safety memory. Evolves defensive patterns, not schema.

### 14. Governed Memory: A Production Architecture for Multi-Agent Workflows
- **arXiv**: 2603.17787 (Mar 2026)
- Production memory governance. Identifies five structural challenges. No schema evolution.

### 15. To Know is to Construct: Schema-Constrained Generation for Agent Memory
- **arXiv**: 2604.20117 (Apr 2026)
- Schema-constrained memory generation. Fixed schema, not evolving.

---

## Patent Landscape

**Google Patents**: Could not be systematically crawled (JS-rendered). Manual search recommended for:
- "evolutionary knowledge graph schema adaptation"
- "self-evolving agent memory graph"
- "adaptive ontology evolution LLM"
- "epigenetic memory knowledge graph"

**Initial assessment**: No known patent directly covering *evolutionary knowledge graph schema adaptation with epigenetic provisional changes and homeostatic regulation*. The space is dominated by academic publications (2025-2026), with few if any patent applications yet. **Window of opportunity is open.**

---

## Gap Analysis

*(Detailed gap table removed for IP protection. See private repo for full analysis.)*

---

## Recommendation

1. **File quickly** — The space is exploding (all Tier 1 papers are from May-July 2026). Window of opportunity is narrow.
2. **See private repo for detailed strategic recommendations.**
