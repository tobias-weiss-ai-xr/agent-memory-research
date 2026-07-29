<h1 align="center">
  <strong>Agent Memory Paper List</strong>
</h1>
<h3 align="center">A data-driven, auto-validated reading list for Agent Memory research</h3>

<div align="center">

[![Survey Paper (Original)](https://img.shields.io/badge/Survey_%28Original%29-2512.13564-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2512.13564)
[![Hugging Face (Original)](https://img.shields.io/badge/HF_%28Original%29-2512.13564-292929.svg?logo=huggingface)](https://huggingface.co/papers/2512.13564)
[![Survey Paper (Extended)](https://img.shields.io/badge/Survey_%28Extended%29-10.5281%2Fzenodo.20780690-004D40.svg?logo=zenodo)](https://doi.org/10.5281/zenodo.20780690)
[![Dataset](https://img.shields.io/badge/Dataset-10.5281%2Fzenodo.20780696-004D40.svg?logo=zenodo)](https://doi.org/10.5281/zenodo.20780696)
[![GitHub](https://img.shields.io/badge/GitHub-tobias--weiss--ai--xr/agent--memory--research-181717.svg?logo=github)](https://github.com/tobias-weiss-ai-xr/agent-memory-research)
[![Codeberg](https://img.shields.io/badge/Codeberg-graphwiz--ai/agent--memory--research-2185D0.svg?logo=codeberg)](https://codeberg.org/graphwiz-ai/agent-memory-research)
[![GitHub Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-brightgreen.svg?logo=github)](https://tobias-weiss-ai-xr.github.io/agent-memory-research/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/tobias-weiss-ai-xr/agent-memory-research/validate.yml?label=CI&logo=github)](https://github.com/tobias-weiss-ai-xr/agent-memory-research/actions/workflows/validate.yml)
[![Benchmark](https://img.shields.io/badge/Benchmark-AMBench-004D40.svg?logo=github)](https://github.com/tobias-weiss-ai-xr/agent-memory-bench)
[![Agentic VR Survey](https://img.shields.io/badge/Agentic_VR_Survey-004D40.svg?logo=arxiv)](https://github.com/tobias-weiss-ai-xr/agentic-vr-research)
[![Skill Survey](https://img.shields.io/badge/Skill_Survey-004D40.svg?logo=github)](https://github.com/tobias-weiss-ai-xr/agent-skill-research)
[![Skill Bench](https://img.shields.io/badge/Skill_Bench-004D40.svg?logo=github)](https://github.com/tobias-weiss-ai-xr/agent-skill-bench)

</div>

## 🙏 Credits & Acknowledgments

This repository is a refactored fork of [Shichun-Liu/Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List), originally created by the authors of the survey *"Memory in the Age of AI Agents: A Survey"* (arXiv 2512.13564).

All credit for the paper list, taxonomy, and survey belongs to the original authors:
- **Original repo**: [Shichun-Liu/Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) (EvoAgentX)
- **Survey paper**: [Memory in the Age of AI Agents: A Survey](https://arxiv.org/abs/2512.13564)

This fork adds:
- **Data-driven architecture**: Papers stored in `papers.yaml`, README auto-generated via `scripts/generate_readme.py`
- **Automated validation**: CI checks for duplicates, URL normalization, format compliance
- **Metadata enrichment**: Scripts to fetch authors/venue/abstract from arXiv and Semantic Scholar
- **New paper discovery**: Automated arXiv search for recent agent memory papers
- **Interactive browsing**: GitHub Pages site with client-side filtering and search
- **Contributor guardrails**: CONTRIBUTING.md, issue/PR templates, URL normalization rules

## 📢 News
- [2026/07] 📄 **Extended survey revised!** Updated to 1,047 papers (593 since Feb 2026). Added two new theme clusters (security/adversarial robustness, efficiency/compression) to the taxonomy. See [paper/main.pdf](paper/main.pdf) — 18 pages
- [2026/07] 📚 **Added 83 new papers!** Discovered via arXiv API queries for ``agent memory'', ``memory system'' agent, and ``long-term memory'' agent. Now 1,047 entries.
- [2026/07] 📚 **Added 787 new papers!** Discovered via 200+ arXiv API queries, OpenAlex, CrossRef, and Semantic Scholar citation networks across 16 search rounds. Now 953 entries (896 unique arXiv papers).
- [2026/07] 📚 **Added 357 new papers!** Discovered via 100+ arXiv API queries across 13 search rounds covering memory architectures, security, benchmarks, consolidation, forgetting, embodied agents, prospective memory, and July 2026 releases. Now 616 entries (573 unique arXiv papers).
- [2026/06] 📄 **Extended survey released!** See [Agent Memory Research in 2026: A Data-Driven Survey and Extended Taxonomy](paper/main.pdf) — 19 pages, 259 papers, expanded 6-dimension taxonomy
- [2026/06] 🔧 Refactored to data-driven architecture: `papers.yaml` → `generate_readme.py` → `README.md`
- [2026/06] 🤖 Added automation: paper validator, metadata fetcher, new paper discovery
- [2026/06] 🌐 Added GitHub Pages site with filtering by category, date, and keyword search
- [2026/06] ✅ Added CI validation, CONTRIBUTING.md, and issue/PR templates
- [2026/01/29] 🎉 Original repository reached **1k stars**!
- [2025/12/16] 📄 Original survey released! See [Memory in the Age of AI Agents: A Survey](https://arxiv.org/abs/2512.13564)


<div align="center">
  <img src="assets/main.png" alt="Overview of agent memory organized by the unified taxonomy" width="80%" />
  <p><em><strong>Figure:</strong> Overview of agent memory organized by the unified taxonomy of <strong>forms</strong>, <strong>functions</strong>, and <strong>dynamics</strong>. <em>(From the original survey)</em></em></p>
</div>

## 👋 Introduction

Memory serves as the cornerstone of foundation model-based agents, underpinning their ability to perform long-horizon reasoning, adapt continually, and interact effectively with complex environments.

Despite the explosion of research in this field, the landscape remains highly fragmented, with loosely defined terminologies and inconsistent taxonomies. The original survey bridges this gap by distinguishing Agent Memory from related concepts like RAG and Context Engineering, and providing a comprehensive overview through three unified lenses:

- **Forms** (What Carries Memory?): Categorizing memory by its storage medium—Token-level (explicit & discrete), Parametric (implicit weights), and Latent (hidden states).
- **Functions** (Why Agents Need Memory?): Moving beyond simple temporal divisions to a functional taxonomy: Factual (knowledge), Experiential (insights & skills), and Working Memory (active context management).
- **Dynamics** (How Memory Evolves?): Dissecting the operational lifecycle into Formation (extraction), Evolution (consolidation & forgetting), and Retrieval (access strategies).

This fork maintains the same taxonomy but makes the paper list **data-driven and auto-validated**. Papers are stored in [`papers.yaml`](papers.yaml) as structured data, and the README is generated by [`scripts/generate_readme.py`](scripts/generate_readme.py). See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to add papers.

## 💡 Concepts

<div align="center">
<img src="assets/concept.png" alt="Conceptual Comparison" width="80%" />
  <p><em><strong>Figure:</strong> Conceptual comparison of <strong>Agent Memory</strong> with <strong>LLM Memory</strong>, <strong>RAG</strong>, and <strong>Context Engineering</strong>. <em>(From the original survey)</em></em></p>
</div>

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Concepts](#-concepts)
- [Paper List](#-paper-list)
- [Related Projects](#-related-projects)
- [Citation](#-citation)

## 🔗 Quick Links

- [papers.yaml](papers.yaml)
- [docs/papers.json](docs/papers.json)
- [paper/main.pdf](paper/main.pdf)
- [CONTRIBUTING.md](CONTRIBUTING.md)

> [!NOTE]
> This list is auto-generated from [papers.yaml](papers.yaml). See [CONTRIBUTING.md](CONTRIBUTING.md) to add papers.


## 📚 Paper list

- [📚 Factual Memory](#factual-memory)
  - [Token-level](#token-level)
  - [Parametric](#parametric)
  - [Latent](#latent)
- [📚 Experiential Memory](#experiential-memory)
  - [Token-level](#token-level)
  - [Parametric](#parametric)
  - [Latent](#latent)
- [📚 Working Memory](#working-memory)
  - [Token-level](#token-level)
  - [Parametric](#parametric)
  - [Latent](#latent)

### Factual Memory

#### Token-level

##### 2026

- [2026] **CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning** [[paper](https://arxiv.org/abs/2607.20553)]
- [2026] **When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents** [[paper](https://arxiv.org/abs/2607.06595)]
- [2026] **Learning User-Aware Recall: Personalized Retrieval in Long-Term Conversational Memory** [[paper](https://arxiv.org/abs/2607.00017)]
- [2026] **MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations** [[paper](https://arxiv.org/abs/2607.12893)]
- [2026] **RUMBA: Russian User Memory Benchmark** [[paper](https://arxiv.org/abs/2607.21447)]
- [2026] **Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems** [[paper](https://arxiv.org/abs/2607.14611)]
- [2026] **The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI** [[paper](https://arxiv.org/abs/2607.19433)]
- [2026] **MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents** [[paper](https://arxiv.org/abs/2607.14651)]
- [2026] **When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents** [[paper](https://arxiv.org/abs/2607.05189)]
- [2026] **Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory** [[paper](https://arxiv.org/abs/2607.05029)]
- [2026] **Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents** [[paper](https://arxiv.org/abs/2607.15657)]
- [2026] **Stigmergic Graph Memory: An Environment-Aware Approach for Many-to-Many Multi-Agent Pickup and Delivery** [[paper](https://arxiv.org/abs/2607.15182)]
- [2026] **Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents** [[paper](https://arxiv.org/abs/2607.08448)]
- [2026] **ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control** [[paper](https://arxiv.org/abs/2607.22962)]
- [2026] **From Cognitive Architectures to Language Agents: A Mechanism-Level Review of Lineage, Convergence, and Migration Gaps** [[paper](https://arxiv.org/abs/2607.23942)]
- [2026] **Isolated but Exposed: Persistence-Based Memory Extraction Attack on LLM Agents** [[paper](https://arxiv.org/abs/2607.23444)]
- [2026] **Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory** [[paper](https://arxiv.org/abs/2606.10677)]
- [2026] **RaMem: Contextual Reinstatement for Long-term Agentic Memory** [[paper](https://arxiv.org/abs/2606.22844)] [[code](https://github.com/weiyang930/RaMem-Release.git)]
- [2026] **MemProbe: Probing Long-Term Agent Memory via Hidden User-State Recovery** [[paper](https://arxiv.org/abs/2606.24595)] [[code](https://github.com/sora1998/MemProbe)]
- [2026] **Are We Ready For An Agent-Native Memory System?** [[paper](https://arxiv.org/abs/2606.24775)]
- [2026] **Rosetta Memory: Adaptive Memory for Cross-LLM Agents** [[paper](https://arxiv.org/abs/2606.07711)]
- [2026] **GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge** [[paper](https://arxiv.org/abs/2606.14470)]
- [2026] **MemPro: Agentic Memory Systems as Evolvable Programs** [[paper](https://arxiv.org/abs/2606.00619)]
- [2026] **AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents** [[paper](https://arxiv.org/abs/2606.21144)]
- [2026] **MemToolAgent: Leveraging Memory for Tool Using Agents Based on Environment and User Feedback** [[paper](https://arxiv.org/abs/2606.07909)]
- [2026] **TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory** [[paper](https://arxiv.org/abs/2606.25161)]
- [2026] **Mandol: An Agglomerative Agent Memory System for Long-Term Conversations** [[paper](https://arxiv.org/abs/2606.29778)]
- [2026] **AdaMEM: Test-Time Adaptive Memory for Language Agents** [[paper](https://arxiv.org/abs/2606.05684)]
- [2026] **Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads** [[paper](https://arxiv.org/abs/2606.06448)]
- [2026] **Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents** [[paper](https://arxiv.org/abs/2606.09483)]
- [2026] **MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide Generation** [[paper](https://arxiv.org/abs/2606.17162)]
- [2026] **MemTrain: Self-Supervised Context Memory Training** [[paper](https://arxiv.org/abs/2606.03197)]
- [2026] **Staying In Character: Perspective-Bounded Memory For Book-Based Role-Playing Agents** [[paper](https://arxiv.org/abs/2606.25632)]
- [2026] **AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts** [[paper](https://arxiv.org/abs/2606.19847)]
- [2026] **PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents** [[paper](https://arxiv.org/abs/2606.04780)]
- [2026] **T-Mem: Memory That Anticipates, Not Archives** [[paper](https://arxiv.org/abs/2606.15405)]
- [2026] **Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory** [[paper](https://arxiv.org/abs/2606.12945)]
- [2026] **Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations** [[paper](https://arxiv.org/abs/2606.15903)]
- [2026] **REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs** [[paper](https://arxiv.org/abs/2606.10694)]
- [2026] **Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents** [[paper](https://arxiv.org/abs/2606.25361)]
- [2026] **Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents** [[paper](https://arxiv.org/abs/2606.27472)]
- [2026] **GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents** [[paper](https://arxiv.org/abs/2606.18829)]
- [2026] **CoreMem: Riemannian Retrieval and Fisher-Guided Distillation for Long-Term Memory in Dialogue Agents** [[paper](https://arxiv.org/abs/2606.18406)]
- [2026] **Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense** [[paper](https://arxiv.org/abs/2606.05743)]
- [2026] **Selective Memory Retention for Long-Horizon LLM Agents** [[paper](https://arxiv.org/abs/2606.29178)]
- [2026] **Towards Persistent Case-Based Memory for Autonomous Data Science: A CBR-Augmented R&D-Agent with a Locally Deployable Small Language Model** [[paper](https://arxiv.org/abs/2606.05250)]
- [2026] **Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees** [[paper](https://arxiv.org/abs/2606.24322)]
- [2026] **User as Code: Executable Memory for Personalized Agents** [[paper](https://arxiv.org/abs/2606.16707)]
- [2026] **Code Isn't Memory: A Structural Codebase Index Inside a Coding Agent** [[paper](https://arxiv.org/abs/2606.22417)]
- [2026] **PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents** [[paper](https://arxiv.org/abs/2606.12329)]
- [2026] **ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents** [[paper](https://arxiv.org/abs/2606.23752)]
- [2026] **Multi-Agent Transactive Memory** [[paper](https://arxiv.org/abs/2606.19911)]
- [2026] **Governed Shared Memory for Multi-Agent LLM Systems** [[paper](https://arxiv.org/abs/2606.24535)]
- [2026] **DMF: A Deterministic Memory Framework for Conversational AI Agents** [[paper](https://arxiv.org/abs/2606.03463)]
- [2026] **MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA** [[paper](https://arxiv.org/abs/2606.05749)]
- [2026] **From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents** [[paper](https://arxiv.org/abs/2607.00233)]
- [2026] **Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge** [[paper](https://arxiv.org/abs/2606.26511)]
- [2026] **G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents** [[paper](https://arxiv.org/abs/2606.13115)]
- [2026] **Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles** [[paper](https://arxiv.org/abs/2607.19359)]
- [2026] **SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems** [[paper](https://arxiv.org/abs/2606.12703)]
- [2026] **TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory** [[paper](https://arxiv.org/abs/2606.06240)]
- [2026] **Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning** [[paper](https://arxiv.org/abs/2606.20954)]
- [2026] **Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents** [[paper](https://arxiv.org/abs/2606.08151)]
- [2026] **Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents** [[paper](https://arxiv.org/abs/2606.06090)]
- [2026] **What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems** [[paper](https://arxiv.org/abs/2606.04425)]
- [2026] **Beyond Similarity: Trustworthy Memory Search for Personal AI Agents** [[paper](https://arxiv.org/abs/2606.06054)]
- [2026] **From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents** [[paper](https://arxiv.org/abs/2606.04329)]
- [2026] **RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation** [[paper](https://arxiv.org/abs/2606.04628)]
- [2026] **Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering** [[paper](https://arxiv.org/abs/2606.29030)]
- [2026] **Trust-Aware Multi-Agent Traceability: Confidence-Calibrated Knowledge Graphs for Consistent Software Artifact Management** [[paper](https://arxiv.org/abs/2606.17203)]
- [2026] **AgentCL: Toward Rigorous Evaluation of Continual Learning in Language Agents** [[paper](https://arxiv.org/abs/2606.02461)]
- [2026] **MemForge: Portable, agent-neutral persistent memory format for AI coding agents (v0.8.1)** [[paper](https://doi.org/https://doi.org/10.5281/zenodo.20995032)]
- [2026] **HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution** [[paper](https://arxiv.org/abs/2605.09942)]
- [2026] **MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents** [[paper](https://arxiv.org/abs/2605.28046)]
- [2026] **Goal-Oriented Reasoning for RAG-based Memory in Conversational Agentic LLM Systems** [[paper](https://arxiv.org/abs/2605.12213)]
- [2026] **VikingMem: A Memory Base Management System for Stateful LLM-based Applications** [[paper](https://arxiv.org/abs/2605.29640)]
- [2026] **MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents** [[paper](https://arxiv.org/abs/2605.00356)]
- [2026] **PRISM: Pareto-Efficient Retrieval over Intent-Aware Structured Memory for Long-Horizon Agents** [[paper](https://arxiv.org/abs/2605.12260)]
- [2026] **NeuSymMS: A Hybrid Neuro-Symbolic Memory System for Persistent, Self-Curating LLM Agents** [[paper](https://arxiv.org/abs/2605.17596)]
- [2026] **MEMOREPAIR: Barrier-First Cascade Repair in Agentic Memory** [[paper](https://arxiv.org/abs/2605.07242)]
- [2026] **Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory** [[paper](https://arxiv.org/abs/2605.26252)]
- [2026] **RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents** [[paper](https://arxiv.org/abs/2605.16045)]
- [2026] **DimMem: Dimensional Structuring for Efficient Long-Term Agent Memory** [[paper](https://arxiv.org/abs/2605.15759)]
- [2026] **MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents** [[paper](https://arxiv.org/abs/2605.01386)]
- [2026] **Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory** [[paper](https://arxiv.org/abs/2605.19952)]
- [2026] **Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory** [[paper](https://arxiv.org/abs/2605.00702)]
- [2026] **Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents** [[paper](https://arxiv.org/abs/2605.20616)]
- [2026] **Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents** [[paper](https://arxiv.org/abs/2605.17641)]
- [2026] **GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations** [[paper](https://arxiv.org/abs/2605.14498)]
- [2026] **MemGym: a Long-Horizon Memory Environment for LLM Agents** [[paper](https://arxiv.org/abs/2605.20833)]
- [2026] **MemPrivacy: Privacy-Preserving Personalized Memory Management for Edge-Cloud Agents** [[paper](https://arxiv.org/abs/2605.09530)]
- [2026] **Agentic Recommender System with Hierarchical Belief-State Memory** [[paper](https://arxiv.org/abs/2605.14401)]
- [2026] **SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory** [[paper](https://arxiv.org/abs/2605.12061)]
- [2026] **Rethinking Memory as Continuously Evolving Connectivity** [[paper](https://arxiv.org/abs/2605.28773)]
- [2026] **GRAVITY: Architecture-Agnostic Structured Anchoring for Long-Horizon Conversational Memory** [[paper](https://arxiv.org/abs/2605.01688)]
- [2026] **AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational Memory** [[paper](https://arxiv.org/abs/2605.25092)]
- [2026] **BOOKMARKS: Efficient Active Storyline Memory for Role-playing** [[paper](https://arxiv.org/abs/2605.14169)]
- [2026] **STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?** [[paper](https://arxiv.org/abs/2605.06527)]
- [2026] **Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents** [[paper](https://arxiv.org/abs/2605.17830)]
- [2026] **MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution** [[paper](https://arxiv.org/abs/2605.23723)]
- [2026] **MEME: Multi-entity & Evolving Memory Evaluation** [[paper](https://arxiv.org/abs/2605.12477)]
- [2026] **ENPMR-Bench: Benchmarking Proactive Memory Retrieval for Emotional Support Agents** [[paper](https://arxiv.org/abs/2605.27240)]
- [2026] **Mem-Pi: Adaptive Memory through Learning When and What to Generate** [[paper](https://arxiv.org/abs/2605.21463)]
- [2026] **From Facts to Insights: A Persona-Driven Dual Memory Framework and Dataset for Role-Playing Agents** [[paper](https://arxiv.org/abs/2605.25693)]
- [2026] **MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval** [[paper](https://arxiv.org/abs/2605.06132)]
- [2026] **Learning to Retrieve: Dual-Level Long-Term Memory for Text-to-SQL Agents** [[paper](https://arxiv.org/abs/2606.00547)]
- [2026] **SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs** [[paper](https://arxiv.org/abs/2605.30711)]
- [2026] **Hidden in Memory: Sleeper Memory Poisoning in LLM Agents** [[paper](https://arxiv.org/abs/2605.15338)]
- [2026] **MemLineage: Lineage-Guided Enforcement for LLM Agent Memory** [[paper](https://arxiv.org/abs/2605.14421)]
- [2026] **Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents** [[paper](https://arxiv.org/abs/2605.21768)]
- [2026] **MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning** [[paper](https://arxiv.org/abs/2605.26154)]
- [2026] **Accurate and Efficient Long-Term Memory for LLM Agents** [[paper](https://arxiv.org/abs/2607.16211)]
- [2026] **Eywa: Provenance-Grounded Long-Term Memory for AI Agents** [[paper](https://arxiv.org/abs/2605.30771)]
- [2026] **MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems** [[paper](https://arxiv.org/abs/2605.25002)]
- [2026] **Tree-based Credit Assignment for Multi-Agent Memory System** [[paper](https://arxiv.org/abs/2605.04811)]
- [2026] **Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems** [[paper](https://arxiv.org/abs/2605.04264)]
- [2026] **MMoA: An AI-Agent framework with recurrence for Memoried Mixure-of-Agent** [[paper](https://arxiv.org/abs/2605.19194)]
- [2026] **Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall** [[paper](https://arxiv.org/abs/2605.04897)]
- [2026] **Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents** [[paper](https://arxiv.org/abs/2605.17625)]
- [2026] **Defense effectiveness across architectural layers: a mechanistic evaluation of persistent memory attacks on stateful LLM agents** [[paper](https://arxiv.org/abs/2605.08442)]
- [2026] **MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents** [[paper](https://arxiv.org/abs/2605.03482)]
- [2026] **ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts** [[paper](https://arxiv.org/abs/2605.09033)]
- [2026] **FundaPod: A Multi-Persona Agent Pod Platform with Knowledge Graph Memory for AI-Assisted Fundamental Investment Research** [[paper](https://arxiv.org/abs/2605.27864)]
- [2026] **State Contamination in Memory-Augmented LLM Agents** [[paper](https://arxiv.org/abs/2605.16746)]
- [2026] **Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration** [[paper](https://arxiv.org/abs/2605.01970)]
- [2026] **When Routine Chats Turn Toxic: Unintended Long-Term State Poisoning in Personalized Agents** [[paper](https://arxiv.org/abs/2605.06731)]
- [2026] **Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction** [[paper](https://arxiv.org/abs/2605.29960)]
- [2026] **AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle** [[paper](https://arxiv.org/abs/2605.31468)]
- [2026] **OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences** [[paper](https://arxiv.org/abs/2605.18930)]
- [2026] **SafeHarbor: Defining Precise Decision Boundaries via Hierarchical Memory-Augmented Guardrail for LLM Agent Safety** [[paper](https://arxiv.org/abs/2605.05704)]
- [2026] **Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation** [[paper](https://arxiv.org/abs/2605.25869)]
- [2026] **Belief Memory: Agent Memory Under Partial Observability** [[paper](https://arxiv.org/abs/2605.05583)]
- [2026] **Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework** [[paper](https://arxiv.org/abs/2604.01707)]
- [2026] **Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering** [[paper](https://arxiv.org/abs/2604.08224)]
- [2026] **Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents** [[paper](https://arxiv.org/abs/2604.22085)]
- [2026] **OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory** *ACL 2026* [[paper](https://arxiv.org/abs/2604.26622)]
- [2026] **MemSearch-o1: Empowering Large Language Models with Reasoning-Aligned Memory Growth in Agentic Search** *ACL 2026* [[paper](https://arxiv.org/abs/2604.17265)]
- [2026] **Hierarchical Memory Orchestration for Personalized Persistent Agents** [[paper](https://arxiv.org/abs/2604.01670)]
- [2026] **Opal: Private Memory for Personal AI** [[paper](https://arxiv.org/abs/2604.02522)]
- [2026] **HiGMem: A Hierarchical and LLM-Guided Memory System for Long-Term Conversational Agents** [[paper](https://arxiv.org/abs/2604.18349)]
- [2026] **ContextWeaver: Selective and Dependency-Structured Memory Construction for LLM Agents** [[paper](https://arxiv.org/abs/2604.23069)]
- [2026] **Synthius-Mem: Brain-Inspired Hallucination-Resistant Persona Memory Achieving 94.4% Memory Accuracy** [[paper](https://arxiv.org/abs/2604.11563)]
- [2026] **A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle** [[paper](https://arxiv.org/abs/2604.16548)]
- [2026] **HyperMem: Hypergraph Memory for Long-Term Conversations** [[paper](https://arxiv.org/abs/2604.08256)]
- [2026] **GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs** [[paper](https://arxiv.org/abs/2604.23626)]
- [2026] **From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents** [[paper](https://arxiv.org/abs/2604.20006)]
- [2026] **APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI** [[paper](https://arxiv.org/abs/2604.14362)]
- [2026] **To Know is to Construct: Schema-Constrained Generation for Agent Memory** [[paper](https://arxiv.org/abs/2604.20117)]
- [2026] **Mesh Memory Protocol: Semantic Infrastructure for Multi-Agent LLM Systems** [[paper](https://arxiv.org/abs/2604.19540)]
- [2026] **MemEvoBench: Benchmarking Safety Risks from Memory Misevolution in LLM Agents** [[paper](https://arxiv.org/abs/2604.15774)]
- [2026] **PASK: Toward Intent-Aware Proactive Agents with Long-Term Memory** [[paper](https://arxiv.org/abs/2604.08000)]
- [2026] **Long-Term Memory for VLA-based Agents in Open-World Task Execution** [[paper](https://arxiv.org/abs/2604.15671)]
- [2026] **Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents** [[paper](https://arxiv.org/abs/2604.14004)]
- [2026] **Prism: An Evolutionary Memory Substrate for Multi-Agent Open-Ended Discovery** [[paper](https://arxiv.org/abs/2604.19795)]
- [2026] **Every Picture Tells a Dangerous Story: Memory-Augmented Multi-Agent Jailbreak Attacks on VLMs** [[paper](https://arxiv.org/abs/2604.12616)]
- [2026] **Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation on Tabular Data** [[paper](https://arxiv.org/abs/2604.20261)]
- [2026] **IMPACT-CYCLE: A Contract-Based Multi-Agent System for Claim-Level Supervisory Correction of Long-Video Semantic Memory** [[paper](https://arxiv.org/abs/2604.20136)]
- [2026] **Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge Graphs and Agentic Memory** [[paper](https://arxiv.org/abs/2604.11544)]
- [2026] **Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning** *https://doi.org/10.18653/v1/2026.acl-long.954* [[paper](https://arxiv.org/abs/2604.16966)]
- [2026] **Springdrift: An Auditable Persistent Runtime for LLM Agents with Case-Based Memory, Normative Safety, and Ambient Self-Perception** [[paper](https://arxiv.org/abs/2604.04660)]
- [2026] **Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance and Efficiency** [[paper](https://arxiv.org/abs/2604.02280)]
- [2026] **MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents** [[paper](https://arxiv.org/abs/2604.04853)]
- [2026] **ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying** [[paper](https://arxiv.org/abs/2604.09747)]
- [2026] **Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents** [[paper](https://arxiv.org/abs/2604.02623)]
- [2026] **Memory Intelligence Agent** [[paper](https://arxiv.org/abs/2604.04503)]
- [2026] **MEMRES: A Memory-Augmented Resolver with Confidence Cascade for Agentic Python Dependency Resolution** *https://doi.org/10.1145/3803437.3808242* [[paper](https://arxiv.org/abs/2604.16941)]
- [2026] **Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent** *https://doi.org/10.1145/3770855.3818432* [[paper](https://arxiv.org/abs/2604.26197)]
- [2026] **Trust, Lies, and Long Memories: Emergent Social Dynamics and Reputation in Multi-Round Avalon with LLM Agents** [[paper](https://arxiv.org/abs/2604.20582)]
- [2026] **Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms** [[paper](https://arxiv.org/abs/2604.21131)]
- [2026] **ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents** *https://doi.org/10.1145/3805621.3807648* [[paper](https://arxiv.org/abs/2604.10352)]
- [2026] **From Soliloquy to Agora: Memory-Enhanced LLM Agents with Decentralized Debate for Optimization Modeling** [[paper](https://arxiv.org/abs/2604.25847)]
- [2026] **HEEL: A State-Centric Autobiographical Memory Architecture for Persistent Agents — Beyond the Session-Centric Ontology** [[paper](https://doi.org/https://doi.org/10.5281/zenodo.19851563)]
- [2026] **Cross-Agent Memory Architecture with Contextual Coherence and Factually Grounded Multi-Agent System** [[paper](https://doi.org/https://doi.org/10.21203/rs.3.rs-9180420/v1)]
- [2026] **Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers** [[paper](https://arxiv.org/abs/2603.07670)]
- [2026] **Toward a Theory of Hierarchical Memory for Language Agents** [[paper](https://arxiv.org/abs/2603.21564)]
- [2026] **MemFactory: Unified Inference & Training Framework for Agent Memory** [[paper](https://arxiv.org/abs/2603.29493)]
- [2026] **Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework** [[paper](https://arxiv.org/abs/2603.11768)]
- [2026] **CLAG: Adaptive Memory Organization via Agent-Driven Clustering for Small Language Model Agents** [[paper](https://arxiv.org/abs/2603.15421)]
- [2026] **PERMA: Benchmarking Personalized Memory Agents via Event-Driven Preference and Realistic Task Environments** [[paper](https://arxiv.org/abs/2603.23231)]
- [2026] **Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead** [[paper](https://arxiv.org/abs/2603.10062)]
- [2026] **Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation** [[paper](https://arxiv.org/abs/2603.13017)]
- [2026] **AdaMem: Adaptive User-Centric Memory for Long-Horizon Dialogue Agents** [[paper](https://arxiv.org/abs/2603.16496)]
- [2026] **Adaptive Memory Admission Control for LLM Agents** [[paper](https://arxiv.org/abs/2603.04549)]
- [2026] **Semantic XPath: Structured Agentic Memory Access for Conversational AI** [[paper](https://arxiv.org/abs/2603.01160)]
- [2026] **MemArchitect: A Policy Driven Memory Governance Layer** [[paper](https://arxiv.org/abs/2603.18330)]
- [2026] **Cognis: Context-Aware Memory for Conversational AI Agents** [[paper](https://arxiv.org/abs/2604.19771)]
- [2026] **MemGround: Long-Term Memory Evaluation Kit for Large Language Models in Gamified Scenarios** [[paper](https://arxiv.org/abs/2604.14158)]
- [2026] **MemCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization** [[paper](https://arxiv.org/abs/2603.25973)]
- [2026] **Governed Memory: A Production Architecture for Multi-Agent Workflows** [[paper](https://arxiv.org/abs/2603.17787)]
- [2026] **PersonaVLM: Long-Term Personalized Multimodal LLMs** [[paper](https://arxiv.org/abs/2604.13074)]
- [2026] **EchoGuard: An Agentic Framework with Knowledge-Graph Memory for Detecting Manipulative Communication in Longitudinal Dialogue** [[paper](https://arxiv.org/abs/2603.04815)]
- [2026] **Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents** [[paper](https://arxiv.org/abs/2603.19935)]
- [2026] **SuperLocalMemory V3: Information-Geometric Foundations for Zero-LLM Enterprise Agent Memory** *https://doi.org/10.5281/zenodo.19038659* [[paper](https://arxiv.org/abs/2603.14588)]
- [2026] **D-Mem: A Dual-Process Memory System for LLM Agents** [[paper](https://arxiv.org/abs/2603.18631)]
- [2026] **Chronos: Temporal-Aware Conversational Agents with Structured Event Retrieval for Long-Term Memory** [[paper](https://arxiv.org/abs/2603.16862)]
- [2026] **Multi-Agent Debate with Memory Masking** [[paper](https://arxiv.org/abs/2603.20215)]
- [2026] **Memory poisoning and secure multi-agent systems** [[paper](https://arxiv.org/abs/2603.20357)]
- [2026] **Joint Optimization of Multi-agent Memory System** [[paper](https://arxiv.org/abs/2603.12631)]
- [2026] **The Bureaucracy of Speed: Structural Equivalence Between Memory Consistency Models and Multi-Agent Authorization Revocation** [[paper](https://arxiv.org/abs/2603.09875)]
- [2026] **VeriAgent: A Tool-Integrated Multi-Agent System with Evolving Memory for PPA-Aware RTL Code Generation** [[paper](https://arxiv.org/abs/2603.17613)]
- [2026] **ChatNeuroSim: An LLM Agent Framework for Automated Compute-in-Memory Accelerator Deployment and Optimization** [[paper](https://arxiv.org/abs/2603.08745)]
- [2026] **Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures** [[paper](https://arxiv.org/abs/2603.17244)]
- [2026] **Persistent Identity in AI Agents: A Multi-Anchor Architecture for Resilient Memory and Continuity** [[paper](https://arxiv.org/abs/2604.09588)]
- [2026] **GAAMA: Graph Augmented Associative Memory for Agents** [[paper](https://arxiv.org/abs/2603.27910)]
- [2026] **Advancing Multimodal Agent Reasoning with Long-Term Neuro-Symbolic Memory** [[paper](https://arxiv.org/abs/2603.15280)]
- [2026] **Memory-Augmented Vision-Language Agents for Persistent and Semantically Consistent Object Captioning** [[paper](https://arxiv.org/abs/2603.24257)]
- [2026] **Knowledge Access Beats Model Size: Memory Augmented Routing for Persistent AI Agents** [[paper](https://arxiv.org/abs/2603.23013)]
- [2026] **Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents** [[paper](https://arxiv.org/abs/2603.04814)]
- [2026] **VoiceAgentRAG: Solving the RAG Latency Bottleneck in Real-Time Voice Agents Using Dual-Agent Architectures** [[paper](https://arxiv.org/abs/2603.02206)]
- [2026] **See and Remember: A Multimodal Agent for Web Traversal** [[paper](https://arxiv.org/abs/2603.02626)]
- [2026] **Trajectory-Informed Memory Generation for Self-Improving Agent Systems** [[paper](https://arxiv.org/abs/2603.10600)]
- [2026] **ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory** [[paper](https://doi.org/https://doi.org/10.1609/aaai.v40i30.39773)]
- [2026] **PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents** *ICML 2026* [[paper](https://arxiv.org/abs/2603.03296)]
- [2026] **Graph-based Agent Memory: Taxonomy, Techniques, and Applications** [[paper](https://arxiv.org/abs/2602.05665)]
- [2026] **Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey** [[paper](https://arxiv.org/abs/2602.06052)]
- [2026] **MemAdapter: Fast Alignment across Agent Memory Paradigms via Generative Subgraph Retrieval** [[paper](https://arxiv.org/abs/2602.08369)]
- [2026] **Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation** [[paper](https://arxiv.org/abs/2602.02007)]
- [2026] **Memora: A Harmonic Memory Representation Balancing Abstraction and Specificity** [[paper](https://arxiv.org/abs/2602.03315)]
- [2026] **MemFly: On-the-Fly Memory Optimization via Information Bottleneck** [[paper](https://arxiv.org/abs/2602.07885)]
- [2026] **HyMem: Hybrid Memory Architecture with Dynamic Retrieval Scheduling** [[paper](https://arxiv.org/abs/2602.13933)]
- [2026] **ActMem: Bridging the Gap Between Memory Retrieval and Reasoning in LLM Agents** [[paper](https://arxiv.org/abs/2603.00026)]
- [2026] **Hippocampus: An Efficient and Scalable Memory Module for Agentic AI** [[paper](https://arxiv.org/abs/2602.13594)]
- [2026] **AriadneMem: Threading the Maze of Lifelong Memory for LLM Agents** [[paper](https://arxiv.org/abs/2603.03290)]
- [2026] **VimRAG: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph** [[paper](https://arxiv.org/abs/2602.12735)]
- [2026] **MemPot: Defending Against Memory Extraction Attack with Optimized Honeypots** [[paper](https://arxiv.org/abs/2602.07517)]
- [2026] **Locomo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents** [[paper](https://arxiv.org/abs/2602.10715)]
- [2026] **Evaluating Long-Horizon Memory for Multi-Party Collaborative Dialogues** [[paper](https://arxiv.org/abs/2602.01313)]
- [2026] **MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks** [[paper](https://arxiv.org/abs/2602.16313)]
- [2026] **AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications** [[paper](https://arxiv.org/abs/2602.22769)]
- [2026] **Evaluating Memory Structure in LLM Agents** [[paper](https://arxiv.org/abs/2602.11243)]
- [2026] **TraceMem: Weaving Narrative Memory Schemata from User Conversational Traces** [[paper](https://arxiv.org/abs/2602.09712)]
- [2026] **Pancake: Hierarchical Memory System for Multi-Agent LLM Serving** [[paper](https://arxiv.org/abs/2602.21477)]
- [2026] **MemoPhishAgent: Memory-Augmented Multi-Modal LLM Agent for Phishing URL Detection** [[paper](https://arxiv.org/abs/2602.21394)]
- [2026] **REMem: Reasoning with Episodic Memory in Language Agent** [[paper](https://arxiv.org/abs/2602.13530)]
- [2026] **Your Code Agent Can Grow Alongside You with Structured Memory** [[paper](https://arxiv.org/abs/2603.13258)]
- [2026] **SuperLocalMemory: Privacy-Preserving Multi-Agent Memory with Bayesian Trust Defense Against Memory Poisoning** [[paper](https://arxiv.org/abs/2603.02240)]
- [2026] **MAPLE: A Sub-Agent Architecture for Memory, Learning, and Personalization in Agentic AI Systems** [[paper](https://arxiv.org/abs/2602.13258)]
- [2026] **AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management** [[paper](https://arxiv.org/abs/2602.07398)]
- [2026] **Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback** [[paper](https://arxiv.org/abs/2602.02369)]
- [2026] **Towards Autonomous Memory Agents** [[paper](https://arxiv.org/abs/2602.22406)]
- [2026] **AMEM4Rec: Leveraging Cross-User Similarity for Memory Evolution in Agentic LLM Recommenders** [[paper](https://arxiv.org/abs/2602.08837)]
- [2026] **Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning** [[paper](https://arxiv.org/abs/2601.04726)]
- [2026] **MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents** [[paper](https://arxiv.org/abs/2601.03236)]
- [2026] **EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning** [[paper](https://arxiv.org/abs/2601.02163)]
- [2026] **SimpleMem: Efficient Lifelong Memory for LLM Agents** *ICLR 2026* [[paper](https://arxiv.org/abs/2601.02553)]
- [2026] **MemWeaver: Weaving Hybrid Memories for Traceable Long-Horizon Agentic Reasoning** *Findings ACL 2026* [[paper](https://arxiv.org/abs/2601.18204)]
- [2026] **E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory** [[paper](https://arxiv.org/abs/2601.21714)]
- [2026] **SwiftMem: Fast Agentic Memory via Query-aware Indexing** [[paper](https://arxiv.org/abs/2601.08160)]
- [2026] **Grounding Agent Memory in Contextual Intent** [[paper](https://arxiv.org/abs/2601.10702)]
- [2026] **AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation** [[paper](https://arxiv.org/abs/2601.08323)]
- [2026] **AMA: Adaptive Memory via Multi-Agent Collaboration** [[paper](https://arxiv.org/abs/2601.20352)]
- [2026] **HiMeS: Hippocampus-inspired Memory System for Personalized AI Assistants** [[paper](https://arxiv.org/abs/2601.06152)]
- [2026] **Beyond Static Summarization: Proactive Memory Extraction for LLM Agents** [[paper](https://arxiv.org/abs/2601.04463)]
- [2026] **Membox: Weaving Topic Continuity into Long-Range Memory for LLM Agents** [[paper](https://arxiv.org/abs/2601.03785)]
- [2026] **ES-Mem: Event Segmentation-Based Memory for Long-Term Dialogue Agents** [[paper](https://arxiv.org/abs/2601.07582)]
- [2026] **Inside Out: Evolving User-Centric Core Memory Trees for Long-Term Personalized Dialogue Systems** [[paper](https://arxiv.org/abs/2601.05171)]
- [2026] **MemRec: Collaborative Memory-Augmented Agentic Recommender System** *ACL 2026 Main Conference* [[paper](https://arxiv.org/abs/2601.08816)]
- [2026] **TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents** [[paper](https://arxiv.org/abs/2601.02845)]
- [2026] **CAST: Character-and-Scene Episodic Memory for Agents** [[paper](https://arxiv.org/abs/2602.06051)]
- [2026] **Me-Agent: A Personalized Mobile Agent with Two-Level User Habit Learning for Enhanced Interaction** [[paper](https://arxiv.org/abs/2601.20162)]
- [2026] **Amory: Building Coherent Narrative-Driven Agent Memory through Agentic Reasoning** [[paper](https://arxiv.org/abs/2601.06282)]
- [2026] **RealMem: Benchmarking LLMs in Real-World Memory-Driven Interaction** [[paper](https://arxiv.org/abs/2601.06966)]
- [2026] **OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents** [[paper](https://arxiv.org/abs/2601.13722)]
- [2026] **Character-R1: Enhancing Role-Aware Reasoning in Role-Playing Agents via RLVR** [[paper](https://arxiv.org/abs/2601.04611)]
- [2026] **SYNAPSE: Empowering LLM Agents with Episodic-Semantic Memory via Spreading Activation** [[paper](https://arxiv.org/abs/2601.02744)]
- [2026] **Memory Poisoning Attack and Defense on Memory Based LLM-Agents** [[paper](https://arxiv.org/abs/2601.05504)]
- [2026] **ShardMemo: Masked MoE Routing for Sharded Agentic LLM Memory** [[paper](https://arxiv.org/abs/2601.21545)]
- [2026] **HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents** [[paper](https://arxiv.org/abs/2601.06377)]
- [2026] **Cost and Accuracy of Long-Term Memory in Distributed Multi-Agent Systems Based on Large Language Models** [[paper](https://arxiv.org/abs/2601.07978)]
- [2026] **BMAM: Brain-inspired Multi-Agent Memory Framework** [[paper](https://arxiv.org/abs/2601.20465)]
- [2026] **Project Synapse: A Hierarchical Multi-Agent Framework with Hybrid Memory for Autonomous Resolution of Last-Mile Delivery Disruptions** [[paper](https://arxiv.org/abs/2601.08156)]
- [2026] **CaveAgent: Transforming LLMs into Stateful Runtime Operators** [[paper](https://arxiv.org/abs/2601.01569)]
- [2026] **AgentSM: Semantic Memory for Agentic Text-to-SQL** [[paper](https://arxiv.org/abs/2601.15709)]
- [2026] **BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents** [[paper](https://arxiv.org/abs/2601.04566)]
- [2026] **Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human-Agent Interaction** [[paper](https://arxiv.org/abs/2601.05107)]
- [2026] **Query-Efficient Agentic Graph Extraction Attacks on GraphRAG Systems** *ACL Main 2026* [[paper](https://arxiv.org/abs/2601.14662)]
- [2026] **Mem-T: Densifying Rewards for Long-Horizon Memory Agents** [[paper](https://arxiv.org/abs/2601.23014)]

##### 2025

- [2025] **From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition** [[paper](https://arxiv.org/abs/2512.14244)]
- [2025] **MemVerse: Multimodal Memory for Lifelong Learning Agents** [[paper](https://arxiv.org/abs/2512.03627)]
- [2025] **MMAG: Mixed Memory-Augmented Generation for Large Language Models Applications** [[paper](https://arxiv.org/abs/2512.01710)]
- [2025] **Sophia: A Persistent Agent Framework of Artificial Life** [[paper](https://arxiv.org/abs/2512.18202)]
- [2025] **WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning** [[paper](https://arxiv.org/abs/2512.02425)]
- [2025] **Memoria: A Scalable Agentic Memory Framework for Personalized Conversational AI** [[paper](https://arxiv.org/abs/2512.12686)]
- [2025] **Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects** [[paper](https://arxiv.org/abs/2512.12818)]
- [2025] **MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval** [[paper](https://arxiv.org/abs/2512.16962)]
- [2025] **Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs** [[paper](https://arxiv.org/abs/2512.04668)]
- [2025] **Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills** [[paper](https://arxiv.org/abs/2512.16301)]
- [2025] **PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory** [[paper](https://arxiv.org/abs/2512.06688)]
- [2025] **Memory Fabric for Conversational AI Agents: Enabling Shared and Persistent Memory Across Users** [[paper](https://doi.org/https://doi.org/10.36227/techrxiv.176523350.08289935/v1)]
- [2025] **Bilevel Optimization for Covert Memory Tampering in Heterogeneous Multi-Agent Architectures (XAMT)** [[paper](https://arxiv.org/abs/2512.15790)]
- [2025] **Memory in the Age of AI Agents** [[paper](https://arxiv.org/abs/2512.13564)]
- [2025] **AI Meets Brain: Memory Systems from Cognitive Neuroscience to Autonomous Agents** [[paper](https://arxiv.org/abs/2512.23343)]
- [2025] **From Personalization to Prejudice: Bias and Discrimination in Memory-Enhanced AI Agents for Recruitment** *https://doi.org/10.1145/3773966.3779376* [[paper](https://arxiv.org/abs/2512.16532)]
- [2025] **A Simple Yet Strong Baseline for Long-Term Conversational Memory of LLM Agents** [[paper](https://arxiv.org/abs/2511.17208)]
- [2025] **General Agentic Memory Via Deep Research** [[paper](https://arxiv.org/abs/2511.18423)]
- [2025] **O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents** [[paper](https://arxiv.org/abs/2511.13593)]
- [2025] **RCR-Router: Efficient Role-Aware Context Routing for Multi-Agent LLM Systems with Structured Memory** [[paper](https://arxiv.org/abs/2508.04903)]
- [2025] **Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory and User Profiles** [[paper](https://arxiv.org/abs/2510.07925)]
- [2025] **LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning** *Findings ACL 2026* [[paper](https://arxiv.org/abs/2511.01448)]
- [2025] **Fixed-Persona SLMs with Modular Memory: Scalable NPC Dialogue on Consumer Hardware** [[paper](https://arxiv.org/abs/2511.10277)]
- [2025] **Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory** [[paper](https://arxiv.org/abs/2511.20857)]
- [2025] **From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory** [[paper](https://arxiv.org/abs/2511.07800)]
- [2025] **Episodic Memory in Agentic Frameworks: Suggesting Next Tasks** [[paper](https://arxiv.org/abs/2511.17775)]
- [2025] **Livia: An Emotion-Aware AR Companion Powered by Modular AI Agents and Progressive Memory Compression** [[paper](https://arxiv.org/abs/2509.05298)]
- [2025] **D-SMART: Enhancing LLM Dialogue Consistency via Dynamic Structured Memory And Reasoning Tree** [[paper](https://arxiv.org/abs/2510.13363)]
- [2025] **WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research** [[paper](https://arxiv.org/abs/2509.13312)]
- [2025] **CAM: A Constructivist View of Agentic Memory for LLM-Based Reading Comprehension** [[paper](https://arxiv.org/abs/2510.05520)]
- [2025] **Pre-Storage Reasoning for Episodic Memory: Shifting Inference Burden to Memory for Personalized Dialogue** [[paper](https://arxiv.org/abs/2509.10852)]
- [2025] **LightMem: Lightweight and Efficient Memory-Augmented Generation** [[paper](https://arxiv.org/abs/2510.18866)]
- [2025] **RGMem: Renormalization Group-based Memory Evolution for Language Agent User Profile** [[paper](https://arxiv.org/abs/2510.16392)]
- [2025] **PISA: A Pragmatic Psych-Inspired Unified Memory System for Enhanced AI Agency** [[paper](https://arxiv.org/abs/2510.15966)]
- [2025] **A-MemGuard: A Proactive Defense Framework for LLM-Based Agent Memory** [[paper](https://arxiv.org/abs/2510.02373)]
- [2025] **Evaluating Long-Term Memory for Long-Context Question Answering** [[paper](https://arxiv.org/abs/2510.23730)]
- [2025] **WebATLAS: An LLM Agent with Experience-Driven Memory and Action Simulation** [[paper](https://arxiv.org/abs/2510.22732)]
- [2025] **Preference-Aware Memory Update for Long-Term LLM Agents** [[paper](https://arxiv.org/abs/2510.09720)]
- [2025] **MEMTRACK: Evaluating Long-Term Memory and State Tracking in Multi-Platform Dynamic Agent Environments** [[paper](https://arxiv.org/abs/2510.01353)]
- [2025] **Spatiotemporal Knowledge Graphs as Persistent Scene Memory for Embodied Question Answering** [[paper](https://arxiv.org/abs/2510.01483)]
- [2025] **AUGUSTUS: An LLM-Driven Multimodal Agent System with Contextualized User Memory** *NeurIPS 2025. Work done from late 2023 to early 2024* [[paper](https://arxiv.org/abs/2510.15261)]
- [2025] **TALM: Dynamic Tree-Structured Multi-Agent Framework with Long-Term Memory for Scalable Code Generation** [[paper](https://arxiv.org/abs/2510.23010)]
- [2025] **Memory-Augmented State Machine Prompting: A Novel LLM Agent Framework for Real-Time Strategy Games** [[paper](https://arxiv.org/abs/2510.18395)]
- [2025] **Constructing coherent spatial memory in LLM agents through graph rectification** [[paper](https://arxiv.org/abs/2510.04195)]
- [2025] **Evolution in Simulation: AI-Agent School with Dual Memory for High-Fidelity Educational Dynamics** *https://doi.org/10.18653/v1/2025.findings-emnlp.312* [[paper](https://arxiv.org/abs/2510.11290)]
- [2025] **Terrarium: Revisiting the Blackboard for Multi-Agent Safety, Privacy, and Security Studies** [[paper](https://arxiv.org/abs/2510.14312)]
- [2025] **MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems** [[paper](https://arxiv.org/abs/2510.17281)]
- [2025] **Mem-α: Learning Memory Construction via Reinforcement Learning** [[paper](https://arxiv.org/abs/2509.25911)]
- [2025] **SGMem: Sentence Graph Memory for Long-Term Conversational Agents** [[paper](https://arxiv.org/abs/2509.21212)]
- [2025] **Nemori: Self-Organizing Agent Memory Inspired by Cognitive Science** [[paper](https://arxiv.org/abs/2508.03341)]
- [2025] **MOOM: Maintenance, Organization and Optimization of Memory in Ultra-Long Role-Playing Dialogues** [[paper](https://arxiv.org/abs/2509.11860)]
- [2025] **Multiple Memory Systems for Enhancing the Long-term Memory of Agent** [[paper](https://arxiv.org/abs/2508.15294)]
- [2025] **Semantic Anchoring in Agentic Memory: Leveraging Linguistic Structures for Persistent Conversational Context** [[paper](https://arxiv.org/abs/2508.12630)]
- [2025] **ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning** [[paper](https://arxiv.org/abs/2508.10419)]
- [2025] **MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service** [[paper](https://arxiv.org/abs/2509.18713)]
- [2025] **Text2Mem: A Unified Memory Operation Language for Memory Operating System** [[paper](https://arxiv.org/abs/2509.11145)]
- [2025] **Meta-Memory: Retrieving and Integrating Semantic-Spatial Memories for Robot Spatial Reasoning** [[paper](https://arxiv.org/abs/2509.20754)]
- [2025] **LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science** [[paper](https://arxiv.org/abs/2510.01285)]
- [2025] **Building Self-Evolving Agents via Experience-Driven Lifelong Learning: A Framework and Benchmark** [[paper](https://arxiv.org/abs/2508.19005)]
- [2025] **Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory** [[paper](https://arxiv.org/abs/2508.09736)]
- [2025] **Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning** [[paper](https://arxiv.org/abs/2508.19828)]
- [2025] **Intrinsic Memory Agents: Heterogeneous Multi-Agent LLM Systems through Structured Contextual Memory** [[paper](https://arxiv.org/abs/2508.08997)]
- [2025] **Designing Memory-Augmented AR Agents for Spatiotemporal Reasoning in Personalized Task Assistance** [[paper](https://arxiv.org/abs/2508.08774)]
- [2025] **Persode: Personalized Visual Journaling with Episodic Memory-Aware AI Agent** [[paper](https://arxiv.org/abs/2508.20585)]
- [2025] **Scene-Aware Vectorized Memory Multi-Agent Framework with Cross-Modal Differentiated Quantization VLMs for Visually Impaired Assistance** [[paper](https://arxiv.org/abs/2508.18177)]
- [2025] **MIRIX: Multi-Agent Memory System for LLM-Based Agents** [[paper](https://arxiv.org/abs/2507.07957)]
- [2025] **Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents** [[paper](https://arxiv.org/abs/2507.22925)]
- [2025] **MemoryAgentBench: Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions** [[paper](https://arxiv.org/abs/2507.05257)]
- [2025] **MLC-Agent: Cognitive Model based on Memory-Learning Collaboration in LLM Empowered Agent Simulation Environment** [[paper](https://arxiv.org/abs/2507.20215)]
- [2025] **Test-Time-Matching: Decouple Personality, Memory, and Linguistic Style in LLM-based Role-Playing Language Agent** [[paper](https://arxiv.org/abs/2507.16799)]
- [2025] **Generative Life Agents: A Novel Framework for Persistent, Evolving Personas with Traceable Personality Drift** [[paper](https://doi.org/https://doi.org/10.21203/rs.3.rs-7018899/v1)]
- [2025] **G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems** [[paper](https://arxiv.org/abs/2506.07398)]
- [2025] **Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance** *ICLR 2026* [[paper](https://arxiv.org/abs/2505.16348)]
- [2025] **MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents** *ACL 2025 Findings* [[paper](https://arxiv.org/abs/2506.21605)] [[code](https://github.com/import-myself/Membench)]
- [2025] **Memory OS of AI Agent** [[paper](https://arxiv.org/abs/2506.06326)]
- [2025] **State and Memory is All You Need for Robust and Reliable AI Agents** [[paper](https://arxiv.org/abs/2507.00081)]
- [2025] **PersonaAgent: Bridging Memory and Action for Personalized LLM Agents** *ACL 2026* [[paper](https://arxiv.org/abs/2506.06254)]
- [2025] **MAPLE: Multi-Agent Adaptive Planning with Long-Term Memory for Table Reasoning** [[paper](https://arxiv.org/abs/2506.05813)]
- [2025] **VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents** [[paper](https://arxiv.org/abs/2506.02539)]
- [2025] **PBFT-Backed Semantic Voting for Multi-Agent Memory Pruning** [[paper](https://arxiv.org/abs/2506.17338)]
- [2025] **On Immutable Memory Systems for Artificial Agents: A Blockchain-Indexed Automata-Theoretic Framework Using ECDH-Keyed Merkle Chains** [[paper](https://arxiv.org/abs/2506.13246)]
- [2025] **Context manipulation attacks : Web agents are susceptible to corrupted memory** [[paper](https://arxiv.org/abs/2506.17318)]
- [2025] **Hybrid Multi-Agent GraphRAG for E-Government: Towards a Trustworthy AI Assistant** [[paper](https://doi.org/https://doi.org/10.3390/app15116315)]
- [2025] **MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents** [[paper](https://arxiv.org/abs/2505.20231)]
- [2025] **Pre-training Limited Memory Language Models with Internal and External Knowledge** [[paper](https://arxiv.org/abs/2505.15962)]
- [2025] **Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding** [[paper](https://arxiv.org/abs/2501.00358)]
- [2025] **How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior** *ACL 2026* [[paper](https://arxiv.org/abs/2505.16067)]
- [2025] **From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents** [[paper](https://arxiv.org/abs/2505.19549)]
- [2025] **Rethinking Memory in LLM based Agents: Representations, Operations, and Emerging Topics** [[paper](https://arxiv.org/abs/2505.00675)]
- [2025] **Imagine, Verify, Execute: Memory-guided Agentic Exploration with Vision-Language Models** [[paper](https://arxiv.org/abs/2505.07815)]
- [2025] **From Knowledge to Noise: CTIM-Rover and the Pitfalls of Episodic Memory in Software Engineering Agents** [[paper](https://arxiv.org/abs/2505.23422)]
- [2025] **UserCentrix: An Agentic Memory-augmented AI Framework for Smart Spaces** [[paper](https://arxiv.org/abs/2505.00472)]
- [2025] **MemEngine: A Unified and Modular Library for Developing Advanced Memory of LLM-based Agents** [[paper](https://arxiv.org/abs/2505.02099)]
- [2025] **Mem0: Building production-ready ai agents with scalable long-term memory** [[paper](https://arxiv.org/abs/2504.19413)]
- [2025] **Task Memory Engine (TME): Enhancing State Awareness for Multi-Step LLM Agent Tasks** [[paper](https://arxiv.org/abs/2504.08525)]
- [2025] **Decentralizing AI Memory: SHIMI, a Semantic Hierarchical Memory Index for Scalable Agent Reasoning** [[paper](https://arxiv.org/abs/2504.06135)]
- [2025] **AI-native Memory 2.0: Second Me** [[paper](https://arxiv.org/abs/2503.08102)]
- [2025] **Unified Mind Model: Reimagining Autonomous Agents in the LLM Era** [[paper](https://arxiv.org/abs/2503.03459)]
- [2025] **MemInsight: Autonomous Memory Augmentation for LLM Agents** [[paper](https://arxiv.org/abs/2503.21760)]
- [2025] **In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents** [[paper](https://aclanthology.org/2025.acl-long.413/)]
- [2025] **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** [[paper](https://arxiv.org/abs/2501.13956)]
- [2025] **R³Mem: Bridging Memory Retention and Retrieval via Reversible Compression** [[paper](https://arxiv.org/abs/2502.15957)]
- [2025] **A-MEM: Agentic Memory for LLM Agents** [[paper](https://arxiv.org/abs/2502.12110)]
- [2025] **Unveiling Privacy Risks in LLM Agent Memory** [[paper](https://arxiv.org/abs/2502.13172)]
- [2025] **Mem2Ego: Empowering Vision-Language Models with Global-to-Ego Memory for Long-Horizon Embodied Navigation** [[paper](https://arxiv.org/abs/2502.14254)]
- [2025] **Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents** [[paper](https://arxiv.org/abs/2502.15840)]
- [2025] **On Memory Construction and Retrieval for Personalized Conversational Agents** [[paper](https://arxiv.org/abs/2502.05589)]
- [2025] **Position: Episodic Memory is the Missing Piece for Long-Term LLM Agents** [[paper](https://arxiv.org/abs/2502.06975)]
- [2025] **TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogues** *ACL 2025 Findings* [[paper](https://arxiv.org/abs/2502.01630)]
- [2025] **AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware Cross-domain Recommendations** [[paper](https://arxiv.org/abs/2502.13843)]
- [2025] **SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents** [[paper](https://openreview.net/forum?id=xKDZAW0He3)]
- [2025] **Lifelong Learning of Large Language Model based Agents: A Roadmap** [[paper](https://arxiv.org/abs/2501.07278)]
- [2025] **Episodic memory in AI agents poses risks that should be studied and mitigated** [[paper](https://arxiv.org/abs/2501.11739)]
- [2025] **Addressing the sustainable AI trilemma: a case study on LLM agents and RAG** [[paper](https://arxiv.org/abs/2501.08262)]
- [2025] **SciToolAgent: A Knowledge Graph-Driven Scientific Agent for Multi-Tool Integration** [[paper](https://doi.org/https://doi.org/10.21203/rs.3.rs-5610718/v1)]

##### 2024

- [2024] **AI PERSONA: Towards Life-long Personalization of LLMs** [[paper](https://arxiv.org/abs/2412.13103)]
- [2024] **On the Structural Memory of LLM Agents** [[paper](https://arxiv.org/abs/2412.15266)]
- [2024] **OASIS: Open Agent Social Interaction Simulations with One Million Agents** [[paper](https://arxiv.org/abs/2411.11581)]
- [2024] **Video-RAG: Visually-aligned Retrieval-Augmented Long Video Comprehension** *NeurIPS 2025. Camera-ready version* [[paper](https://arxiv.org/abs/2411.13093)]
- [2024] **Memolet: Reifying the Reuse of User-AI Conversational Memories** [[paper](https://doi.org/10.1145/3654777.3676388)]
- [2024] **From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs** [[paper](https://arxiv.org/abs/2410.14052)]
- [2024] **Enhancing Long Context Performance in LLMs Through Inner Loop Query Mechanism** [[paper](https://arxiv.org/abs/2410.12859)]
- [2024] **LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory** [[paper](https://arxiv.org/abs/2410.10813)] [[code](https://github.com/xiaowu0162/LongMemEval)]
- [2024] **DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory** *ICLR 2025* [[paper](https://arxiv.org/abs/2410.08143)]
- [2024] **Large Language Models Empowered Personalized Web Agents** [[paper](https://arxiv.org/abs/2410.17236)]
- [2024] **Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation** [[paper](https://arxiv.org/abs/2410.13232)]
- [2024] **Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs** [[paper](https://arxiv.org/abs/2409.19401)]
- [2024] **KARMA: Augmenting Embodied AI Agents with Long-and-short Term Memory Systems** [[paper](https://arxiv.org/abs/2409.14908)]
- [2024] **Arigraph: Learning knowledge graph world models with episodic memory for llm agents** [[paper](https://arxiv.org/abs/2407.04363)]
- [2024] **ChatHaruhi: Reviving Anime Character in Reality via Large Language Model** [[paper](https://arxiv.org/abs/2308.09597)]
- [2024] **Toward Conversational Agents with Context and Time Sensitive Long-term Memory** [[paper](https://arxiv.org/abs/2406.00057)]
- [2024] **AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases** [[paper](https://arxiv.org/abs/2407.12784)]
- [2024] **Human-inspired Episodic Memory for Infinite Context LLMs** [[paper](https://openreview.net/forum?id=BI2int5SAC)]
- [2024] **Enhancing Long-Term Memory using Hierarchical Aggregate Tree for Retrieval Augmented Generation** [[paper](https://arxiv.org/abs/2406.06124)]
- [2024] **Towards Lifelong Dialogue Agents via Timeline-based Memory Management** [[paper](https://arxiv.org/abs/2406.10996)]
- [2024] **AI-native Memory: A Pathway from LLMs Towards AGI** [[paper](https://arxiv.org/abs/2406.18312)]
- [2024] **Hello Again! LLM-powered Personalized Agent for Long-term Dialogue** [[paper](https://arxiv.org/abs/2406.05925)]
- [2024] **HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models** [[paper](https://arxiv.org/abs/2405.14831)]
- [2024] **Memory Sharing for Large Language Model based Agents** [[paper](https://arxiv.org/abs/2404.09982)]
- [2024] **Knowledge Graph Tuning: Real-time Large Language Model Personalization based on Human Feedback** [[paper](https://arxiv.org/abs/2405.19686)]
- [2024] **Nadine: An LLM-driven Intelligent Social Robot with Affective Capabilities and Human-like Memory** [[paper](https://arxiv.org/abs/2405.20189)]
- [2024] **Episodic Question Answering for Cognitive Agents** [[paper](https://doi.org/https://doi.org/10.21203/rs.3.rs-4351479/v1)]
- [2024] **From Local to Global: A Graph RAG Approach to Query-Focused Summarization** [[paper](https://arxiv.org/abs/2404.16130)]
- [2024] **HELPER-X: A Unified Instructable Embodied Agent with Memory-Augmented Language Models** [[paper](https://arxiv.org/abs/2404.19065)]
- [2024] **AgentsCoDriver: Large Language Model Empowered Collaborative Driving with Lifelong Learning** [[paper](https://arxiv.org/abs/2404.06345)]
- [2024] **A Survey on the Memory Mechanism of Large Language Model based Agents** [[paper](https://arxiv.org/abs/2404.13501)]
- [2024] **Memoro: Using Large Language Models to Realize a Concise Interface for Real-Time Memory Augmentation** [[paper](https://doi.org/10.1145/3613904.3642450)]
- [2024] **"My agent understands me better": Integrating Dynamic Human-like Memory Recall and Consolidation in LLM-Based Agents** *https://doi.org/10.1145/3613905.3650839* [[paper](https://arxiv.org/abs/2404.00573)]
- [2024] **A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts** [[paper](https://arxiv.org/abs/2402.09727)]
- [2024] **From LLM to Conversational Agent: A Memory Enhanced Architecture with Fine-Tuning of Large Language Models** [[paper](https://arxiv.org/abs/2401.02777)]
- [2024] **ATM: Adversarial Tuning Multi-agent System Makes a Robust Retrieval-Augmented Generator** [[paper](https://doi.org/https://doi.org/10.18653/v1/2024.emnlp-main.610)]

##### 2023

- [2023] **Cognitively Inspired Components for Social Conversational Agents** [[paper](https://arxiv.org/abs/2311.05450)]
- [2023] **War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars** [[paper](https://arxiv.org/abs/2311.17227)]
- [2023] **MemGPT: Towards LLMs as Operating Systems** [[paper](https://arxiv.org/abs/2310.08560)]
- [2023] **GameGPT: Multi-agent Collaborative Framework for Game Development** [[paper](https://arxiv.org/abs/2310.08067)]
- [2023] **Lyfe Agents: Generative agents for low-cost real-time social interactions** [[paper](https://arxiv.org/abs/2310.02172)]
- [2023] **Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models** [[paper](https://arxiv.org/abs/2310.15127)]
- [2023] **RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models** [[paper](https://doi.org/10.18653/v1/2024.findings-acl.878)]
- [2023] **MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework** [[paper](https://arxiv.org/abs/2308.00352)]
- [2023] **MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation** [[paper](https://arxiv.org/abs/2308.08239)]
- [2023] **Recursively summarizing enables long-term dialogue memory in large language models** [[paper](https://arxiv.org/abs/2308.15022)]
- [2023] **CALYPSO: LLMs as Dungeon Masters' Assistants** [[paper](https://doi.org/10.1609/aiide.v19i1.27534)]
- [2023] **Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations** [[paper](https://doi.org/10.1145/3731446)]
- [2023] **MovieChat: From Dense Token to Sparse Memory for Long Video Understanding** [[paper](https://doi.org/10.1109/CVPR52733.2024.01725)]
- [2023] **S³: Social-network Simulation System with Large Language Model-Empowered Agents** [[paper](https://arxiv.org/abs/2307.14984)]
- [2023] **RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text** [[paper](https://arxiv.org/abs/2305.13304)]
- [2023] **Memorybank: Enhancing large language models with long-term memory** [[paper](https://arxiv.org/abs/2305.10250)]
- [2023] **RET-LLM: Towards a general read-write memory for large language models** [[paper](https://arxiv.org/abs/2305.14322)]
- [2023] **Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory** [[paper](https://arxiv.org/abs/2305.17144)]
- [2023] **Prompted LLMs as Chatbot Modules for Long Open-domain Conversation** [[paper](https://doi.org/10.18653/v1/2023.findings-acl.277)]
- [2023] **Generative agents: Interactive simulacra of human behavior** [[paper](https://arxiv.org/abs/2304.03442)]
- [2023] **HuaTuo: Tuning LLaMA Model with Chinese Medical Knowledge** [[paper](https://arxiv.org/abs/2304.06975)]
- [2023] **SCM: Enhancing Large Language Model with Self-Controlled Memory Framework** [[paper](https://arxiv.org/abs/2304.13343)]

##### 2022

- [2022] **Deciding a Graph Property by a Single Mobile Agent: One-Bit Memory Suffices** [[paper](https://arxiv.org/abs/2209.01906)]
- [2022] **BlenderBot 3: a deployed conversational agent that continually learns to responsibly engage** [[paper](https://arxiv.org/abs/2208.03188)]
- [2022] **FCMNet: Full Communication Memory Net for Team-Level Cooperation in Multi-Agent Systems** [[paper](https://arxiv.org/abs/2201.11994)]

##### 2020

- [2020] **A Proposal for Intelligent Agents with Episodic Memory** [[paper](https://arxiv.org/abs/2005.03182)]

##### 2018

- [2018] **Unsupervised Predictive Memory in a Goal-Directed Agent** [[paper](https://arxiv.org/abs/1803.10760)]

[⬆ Back to top](#paper-list)

#### Parametric

##### 2026

- [2026] **Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents** [[paper](https://arxiv.org/abs/2606.26806)]
- [2026] **PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft** [[paper](https://arxiv.org/abs/2605.27762)]
- [2026] **HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents** [[paper](https://arxiv.org/abs/2604.16839)]
- [2026] **EmbodiedLGR: Integrating Lightweight Graph Representation and Retrieval for Semantic-Spatial Memory in Robotic Agents** [[paper](https://arxiv.org/abs/2604.18271)]

##### 2025

- [2025] **MemLoRA: Distilling Expert Adapters for On-Device Memory Systems** [[paper](https://arxiv.org/abs/2512.04763)]
- [2025] **Pretraining with hierarchical memories: separating long-tail and common knowledge** [[paper](https://arxiv.org/abs/2510.02375)]
- [2025] **Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models** [[paper](https://arxiv.org/abs/2508.09874)]
- [2025] **MLP Memory: Language Modeling with Retriever-pretrained External Memory** [[paper](https://arxiv.org/abs/2508.01832)]

##### 2024

- [2024] **AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models** [[paper](https://arxiv.org/abs/2410.02355)]
- [2024] **Self-Updatable Large Language Models by Integrating Context into Model Parameters** [[paper](https://openreview.net/forum?id=aCPFCDL9QY)]
- [2024] **ELDER: Enhancing Lifelong Model Editing with Mixture-of-LoRA** [[paper](https://doi.org/10.1609/aaai.v39i23.34622)]
- [2024] **WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models** [[paper](https://papers.nips.cc/paper_files/paper/2024/hash/60960ad78868fce5c165295fbd895060-Abstract-Conference.html)]
- [2024] **Online Adaptation of Language Models with a Memory of Amortized Contexts** [[paper](https://papers.nips.cc/paper_files/paper/2024/hash/eaf956b52bae51fbf387b8be4cc3ce18-Abstract-Conference.html)]
- [2024] **Neighboring Perturbations of Knowledge Editing on Large Language Models** [[paper](https://openreview.net/forum?id=K9NTPRvVRI)]

##### 2023

- [2023] **CharacterGLM: Customizing Social Characters with Large Language Models** [[paper](https://doi.org/10.18653/v1/2024.emnlp-industry.107)]
- [2023] **Character-LLM: A Trainable Agent for Role-Playing** [[paper](https://doi.org/10.18653/v1/2023.emnlp-main.814)]

##### 2021

- [2021] **Fast Model Editing at Scale** [[paper](https://openreview.net/forum?id=0DcZxeWfOPt)]
- [2021] **Editing Factual Knowledge in Language Models** *EMNLP2021 Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing. Code at https* [[paper](https://arxiv.org/abs/2104.08164)]

##### 2020

- [2020] **K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters** [[paper](https://doi.org/10.18653/v1/2021.findings-acl.121)]

##### 2013

- [2013] **ELLA: An Efficient Lifelong Learning Algorithm** [[paper](https://proceedings.mlr.press/v28/ruvolo13.html)]

[⬆ Back to top](#paper-list)

#### Latent

##### 2026

- [2026] **Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory** [[paper](https://arxiv.org/abs/2607.24368)]
- [2026] **LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory** [[paper](https://arxiv.org/abs/2607.22690)]
- [2026] **MRAgent: Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents** *ICML 2026* [[paper](https://arxiv.org/abs/2606.06036)] [[code](https://github.com/Ji-shuo/MRAgent)]
- [2026] **EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory** [[paper](https://arxiv.org/abs/2606.21649)]
- [2026] **When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration** [[paper](https://arxiv.org/abs/2606.28958)]
- [2026] **ElasticMem: Latent Memory as a Learnable Resource for LLM Agents** [[paper](https://arxiv.org/abs/2605.30690)]
- [2026] **Visual Agentic Memory: Enabling Online Long Video Understanding via Online Indexing, Hierarchical Memory, and Agentic Retrieval** [[paper](https://arxiv.org/abs/2605.16481)]
- [2026] **Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning** [[paper](https://arxiv.org/abs/2605.08271)]
- [2026] **Remember Your Trace: Memory-Guided Long-Horizon Agentic Framework for Consistent and Hierarchical Repository-Level Code Documentation** [[paper](https://arxiv.org/abs/2605.14563)]
- [2026] **MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens** [[paper](https://arxiv.org/abs/2603.23516)]
- [2026] **NextMem: Towards Latent Factual Memory for LLM-based Agents** [[paper](https://arxiv.org/abs/2603.15634)]
- [2026] **LatentMem: Customizing Latent Memory for Multi-Agent Systems** [[paper](https://arxiv.org/abs/2602.03036)]
- [2026] **Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices** [[paper](https://arxiv.org/abs/2603.04428)]
- [2026] **Structured Episodic Event Memory** [[paper](https://arxiv.org/abs/2601.06411)]
- [2026] **Dual Latent Memory for Visual Multi-agent System** [[paper](https://arxiv.org/abs/2602.00471)]

##### 2025

- [2025] **Are Agents Probabilistic Automata? A Trace-Based, Memory-Constrained Theory of Agentic AI** [[paper](https://arxiv.org/abs/2510.23487)]
- [2025] **Similarity-Distance-Magnitude Activations** [[paper](https://arxiv.org/abs/2509.12760)]
- [2025] **Towards General Continuous Memory for Vision-Language Models** [[paper](https://arxiv.org/abs/2505.17670)]
- [2025] **Ella: Embodied Social Agents with Lifelong Memory** [[paper](https://arxiv.org/abs/2506.24019)]
- [2025] **3DLLM-Mem: Long-Term Spatial-Temporal Memory for Embodied 3D Large Language Model** [[paper](https://arxiv.org/abs/2505.22657)]
- [2025] **CityNavAgent: Aerial Vision-and-Language Navigation with Hierarchical Semantic Planning and Global Memory** *https://doi.org/10.18653/v1/2025.acl-long.1511* [[paper](https://arxiv.org/abs/2505.05622)]
- [2025] **LLM-Empowered Embodied Agent for Memory-Augmented Task Planning in Household Robotics** [[paper](https://arxiv.org/abs/2504.21716)]
- [2025] **M+: Extending MemoryLLM with Scalable Long-Term Memory** [[paper](https://arxiv.org/abs/2502.00592)]

##### 2024

- [2024] **Episodic Memory Verbalization using Hierarchical Representations of Life-Long Robot Experience** *https://doi.org/10.1109/Humanoids65713.2025.11203101* [[paper](https://arxiv.org/abs/2409.17702)]
- [2024] **Memory³: Language Modeling with Explicit Memory** *https://doi.org/10.4208/jml.240708* [[paper](https://arxiv.org/abs/2407.01178)]
- [2024] **NeuroNAS: Enhancing Efficiency of Neuromorphic In-Memory Computing for Intelligent Mobile Agents through Hardware-Aware Spiking Neural Architecture Search** [[paper](https://arxiv.org/abs/2407.00641)]
- [2024] **MC-GPT: Empowering Vision-and-Language Navigation with Memory Map and Reasoning Chains** [[paper](https://arxiv.org/abs/2405.10620)]
- [2024] **Efficient Episodic Memory Utilization of Cooperative Multi-Agent Reinforcement Learning** [[paper](https://openreview.net/forum?id=LjivA1SLZ6)]

##### 2023

- [2023] **Memoria: Resolving Fateful Forgetting Problem through Human-Inspired Memory Architecture** [[paper](https://arxiv.org/abs/2310.03052)]

##### 2021

- [2021] **Detecting Local Insights from Global Labels: Supervised & Zero-Shot Sequence Labeling via a Convolutional Decomposition** [[paper](https://doi.org/10.1162/coli_a_00416)]

[⬆ Back to top](#paper-list)

### Experiential Memory

#### Token-level

##### 2026

- [2026] **From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents** [[paper](https://arxiv.org/abs/2607.16621)]
- [2026] **Experience Memory Graph: One-Shot Error Correction for Agents** [[paper](https://arxiv.org/abs/2607.13884)]
- [2026] **MemoHarness: Agent Harnesses That Learn from Experience** [[paper](https://arxiv.org/abs/2607.14159)]
- [2026] **Critic Experience Bank: Self-Evolving Step-Level Confidence Estimation for LLM Agents** [[paper](https://arxiv.org/abs/2607.12397)]
- [2026] **MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning** [[paper](https://arxiv.org/abs/2607.06974)]
- [2026] **MemVLN: Episodic and Procedural Memory for Vision-and-Language Navigation** [[paper](https://arxiv.org/abs/2607.23504)]
- [2026] **Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering** [[paper](https://arxiv.org/abs/2607.21571)]
- [2026] **Memory-Driven Self-Disclosure and Relational Turning Points: A Longitudinal Multimodal Study of Human-AI Interaction** [[paper](https://arxiv.org/abs/2607.14593)]
- [2026] **VTM-Nav: Harnessing Cross-Episode Experience for Object-Goal Navigation with Hierarchical Visual-Topological Memory** [[paper](https://arxiv.org/abs/2607.14514)]
- [2026] **MAPS: Modeling Co-Existing Subjective Perspectives and Shared Meaning in Multi-Agent Cognitive Dialogue** [[paper](https://arxiv.org/abs/2607.14110)]
- [2026] **An Explainable Agentic System for Detection of Conversational Scams with Summary-Based Memory** [[paper](https://arxiv.org/abs/2607.11707)]
- [2026] **Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs** [[paper](https://arxiv.org/abs/2606.23283)]
- [2026] **StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance** [[paper](https://arxiv.org/abs/2606.14571)]
- [2026] **Selective QA over Conflicting Multi-Source Personal Memory: A Diagnostic Testbed and Method Comparison** [[paper](https://arxiv.org/abs/2605.30087)]
- [2026] **Beyond Recall: Behavioral Specification as an Interpretive Layer for AI Personalization** [[paper](https://arxiv.org/abs/2605.28969)]
- [2026] **Personal Visual Memory from Explicit and Implicit Evidence** [[paper](https://arxiv.org/abs/2605.28806)]
- [2026] **The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems** [[paper](https://arxiv.org/abs/2605.21997)]
- [2026] **Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture** [[paper](https://arxiv.org/abs/2604.27045)]
- [2026] **StructMem: Structured Memory for Long-Horizon Behavior in LLMs** [[paper](https://arxiv.org/abs/2604.21748)]
- [2026] **VehicleMemBench: An Executable Benchmark for Multi-User Long-Term Memory in In-Vehicle Agents** [[paper](https://arxiv.org/abs/2603.23840)]
- [2026] **Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution** [[paper](https://arxiv.org/abs/2603.23064)]
- [2026] **AdMem: Advanced Memory for Task-solving Agents** [[paper](https://arxiv.org/abs/2606.06787)]
- [2026] **Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering** [[paper](https://arxiv.org/abs/2606.29824)]
- [2026] **Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation** [[paper](https://arxiv.org/abs/2606.23127)]
- [2026] **EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments** [[paper](https://arxiv.org/abs/2606.13681)]
- [2026] **SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents** [[paper](https://arxiv.org/abs/2606.28434)]
- [2026] **Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory** [[paper](https://arxiv.org/abs/2606.09365)]
- [2026] **Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory** [[paper](https://arxiv.org/abs/2606.25115)]
- [2026] **Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning** [[paper](https://arxiv.org/abs/2606.24428)]
- [2026] **From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms** [[paper](https://arxiv.org/abs/2605.06716)]
- [2026] **LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues** [[paper](https://arxiv.org/abs/2605.12493)]
- [2026] **MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation** [[paper](https://arxiv.org/abs/2605.27366)]
- [2026] **EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective** [[paper](https://arxiv.org/abs/2605.18421)]
- [2026] **R2-Mem: Reflective Experience for Memory Search** [[paper](https://arxiv.org/abs/2605.13486)]
- [2026] **CAMeR: Keyword-Gated Hybrid Activation for Adaptive Memory Retention in LLM Agents** [[paper](https://arxiv.org/abs/2607.20458)]
- [2026] **Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory** [[paper](https://arxiv.org/abs/2605.10870)]
- [2026] **Feedback-Normalized Developer Memory for Reinforcement-Learning Coding Agents** [[paper](https://arxiv.org/abs/2605.01567)]
- [2026] **When Search Becomes Memory: Turning Robot Design Trials into Transferable Skills** [[paper](https://arxiv.org/abs/2605.25832)]
- [2026] **SkillOS: Learning Skill Curation for Self-Evolving Agents** [[paper](https://arxiv.org/abs/2605.06614)]
- [2026] **Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents** [[paper](https://arxiv.org/abs/2605.30159)]
- [2026] **Self-Evolving Multi-Agent Systems via Decentralized Memory** [[paper](https://arxiv.org/abs/2605.22721)]
- [2026] **EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents** [[paper](https://arxiv.org/abs/2605.13941)]
- [2026] **MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents** [[paper](https://arxiv.org/abs/2605.27437)]
- [2026] **ExpGraph: Model-Agnostic Experience Learning with Graph-Structured Memory for LLM Agents** [[paper](https://arxiv.org/abs/2605.30712)]
- [2026] **EXG: Self-Evolving Agents with Experience Graphs** [[paper](https://arxiv.org/abs/2605.17721)]
- [2026] **Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation** [[paper](https://arxiv.org/abs/2605.09315)]
- [2026] **AlphaMemo: Structured Search-Process Memory for Self-Evolving Alpha Mining Agents** [[paper](https://arxiv.org/abs/2606.20625)]
- [2026] **MetaEvo: A Meta-Optimization Framework for Experience-Driven Agent Evolution** [[paper](https://arxiv.org/abs/2606.07603)]
- [2026] **MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs** [[paper](https://arxiv.org/abs/2605.08374)]
- [2026] **SECREFLECT: Reliable Context Evolution for Autonomous Cyber Agents via Pre-Memory Reflection Validation** [[paper](https://doi.org/https://doi.org/10.21203/rs.3.rs-9843491/v1)]
- [2026] **GAM: Hierarchical Graph-based Agentic Memory for LLM Agents** *ACL 2026* [[paper](https://arxiv.org/abs/2604.12285)]
- [2026] **Artifacts as Memory Beyond the Agent Boundary** [[paper](https://arxiv.org/abs/2604.08756)]
- [2026] **Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents** [[paper](https://arxiv.org/abs/2604.15877)]
- [2026] **When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents** [[paper](https://arxiv.org/abs/2604.27003)]
- [2026] **AEL: Agent Evolving Learning for Open-Ended Environments** [[paper](https://arxiv.org/abs/2604.21725)]
- [2026] **Thought-Retriever: Don't Just Retrieve Raw Data, Retrieve Thoughts for Memory-Augmented Agentic Systems** [[paper](https://arxiv.org/abs/2604.12231)]
- [2026] **Task-Adaptive Retrieval over Agentic Multi-Modal Web Histories via Learned Graph Memory** [[paper](https://arxiv.org/abs/2604.07863)]
- [2026] **Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents** [[paper](https://arxiv.org/abs/2604.20572)]
- [2026] **SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents** [[paper](https://arxiv.org/abs/2604.07791)]
- [2026] **Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory** [[paper](https://arxiv.org/abs/2604.01007)]
- [2026] **Drawing on Memory: Dual-Trace Encoding Improves Cross-Session Recall in LLM Agents** [[paper](https://arxiv.org/abs/2604.12948)]
- [2026] **PsychAgent: An Experience-Driven Lifelong Learning Agent for Self-Evolving Psychological Counselor** [[paper](https://arxiv.org/abs/2604.00931)]
- [2026] **Mem2Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation** [[paper](https://arxiv.org/abs/2604.10923)]
- [2026] **D-MEM: Dopamine-Gated Agentic Memory via Reward Prediction Error Routing** [[paper](https://arxiv.org/abs/2603.14597)]
- [2026] **Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory** [[paper](https://arxiv.org/abs/2603.04257)]
- [2026] **Scaling Teams or Scaling Time? Memory Enabled Lifelong Learning in LLM Multi-Agent Systems** [[paper](https://arxiv.org/abs/2604.03295)]
- [2026] **TheraAgent: Multi-Agent Framework with Self-Evolving Memory and Evidence-Calibrated Reasoning for PET Theranostics** [[paper](https://arxiv.org/abs/2603.13676)]
- [2026] **Position: Modular Memory is the Key to Continual Learning Agents** [[paper](https://arxiv.org/abs/2603.01761)]
- [2026] **Retrieval-Augmented LLM Agents: Learning to Learn from Experience** [[paper](https://arxiv.org/abs/2603.18272)]
- [2026] **AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents** [[paper](https://arxiv.org/abs/2603.09716)]
- [2026] **Token Coherence: Adapting MESI Cache Protocols to Minimize Synchronization Overhead in Multi-Agent LLM Systems** [[paper](https://arxiv.org/abs/2603.15183)]
- [2026] **HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC** [[paper](https://arxiv.org/abs/2603.01661)]
- [2026] **TA-Mem: Tool-Augmented Autonomous Memory Retrieval for LLM in Long-Term Conversational QA** [[paper](https://arxiv.org/abs/2603.09297)]
- [2026] **ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents** *ICML 2026* [[paper](https://arxiv.org/abs/2602.01869)]
- [2026] **UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory** [[paper](https://arxiv.org/abs/2602.10652)]
- [2026] **MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents** [[paper](https://arxiv.org/abs/2602.02474)]
- [2026] **MIRA: Memory-Integrated Reinforcement Learning Agent with Limited LLM Guidance** [[paper](https://arxiv.org/abs/2602.17930)]
- [2026] **Structurally Aligned Subtask-Level Memory for Software Engineering Agents** [[paper](https://arxiv.org/abs/2602.21611)]
- [2026] **Learning to Continually Learn via Meta-learning Agentic Memory Designs** [[paper](https://arxiv.org/abs/2602.07755)]
- [2026] **OCR-Agent: Agentic OCR with Capability and Memory Reflection** [[paper](https://arxiv.org/abs/2602.21053)]
- [2026] **MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory** [[paper](https://arxiv.org/abs/2601.03192)]
- [2026] **FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory** [[paper](https://arxiv.org/abs/2601.18642)]
- [2026] **Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory** *ACL 2026 Findings* [[paper](https://arxiv.org/abs/2601.07470)]
- [2026] **StackPlanner: A Centralized Hierarchical Multi-Agent System with Task-Experience Memory Management** [[paper](https://arxiv.org/abs/2601.05890)]
- [2026] **Jenius Agent: Towards Experience-Driven Accuracy Optimization in Real-World Scenarios** [[paper](https://arxiv.org/abs/2601.01857)]
- [2026] **EvoRoute: Experience-Driven Self-Routing LLM Agent Systems** [[paper](https://arxiv.org/abs/2601.02695)]
- [2026] **Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates** [[paper](https://arxiv.org/abs/2601.18510)]
- [2026] **Bi-Mem: Bidirectional Construction of Hierarchical Memory for Personalized LLMs via Inductive-Reflective Agents** [[paper](https://arxiv.org/abs/2601.06490)]
- [2026] **What Deserves Memory: Adaptive Memory Distillation for LLM Agents** [[paper](https://doi.org/https://doi.org/10.18653/v1/2026.acl-long.1607)]

##### 2025

- [2025] **MemEvolve: Meta-Evolution of Agent Memory Systems** [[paper](https://arxiv.org/abs/2512.18746)]
- [2025] **Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution** [[paper](https://arxiv.org/abs/2512.10696)]
- [2025] **Context as a Tool: Context Management for Long-Horizon SWE-Agents** [[paper](https://arxiv.org/abs/2512.22087)]
- [2025] **Memento 2: Learning by Stateful Reflective Memory** [[paper](https://arxiv.org/abs/2512.22716)]
- [2025] **Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory** [[paper](https://arxiv.org/abs/2512.23760)]
- [2025] **R-Debater: Retrieval-Augmented Debate Generation through Argumentative Memory** [[paper](https://arxiv.org/abs/2512.24684)]
- [2025] **AnalogSAGE: Self-evolving Analog Design Multi-Agents with Stratified Memory and Grounded Experience** [[paper](https://arxiv.org/abs/2512.22435)]
- [2025] **MemR3: Memory Retrieval via Reflective Reasoning for LLM Agents** [[paper](https://arxiv.org/abs/2512.20237)]
- [2025] **SEAL: Self-Evolving Agentic Learning for Conversational Question Answering over Knowledge Graphs** [[paper](https://arxiv.org/abs/2512.04868)]
- [2025] **Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement** [[paper](https://arxiv.org/abs/2512.18950)]
- [2025] **Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models** [[paper](https://arxiv.org/abs/2510.04618)]
- [2025] **FLEX: Continuous Agent Evolution via Forward Learning from Experience** [[paper](https://arxiv.org/abs/2511.06449)]
- [2025] **Scaling Agent Learning via Experience Synthesis** [[paper](https://arxiv.org/abs/2511.03773)]
- [2025] **UFO2: The Desktop AgentOS** [[paper](https://arxiv.org/abs/2504.14603)]
- [2025] **WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance** [[paper](https://arxiv.org/abs/2511.12997)]
- [2025] **Automated Test Case Generation in a Real-World System Using a Customized AI Agent: An Experience Report** [[paper](https://doi.org/https://doi.org/10.5753/sbqs.2025.15010)]
- [2025] **MemoriesDB: A Temporal-Semantic-Relational Database for Long-Term Agent Memory / Modeling Experience as a Graph of Temporal-Semantic Surfaces** *https://doi.org/10.5281/zenodo.17469799* [[paper](https://arxiv.org/abs/2511.06179)]
- [2025] **PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agents** *https://doi.org/10.18653/v1/2025.findings-emnlp.1164* [[paper](https://arxiv.org/abs/2509.17459)]
- [2025] **Training-Free Group Relative Policy Optimization** [[paper](https://arxiv.org/abs/2510.08191)]
- [2025] **ToolMem: Enhancing Multimodal Agents with Learnable Tool Capability Memory** [[paper](https://arxiv.org/abs/2510.06664)]
- [2025] **H²R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents** [[paper](https://arxiv.org/abs/2509.12810)]
- [2025] **BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions** [[paper](https://arxiv.org/abs/2510.10666)]
- [2025] **LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation** [[paper](https://arxiv.org/abs/2510.04851)]
- [2025] **Alita-G: Self-Evolving Generative Agent for Agent Generation** [[paper](https://arxiv.org/abs/2510.23601)]
- [2025] **Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting** [[paper](https://arxiv.org/abs/2510.10304)]
- [2025] **Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks** [[paper](https://arxiv.org/abs/2510.08002)]
- [2025] **Branch-and-Browse: Efficient and Controllable Web Exploration with Tree-Structured Reasoning and Action Memory** [[paper](https://arxiv.org/abs/2510.19838)]
- [2025] **Improving Code Localization with Repository Memory** [[paper](https://arxiv.org/abs/2510.01003)]
- [2025] **Learning from Supervision with Semantic and Episodic Memory: A Reflective Approach to Agent Adaptation** *https://doi.org/10.1145/3786335.3813154* [[paper](https://arxiv.org/abs/2510.19897)]
- [2025] **ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory** [[paper](https://arxiv.org/abs/2509.25140)]
- [2025] **Memento: Fine-tuning LLM Agents without Fine-tuning LLMs** [[paper](https://arxiv.org/abs/2508.16153)]
- [2025] **EgoMem: Lifelong Memory Agent for Full-duplex Omnimodal Models** [[paper](https://arxiv.org/abs/2509.11914)]
- [2025] **Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent** [[paper](https://arxiv.org/abs/2509.03990)]
- [2025] **Memp: Exploring Agent Procedural Memory** [[paper](https://arxiv.org/abs/2508.06433)]
- [2025] **SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience** [[paper](https://arxiv.org/abs/2508.04700)]
- [2025] **Towards Reliable Multi-Agent Systems for Marketing Applications via Reflection, Memory, and Planning** [[paper](https://arxiv.org/abs/2508.11120)]
- [2025] **Learn to Memorize: Optimizing LLM-based Agents with Adaptive Memory Framework** [[paper](https://arxiv.org/abs/2508.16629)]
- [2025] **Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving** [[paper](https://arxiv.org/abs/2507.06229)]
- [2025] **MemTool: Optimizing short-term memory management for dynamic tool calling in llm agent multi-turn conversations** [[paper](https://arxiv.org/abs/2507.21428)]
- [2025] **A Pragmatist Robot: Learning to Plan Tasks by Experiencing the Real World** [[paper](https://arxiv.org/abs/2507.16713)]
- [2025] **Reflection-Based Memory For Web navigation Agents** [[paper](https://arxiv.org/abs/2506.02158)]
- [2025] **Contextual Experience Replay for Self-Improvement of Language Agents** [[paper](https://arxiv.org/abs/2506.06698)]
- [2025] **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents** [[paper](https://arxiv.org/abs/2505.22954)]
- [2025] **Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution** [[paper](https://arxiv.org/abs/2505.20286)]
- [2025] **SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills** [[paper](https://arxiv.org/abs/2504.07079)]
- [2025] **LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark** [[paper](https://arxiv.org/abs/2504.13805)]
- [2025] **Retrieval Models Aren't Tool-Savvy: Benchmarking Tool Retrieval for Large Language Models** [[paper](https://arxiv.org/abs/2503.01763)]
- [2025] **AnnaAgent: Dynamic Evolution Agent System with Multi-Session Memory for Realistic Seeker Simulation** *https://doi.org/10.18653/v1/2025.findings-acl.1192* [[paper](https://arxiv.org/abs/2506.00551)]
- [2025] **BAR: A Backward Reasoning based Agent for Complex Minecraft Tasks** [[paper](https://arxiv.org/abs/2505.14079)]
- [2025] **Procedural Memory Is Not All You Need: Bridging Cognitive Gaps in LLM-Based Agents** *https://doi.org/10.1145/3708319.3734172* [[paper](https://arxiv.org/abs/2505.03434)]
- [2025] **Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory** [[paper](https://arxiv.org/abs/2504.07952)]
- [2025] **Inducing Programmatic Skills for Agentic Tasks** [[paper](https://arxiv.org/abs/2504.06821)]
- [2025] **COLA: A Scalable Multi-Agent Framework For Windows UI Task Automation** [[paper](https://arxiv.org/abs/2503.09263)]
- [2025] **Memory-augmented Query Reconstruction for LLM-based Knowledge Graph Reasoning** [[paper](https://arxiv.org/abs/2503.05193)]
- [2025] **MARS: Memory-Enhanced Agents with Reflective Self-improvement** [[paper](https://arxiv.org/abs/2503.19271)]
- [2025] **From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions** [[paper](https://arxiv.org/abs/2410.08197)]
- [2025] **From RAG to Memory: Non-Parametric Continual Learning for Large Language Models** [[paper](https://arxiv.org/abs/2502.14802)]
- [2025] **LLM-Powered Decentralized Generative Agents with Adaptive Hierarchical Knowledge Graph for Cooperative Planning** [[paper](https://arxiv.org/abs/2502.05453)]
- [2025] **R2D2: Remembering, Replaying and Dynamic Decision Making with a Reflective Agentic Memory** [[paper](https://arxiv.org/abs/2501.12485)]

##### 2024

- [2024] **Planning from Imagination: Episodic Simulation and Episodic Memory for Vision-and-Language Navigation** [[paper](https://arxiv.org/abs/2412.01857)]
- [2024] **Positive Experience Reflection for Agents in Interactive Text Environments** *NeurIPS 2024 Language Gamification workshop* [[paper](https://arxiv.org/abs/2411.02223)]
- [2024] **RepairAgent: An Autonomous, LLM-Based Agent for Program Repair** [[paper](https://arxiv.org/abs/2403.17134)]
- [2024] **SAGE: Self-evolving Agents with Reflective and Memory-augmented Abilities** [[paper](https://doi.org/10.1016/j.neucom.2025.130470)]
- [2024] **RAG-Modulo: Solving Sequential Tasks using Experience, Critics, and Language Models** [[paper](https://arxiv.org/abs/2409.12294)]
- [2024] **Self-evolving Agents with reflective and memory-augmented abilities** [[paper](https://arxiv.org/abs/2409.00872)]
- [2024] **Fincon: A synthesized llm multi-agent system with conceptual verbal reinforcement for enhanced financial decision making** [[paper](https://arxiv.org/abs/2407.06567)]
- [2024] **Agent Workflow Memory** [[paper](https://openreview.net/forum?id=NTAhi2JEEE)]
- [2024] **Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models** [[paper](https://papers.nips.cc/paper_files/paper/2024/hash/cde328b7bf6358f5ebb91fe9c539745e-Abstract-Conference.html)]
- [2024] **COLT: Towards Completeness-Oriented Tool Retrieval for Large Language Models** *https://doi.org/10.1145/3627673.3679847* [[paper](https://arxiv.org/abs/2405.16089)]
- [2024] **MetaReflection: Learning Instructions for Language Agents using Past Reflections** [[paper](https://arxiv.org/abs/2405.13009)]

##### 2023

- [2023] **JARVIS-1: Open-World Multi-Task Agents With Memory-Augmented Multimodal Language Models** [[paper](https://doi.org/10.1109/TPAMI.2024.3511593)]
- [2023] **Agents: An Open-source Framework for Autonomous Language Agents** [[paper](https://arxiv.org/abs/2309.07870)]
- [2023] **RecMind: Large Language Model Powered Agent For Recommendation** [[paper](https://doi.org/10.18653/v1/2024.findings-naacl.271)]
- [2023] **ExpeL: LLM Agents Are Experiential Learners** [[paper](https://doi.org/10.1609/aaai.v38i17.29936)]
- [2023] **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs** [[paper](https://arxiv.org/abs/2307.16789)]
- [2023] **Building Cooperative Embodied Agents Modularly with Large Language Models** [[paper](https://arxiv.org/abs/2307.02485)]
- [2023] **AccMER: Accelerating Multi-Agent Experience Replay with Cache Locality-aware Prioritization** [[paper](https://arxiv.org/abs/2306.00187)]
- [2023] **CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models** [[paper](https://doi.org/10.18653/v1/2023.findings-emnlp.462)]
- [2023] **Reflexion: Language agents with verbal reinforcement learning** [[paper](https://arxiv.org/abs/2303.11366)]
- [2023] **Toolformer: Language models can teach themselves to use tools** [[paper](https://arxiv.org/abs/2302.04761)]

[⬆ Back to top](#paper-list)

#### Parametric

##### 2026

- [2026] **WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction** [[paper](https://arxiv.org/abs/2605.29341)]
- [2026] **Scaling Self-Evolving Agents via Parametric Memory** [[paper](https://arxiv.org/abs/2606.04536)]
- [2026] **FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast** *https://doi.org/10.1145/3786335.3813155* [[paper](https://arxiv.org/abs/2605.16233)]
- [2026] **APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay** [[paper](https://arxiv.org/abs/2603.29093)]
- [2026] **ParamMem: Augmenting Language Agents with Parametric Reflective Memory** [[paper](https://arxiv.org/abs/2602.23320)]

##### 2025

- [2025] **AgentEvolver: Towards Efficient Self-Evolving Agent System** [[paper](https://arxiv.org/abs/2511.10395)]
- [2025] **Agent Learning via Early Experience** [[paper](https://arxiv.org/abs/2510.08558)]
- [2025] **Scaling Agents via Continual Pre-training** [[paper](https://arxiv.org/abs/2509.13310)]

##### 2024

- [2024] **ToolGen: Unified Tool Retrieval and Calling via Generation** [[paper](https://arxiv.org/abs/2410.03439)]

##### 2023

- [2023] **Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization** [[paper](https://arxiv.org/abs/2308.02151)]
- [2023] **A Machine with Short-Term, Episodic, and Semantic Memory Systems** [[paper](https://doi.org/10.1609/aaai.v37i1.25075)]

[⬆ Back to top](#paper-list)

#### Latent

##### 2026

- [2026] **MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents** [[paper](https://arxiv.org/abs/2607.24097)]
- [2026] **Deployment-Time Memorization in Foundation-Model Agents** [[paper](https://arxiv.org/abs/2606.10062)]
- [2026] **From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory** [[paper](https://arxiv.org/abs/2606.08656)]
- [2026] **DELTAMEM: Incremental Experience Memory for LLM Agents via Residual Trees** [[paper](https://arxiv.org/abs/2606.03083)]
- [2026] **ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems** [[paper](https://arxiv.org/abs/2606.08702)]
- [2026] **Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles** [[paper](https://arxiv.org/abs/2607.19359)]
- [2026] **What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA** [[paper](https://arxiv.org/abs/2605.23067)]
- [2026] **All-Mem: Agentic Lifelong Memory via Dynamic Topology Evolution** [[paper](https://arxiv.org/abs/2603.19595)] [[code](https://github.com/LvCan926/All-Mem)]
- [2026] **Temporal Memory for Resource-Constrained Agents: Continual Learning via Stochastic Compress-Add-Smooth** [[paper](https://arxiv.org/abs/2604.00067)]
- [2026] **TeleMem: Building Long-Term and Multimodal Memory for Agentic AI** [[paper](https://arxiv.org/abs/2601.06037)]
- [2026] **Experience-Driven Multi-Agent Systems Are Training-free Context-aware Earth Observers** [[paper](https://arxiv.org/abs/2602.02559)]

##### 2025

- [2025] **Auto-scaling Continuous Memory for GUI Agent** [[paper](https://arxiv.org/abs/2510.09038)]
- [2025] **SWE-Bench-CL: Continual Learning for Coding Agents** [[paper](https://arxiv.org/abs/2507.00014)]
- [2025] **NeSyC: A Neuro-symbolic Continual Learner For Complex Embodied Tasks In Open Domains** *ICLR 2025. Project site with code* [[paper](https://arxiv.org/abs/2503.00870)]

##### 2023

- [2023] **Large Language Models Are Semi-Parametric Reinforcement Learning Agents** [[paper](https://arxiv.org/abs/2306.07929)]

[⬆ Back to top](#paper-list)

### Working Memory

#### Token-level

##### 2026

- [2026] **SelfMem: Self-Optimizing Memory for AI Agents** [[paper](https://arxiv.org/abs/2607.03726)]
- [2026] **Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents** [[paper](https://arxiv.org/abs/2607.08716)]
- [2026] **AutoMem: Automated Learning of Memory as a Cognitive Skill** [[paper](https://arxiv.org/abs/2607.01224)]
- [2026] **Memory in the Loop: In-Process Retrieval as Extended Working Memory for Language Agents** [[paper](https://arxiv.org/abs/2607.05690)]
- [2026] **PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents** [[paper](https://arxiv.org/abs/2607.04089)]
- [2026] **Speculate with Memory: Lossless Acceleration for LLM Agents** [[paper](https://arxiv.org/abs/2607.12236)]
- [2026] **Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents** [[paper](https://arxiv.org/abs/2607.13591)]
- [2026] **PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning** [[paper](https://arxiv.org/abs/2607.20064)]
- [2026] **OpsMem: Dual-Memory Reasoning with Cross-Memory Resonance for Failure Diagnosis** [[paper](https://arxiv.org/abs/2607.11357)]
- [2026] **AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents** [[paper](https://arxiv.org/abs/2607.02255)]
- [2026] **Multi-Head Recurrent Memory Agents** [[paper](https://arxiv.org/abs/2607.01523)]
- [2026] **MemTools: A Unified Research Framework for Interoperable Agent Memory** [[paper](https://arxiv.org/abs/2607.21404)]
- [2026] **Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture** [[paper](https://arxiv.org/abs/2607.04391)]
- [2026] **StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems** [[paper](https://arxiv.org/abs/2607.05844)]
- [2026] **PM-Bench: Evaluating Prospective Memory in LLM Agents** *COLM 2026* [[paper](https://arxiv.org/abs/2607.12385)]
- [2026] **ElephantAgent: Contextual State Continuity in Agentic Systems** [[paper](https://arxiv.org/abs/2607.01919)]
- [2026] **RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts** [[paper](https://arxiv.org/abs/2607.16716)]
- [2026] **Supra Cognitive Modes: A Routed Architecture for Agent Memory** [[paper](https://arxiv.org/abs/2607.19096)]
- [2026] **Shared Selective Persistent Memory for Agentic LLM Systems** [[paper](https://arxiv.org/abs/2607.09493)]
- [2026] **MRMS: A Multi-Resolution Memory Substrate for Long-Lived AI Agents** [[paper](https://arxiv.org/abs/2607.04617)]
- [2026] **Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents** [[paper](https://arxiv.org/abs/2607.20972)]
- [2026] **A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory** [[paper](https://arxiv.org/abs/2607.01935)]
- [2026] **Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents** [[paper](https://arxiv.org/abs/2607.12267)]
- [2026] **Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory** [[paper](https://arxiv.org/abs/2607.17545)]
- [2026] **Organizational Memory for Agentic Business Process Execution** [[paper](https://arxiv.org/abs/2607.03228)]
- [2026] **From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space** [[paper](https://arxiv.org/abs/2607.05794)]
- [2026] **The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory** [[paper](https://arxiv.org/abs/2607.10608)]
- [2026] **MemSyco-Bench: Benchmarking Sycophancy in Agent Memory** [[paper](https://arxiv.org/abs/2607.01071)]
- [2026] **Mechanistic Attention Guidance for Agent Memory Refinement** [[paper](https://arxiv.org/abs/2607.17621)]
- [2026] **AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning** [[paper](https://arxiv.org/abs/2607.21106)]
- [2026] **Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation** [[paper](https://arxiv.org/abs/2607.19985)]
- [2026] **Episodic-to-Semantic Consolidation Without Identity Drift** [[paper](https://arxiv.org/abs/2607.01988)]
- [2026] **ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory** [[paper](https://arxiv.org/abs/2607.10350)]
- [2026] **ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended Video Streams** [[paper](https://arxiv.org/abs/2607.09759)]
- [2026] **Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory** [[paper](https://arxiv.org/abs/2607.17879)]
- [2026] **ZifaMem: Structured Memory for Persona, Preference, and Emotional Continuity in AI Companions** [[paper](https://arxiv.org/abs/2607.17564)]
- [2026] **Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration** [[paper](https://arxiv.org/abs/2607.16848)]
- [2026] **KnowAct-GUIClaw: Personal GUI Assistant with Self-Evolving Memory and Skill** [[paper](https://arxiv.org/abs/2607.12625)]
- [2026] **Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents** [[paper](https://arxiv.org/abs/2607.10526)]
- [2026] **Narrative World Model: Narratology-Grounded Writer Memory for Long-Form Fiction** [[paper](https://arxiv.org/abs/2607.05577)]
- [2026] **Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents** [[paper](https://arxiv.org/abs/2607.13157)]
- [2026] **Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory** [[paper](https://arxiv.org/abs/2607.06447)]
- [2026] **RetroAgent: Harnessing LLMs to Search Over Structured Memory for Agentic Retrosynthesis Planning** *COLM 2026* [[paper](https://arxiv.org/abs/2607.14512)]
- [2026] **Homer: Understanding Long-form Videos with Hierarchical Memory and Agentic Reasoning** [[paper](https://arxiv.org/abs/2607.02588)]
- [2026] **Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory** [[paper](https://arxiv.org/abs/2607.05511)]
- [2026] **A hierarchical memory architecture overcomes context limits in long-horizon multi-agent computational modeling** [[paper](https://arxiv.org/abs/2607.07666)]
- [2026] **Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems** [[paper](https://arxiv.org/abs/2607.21503)]
- [2026] **End-to-End LLM Flight Planning with RAG-based Memory and Multi-modal Coach Agent** [[paper](https://arxiv.org/abs/2607.06964)]
- [2026] **What to Keep, What to Forget: A Rate--Distortion View of Memory Compaction in LLMs and Agents** [[paper](https://arxiv.org/abs/2607.08032)]
- [2026] **Why Git Is the Memory Solution for the Agentic Development Lifecycle** [[paper](https://arxiv.org/abs/2607.14390)]
- [2026] **ACM: Agentic Context Management for Long Horizon Tasks** [[paper](https://arxiv.org/abs/2607.23809)]
- [2026] **Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV** [[paper](https://arxiv.org/abs/2607.23693)]
- [2026] **ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in Tool-Using LLM Agents** [[paper](https://arxiv.org/abs/2607.23999)]
- [2026] **ReCon: A Resource-Constrained Benchmark for LLM-Based Cybersecurity Compliance Across Ingestion and Retrieval Pipelines** [[paper](https://arxiv.org/abs/2607.22885)]
- [2026] **SF-AMS: Strategic Forgetting for Structured Memory in LLM Agent** [[paper](https://arxiv.org/abs/2607.22562)]
- [2026] **Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings** [[paper](https://arxiv.org/abs/2607.21962)]
- [2026] **Encoding Invisible Causation for Bridge Diagnostic Agents: Triple-Guided Retrieval-Augmented Fine-Tuning with QLoRA** [[paper](https://arxiv.org/abs/2607.21680)]
- [2026] **AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems** [[paper](https://arxiv.org/abs/2607.21604)]
- [2026] **Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents** [[paper](https://arxiv.org/abs/2607.21125)]
- [2026] **Workflow-Localized Mechanism Learning: Attribution-Guided Repair and Knowledge Reuse for Structured Agent Skills** [[paper](https://arxiv.org/abs/2607.20999)]
- [2026] **TraceDev: A Traceability-Driven Multi-agent Framework for Requirement-to-Code Development** [[paper](https://arxiv.org/abs/2607.18886)]
- [2026] **Formal Verification of an Out-of-Order Multiprocessor against an In-Order Weak-Memory ISA** [[paper](https://arxiv.org/abs/2607.18727)]
- [2026] **Learnable Sequential Memory in Coupled Oscillator Networks** [[paper](https://arxiv.org/abs/2607.18439)]
- [2026] **A Calculus of Discernment: Decision-Relevant Insight, Sequence Value, and Forgetting as Higher-Order Learning** [[paper](https://arxiv.org/abs/2607.18275)]
- [2026] **HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory** [[paper](https://arxiv.org/abs/2607.18141)]
- [2026] **RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning** [[paper](https://arxiv.org/abs/2607.18060)]
- [2026] **Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents** [[paper](https://arxiv.org/abs/2607.18039)]
- [2026] **PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution** [[paper](https://arxiv.org/abs/2607.16636)]
- [2026] **Self-Evolving Just-In-Time Memory for Proactive Embodied Safety** [[paper](https://arxiv.org/abs/2607.16247)]
- [2026] **SkillNav: Score-Level Skill Intervention for Zero-Shot Object Goal Navigation** [[paper](https://arxiv.org/abs/2607.15758)]
- [2026] **Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent** [[paper](https://arxiv.org/abs/2607.14541)]
- [2026] **CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Context Engineering for GenAI Models** [[paper](https://arxiv.org/abs/2607.14396)]
- [2026] **AI Agents Do Not Fail Alone:The Context Fails First** [[paper](https://arxiv.org/abs/2607.14275)]
- [2026] **Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment** [[paper](https://arxiv.org/abs/2607.14047)]
- [2026] **SPyCE: Skill-Policy Co-evolution for Multimodal Agents** [[paper](https://arxiv.org/abs/2607.13854)]
- [2026] **SkillComm: Skill-Driven Semantic Communication for Sequential Workflows via Incremental Token Transmission** [[paper](https://arxiv.org/abs/2607.11972)]
- [2026] **Self-Healing Coordination in Cognitive Swarm Agents with Bloch-Type Perceptual Memory** [[paper](https://arxiv.org/abs/2607.11960)]
- [2026] **Forgetting Our Way to Shared Meaning: Effects of Forgetting on Conceptual Alignment in a Non-Partnership Coordination Game** [[paper](https://arxiv.org/abs/2607.11787)]
- [2026] **Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory** [[paper](https://arxiv.org/abs/2607.11226)]
- [2026] **Feedback-Coupled Memory Systems in Continuous Time** [[paper](https://arxiv.org/abs/2607.09714)]
- [2026] **MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation** [[paper](https://arxiv.org/abs/2606.29914)]
- [2026] **MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory** [[paper](https://arxiv.org/abs/2606.29788)]
- [2026] **When Does Overlap Help? OSU-Mem and a Cell-Conditional Analysis of Trajectory Memory for LLM Agents** [[paper](https://arxiv.org/abs/2606.28376)]
- [2026] **Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One** [[paper](https://arxiv.org/abs/2606.25449)]
- [2026] **RAVEN: Long-Horizon Reasoning &amp; Navigation with a Visuo-Spatio-Temporal Memory** [[paper](https://arxiv.org/abs/2606.25206)]
- [2026] **MemTrace: Probing What Final Accuracy Misses in Long-Term Memory** [[paper](https://arxiv.org/abs/2606.17328)]
- [2026] **eMEM: A Hybrid Spatio-Temporal Memory System For Embodied Agents** [[paper](https://arxiv.org/abs/2606.03374)]
- [2026] **PhotoCraft: Agentic Reasoning with Hierarchical Self-Evolving Memory for Deep Image Search** [[paper](https://arxiv.org/abs/2606.03099)]
- [2026] **Don&#39;t Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution** [[paper](https://arxiv.org/abs/2606.01435)]
- [2026] **MRMMIA: Membership Inference Attacks on Memory in Chat Agents** [[paper](https://arxiv.org/abs/2605.27825)]
- [2026] **MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts** [[paper](https://arxiv.org/abs/2605.20926)]
- [2026] **Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction** [[paper](https://arxiv.org/abs/2605.18729)]
- [2026] **SocialMemBench: Are AI Memory Systems Ready for Social Group Settings?** [[paper](https://arxiv.org/abs/2605.17789)]
- [2026] **LASAR: Towards Spatio-temporal Reasoning with Latent Cognitive Map** [[paper](https://arxiv.org/abs/2605.16899)]
- [2026] **The Trap of Trajectory: Towards Understanding and Mitigating Spurious Correlations in Agentic Memory** [[paper](https://arxiv.org/abs/2605.09330)]
- [2026] **MemCompiler: Compile, Don&#39;t Inject -- State-Conditioned Memory for Embodied Agents** [[paper](https://arxiv.org/abs/2605.07594)]
- [2026] **MiA-Signature: Approximating Global Activation for Long-Context Understanding** [[paper](https://arxiv.org/abs/2605.06416)]
- [2026] **From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction** [[paper](https://arxiv.org/abs/2604.27906)]
- [2026] **Contextual Agentic Memory is a Memo, Not True Memory** [[paper](https://arxiv.org/abs/2604.27707)]
- [2026] **BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning** [[paper](https://arxiv.org/abs/2604.16331)]
- [2026] **MemExplorer: Navigating the Heterogeneous Memory Design Space for Agentic Inference NPUs** [[paper](https://arxiv.org/abs/2604.16007)]
- [2026] **FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion** [[paper](https://arxiv.org/abs/2606.15609)]
- [2026] **Memory-Induced Tool-Drift in LLM Agents** [[paper](https://arxiv.org/abs/2605.24941)]
- [2026] **MEMAUDIT: An Exact Package-Oracle Evaluation Protocol for Budgeted Long-Term LLM Memory Writing** [[paper](https://arxiv.org/abs/2605.02199)]
- [2026] **Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems** [[paper](https://arxiv.org/abs/2604.20795)]
- [2026] **Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation** [[paper](https://arxiv.org/abs/2604.15391)]
- [2026] **MemX: A Local-First Long-Term Memory System for AI Assistants** [[paper](https://arxiv.org/abs/2603.16171)]
- [2026] **KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization** [[paper](https://arxiv.org/abs/2603.10085)]
- [2026] **LifeBench: A Benchmark for Long-Horizon Multi-Source Memory** [[paper](https://arxiv.org/abs/2603.03781)]
- [2026] **EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use** [[paper](https://arxiv.org/abs/2602.15329)]
- [2026] **STaR: Scalable Task-Conditioned Retrieval for Long-Horizon Multimodal Robot Memory** [[paper](https://arxiv.org/abs/2602.09255)]
- [2026] **How Implicit Bias Accumulates and Propagates in LLM Long-term Memory** [[paper](https://arxiv.org/abs/2602.01558)]
- [2026] **MemRefine: LLM-Guided Compression for Long-Term Agent Memory** [[paper](https://arxiv.org/abs/2606.13177)]
- [2026] **Joint Agent Memory and Exploration Learning via Novelty Signals** [[paper](https://arxiv.org/abs/2606.01528)]
- [2026] **DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation** [[paper](https://arxiv.org/abs/2606.29961)]
- [2026] **When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents** [[paper](https://arxiv.org/abs/2606.06055)]
- [2026] **Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline** [[paper](https://arxiv.org/abs/2606.04315)]
- [2026] **Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents** [[paper](https://arxiv.org/abs/2606.04555)]
- [2026] **What Must Generalist Agents Remember?** [[paper](https://arxiv.org/abs/2606.18746)]
- [2026] **When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense** [[paper](https://arxiv.org/abs/2606.22030)]
- [2026] **Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents** [[paper](https://arxiv.org/abs/2606.11680)]
- [2026] **Context-Driven Incremental Compression for Multi-Turn Dialogue Generation** *ICML 2026* [[paper](https://arxiv.org/abs/2606.12411)]
- [2026] **ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning** [[paper](https://arxiv.org/abs/2606.10532)]
- [2026] **Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents** [[paper](https://arxiv.org/abs/2606.10616)]
- [2026] **ECHO: Prune To Act, Trace To Learn With Selective Turn Memory In Agentic RL** [[paper](https://arxiv.org/abs/2606.31650)]
- [2026] **WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents** [[paper](https://arxiv.org/abs/2606.18847)]
- [2026] **SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents** [[paper](https://arxiv.org/abs/2606.05761)]
- [2026] **DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection** [[paper](https://arxiv.org/abs/2606.27499)]
- [2026] **HMARS: A Hierarchical Multi-Agent Memory System for Long-Context Reasoning** [[paper](https://arxiv.org/abs/2606.28349)]
- [2026] **H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions** [[paper](https://arxiv.org/abs/2606.09461)]
- [2026] **M3Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions** [[paper](https://arxiv.org/abs/2606.07402)]
- [2026] **MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism** [[paper](https://arxiv.org/abs/2606.07512)]
- [2026] **ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling** [[paper](https://arxiv.org/abs/2606.24437)]
- [2026] **SpaceVLN: A Zero-Shot Vision-and-Language Navigation Agent with Online Spatial Cognitive Memory and Reasoning** [[paper](https://arxiv.org/abs/2606.08992)]
- [2026] **GOPAgen: Motion-Aware and Efficient Agentic Long-Video Understanding with Structural Memory and Hierarchical Reasoning** [[paper](https://arxiv.org/abs/2606.06532)]
- [2026] **Compressing Observation History into Agent Memory: Distilling Transformers into Recurrent Transformers** [[paper](https://arxiv.org/abs/2606.21562)]
- [2026] **TokenPilot: Cache-Efficient Context Management for LLM Agents** [[paper](https://arxiv.org/abs/2606.17016)]
- [2026] **Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory** [[paper](https://arxiv.org/abs/2606.23195)]
- [2026] **H-Mem: A Novel Memory Mechanism for Evolving and Retrieving Agent Memory via a Hybrid Structure** [[paper](https://arxiv.org/abs/2605.15701)]
- [2026] **What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis** [[paper](https://arxiv.org/abs/2605.03354)]
- [2026] **Executable Agentic Memory for GUI Agent** [[paper](https://arxiv.org/abs/2605.12294)]
- [2026] **DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA** [[paper](https://arxiv.org/abs/2605.22411)]
- [2026] **CogniFold: Always-On Proactive Memory via Cognitive Folding** [[paper](https://arxiv.org/abs/2605.13438)]
- [2026] **Useful Memories Become Faulty When Continuously Updated by LLMs** [[paper](https://arxiv.org/abs/2605.12978)]
- [2026] **ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting** [[paper](https://arxiv.org/abs/2605.03804)]
- [2026] **SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent** [[paper](https://arxiv.org/abs/2605.24468)]
- [2026] **MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory** [[paper](https://arxiv.org/abs/2605.03228)]
- [2026] **CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems** [[paper](https://arxiv.org/abs/2606.00756)]
- [2026] **MemFail: Stress-Testing Failure Modes of LLM Memory Systems** [[paper](https://arxiv.org/abs/2605.26667)]
- [2026] **MemRepair: Hierarchical Memory for Agentic Repository-Level Vulnerability Repair** [[paper](https://arxiv.org/abs/2605.17444)]
- [2026] **The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents** [[paper](https://arxiv.org/abs/2605.08060)]
- [2026] **MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading** [[paper](https://arxiv.org/abs/2605.10268)]
- [2026] **PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails** [[paper](https://arxiv.org/abs/2607.20482)]
- [2026] **MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory** [[paper](https://arxiv.org/abs/2605.15128)]
- [2026] **MemFlow: Intent-Driven Memory Orchestration for Small Language Model Agents** [[paper](https://arxiv.org/abs/2605.03312)]
- [2026] **Evaluating Memory Condensation Strategies for Coding Agents in Data-Driven Scientific Discovery** [[paper](https://arxiv.org/abs/2605.18854)]
- [2026] **MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented Generation** [[paper](https://arxiv.org/abs/2606.00610)]
- [2026] **Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory** [[paper](https://arxiv.org/abs/2606.01385)]
- [2026] **Symbolic Reasoning Frameworks Trigger Memory-Mediated Ecosystem Dynamics in Multi-Agent LLM Systems** [[paper](https://arxiv.org/abs/2606.07552)]
- [2026] **MedMemoryBench: Benchmarking Agent Memory in Personalized Healthcare** [[paper](https://arxiv.org/abs/2605.11814)]
- [2026] **SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory** [[paper](https://arxiv.org/abs/2605.15710)]
- [2026] **Personalize-then-Store: Benchmarking and Learning Personalized Memory for Long-horizon Agents** [[paper](https://arxiv.org/abs/2605.25535)]
- [2026] **MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents** [[paper](https://arxiv.org/abs/2605.03675)]
- [2026] **Entity-Collision: A Stratified Protocol for Attributing Retrieval Lift in Agent Memory** [[paper](https://arxiv.org/abs/2605.29630)]
- [2026] **Momento: Evaluating Persistent Memory and Reasoning with Multi-Session Agentic Conversations** [[paper](https://arxiv.org/abs/2606.00832)]
- [2026] **VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions** [[paper](https://arxiv.org/abs/2605.27141)]
- [2026] **MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing** [[paper](https://arxiv.org/abs/2605.23986)]
- [2026] **MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems** [[paper](https://arxiv.org/abs/2605.18565)]
- [2026] **Lightweight LLM Agent Memory with Small Language Models** *ACL 2026* [[paper](https://arxiv.org/abs/2604.07798)]
- [2026] **LightThinker++: From Reasoning Compression to Memory Management** [[paper](https://arxiv.org/abs/2604.03679)]
- [2026] **FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory** [[paper](https://arxiv.org/abs/2604.20300)]
- [2026] **SuperLocalMemory V3.3: The Living Brain -- Biologically-Inspired Forgetting, Cognitive Quantization, and Multi-Channel Retrieval for Zero-LLM Agent Memory Systems** *https://doi.org/10.5281/zenodo.19435120* [[paper](https://arxiv.org/abs/2604.04514)]
- [2026] **Escaping the Context Bottleneck: Active Context Curation for LLM Agents via Reinforcement Learning** [[paper](https://arxiv.org/abs/2604.11462)]
- [2026] **Aligning Progress and Feasibility: A Neuro-Symbolic Dual Memory Framework for Long-Horizon LLM Agents** [[paper](https://arxiv.org/abs/2604.02734)]
- [2026] **Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents** [[paper](https://arxiv.org/abs/2604.27283)]
- [2026] **MemReader: From Passive to Active Extraction for Long-Term Agent Memory** [[paper](https://arxiv.org/abs/2604.07877)]
- [2026] **Joint Optimization of Reasoning and Dual-Memory for Self-Learning Diagnostic Agent** [[paper](https://arxiv.org/abs/2604.07269)]
- [2026] **ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context** [[paper](https://arxiv.org/abs/2604.01599)]
- [2026] **ATANT v1.1: Positioning Continuity Evaluation Against Memory, Long-Context, and Agentic-Memory Benchmarks** [[paper](https://arxiv.org/abs/2604.10981)]
- [2026] **Rashomon Memory: Towards Argumentation-Driven Retrieval for Multi-Perspective Agent Memory** [[paper](https://arxiv.org/abs/2604.03588)]
- [2026] **StreamMeCo: Long-Term Agent Memory Compression for Efficient Streaming Video Understanding** [[paper](https://arxiv.org/abs/2604.09000)]
- [2026] **AffectAgent: Collaborative Multi-Agent Reasoning for Retrieval-Augmented Multimodal Emotion Recognition** [[paper](https://arxiv.org/abs/2604.12735)]
- [2026] **Stateless Decision Memory for Enterprise AI Agents** [[paper](https://arxiv.org/abs/2604.20158)]
- [2026] **: Benchmarking AI Agents for Long-Term Planning and Consistent Execution** [[paper](https://arxiv.org/abs/2604.01212)]
- [2026] **CraniMem: Cranial Inspired Gated and Bounded Memory for Agentic Systems** [[paper](https://arxiv.org/abs/2603.15642)] [[code](https://github.com/PearlMody05/Cranimem)]
- [2026] **Did You Check the Right Pocket? Cost-Sensitive Store Routing for Memory-Augmented Agents** *ICLR 2026 Workshop on Memory for LLM-Based Agentic Systems* [[paper](https://arxiv.org/abs/2603.15658)]
- [2026] **AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations** [[paper](https://arxiv.org/abs/2603.01966)]
- [2026] **Oblivion: Self-Adaptive Agentic Memory Control through Decay-Driven Activation** [[paper](https://arxiv.org/abs/2604.00131)]
- [2026] **ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory** *https://doi.org/10.1145/3770855.3818931* [[paper](https://arxiv.org/abs/2603.26182)]
- [2026] **Enhancing Web Agents with a Hierarchical Memory Tree** [[paper](https://arxiv.org/abs/2603.07024)]
- [2026] **Hybrid Self-evolving Structured Memory for GUI Agents** [[paper](https://arxiv.org/abs/2603.10291)]
- [2026] **Memento-Skills: Let Agents Design Agents** [[paper](https://arxiv.org/abs/2603.18743)]
- [2026] **MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games** [[paper](https://arxiv.org/abs/2603.09022)]
- [2026] **MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution** [[paper](https://arxiv.org/abs/2603.18718)]
- [2026] **Multi-Layered Memory Architectures for LLM Agents: An Experimental Evaluation of Long-Term Context Retention** [[paper](https://arxiv.org/abs/2603.29194)]
- [2026] **Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval** [[paper](https://arxiv.org/abs/2603.10700)]
- [2026] **FluxMem: Choosing How to Remember: Adaptive Memory Structures for LLM Agents** [[paper](https://arxiv.org/abs/2602.14038)]
- [2026] **BudgetMem: Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory** [[paper](https://arxiv.org/abs/2602.06025)] [[code](https://github.com/ViktorAxelsen/BudgetMem)]
- [2026] **EMPO2: Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization** [[paper](https://arxiv.org/abs/2602.23008)]
- [2026] **Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations** [[paper](https://arxiv.org/abs/2602.19320)]
- [2026] **TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking** [[paper](https://arxiv.org/abs/2602.03224)]
- [2026] **Fix the Structural Bottleneck: Context Compression via Explicit Information Transmission** [[paper](https://arxiv.org/abs/2602.03784)]
- [2026] **ES-MemEval: Benchmarking Conversational Agents on Personalized Long-Term Emotional Support** *https://doi.org/10.1145/3774904.3792143* [[paper](https://arxiv.org/abs/2602.01885)]
- [2026] **MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments** [[paper](https://arxiv.org/abs/2602.06075)]
- [2026] **AI Agent Systems for Supply Chains: Structured Decision Prompts and Memory Retrieval** [[paper](https://arxiv.org/abs/2602.05524)]
- [2026] **ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory** [[paper](https://arxiv.org/abs/2602.20502)]
- [2026] **Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents** [[paper](https://arxiv.org/abs/2601.01885)]
- [2026] **MemoBrain: Executive Memory as an Agentic Brain for Reasoning** *ACL 2026 Findings* [[paper](https://arxiv.org/abs/2601.08079)]
- [2026] **Chain-of-Memory: Lightweight Memory Construction with Dynamic Evolution for LLM Agents** *ACL 2026* [[paper](https://arxiv.org/abs/2601.14287)]
- [2026] **Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management** *ACL 2026* [[paper](https://arxiv.org/abs/2601.08435)]
- [2026] **Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents** [[paper](https://arxiv.org/abs/2601.19935)]
- [2026] **Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents** [[paper](https://arxiv.org/abs/2601.03515)]
- [2026] **LLMs Can't Play Hangman: On the Necessity of a Private Working Memory for Language Agents** [[paper](https://arxiv.org/abs/2601.06973)]
- [2026] **LSTM-MAS: A Long Short-Term Memory Inspired Multi-Agent System for Long-Context Understanding** [[paper](https://arxiv.org/abs/2601.11913)]
- [2026] **Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution** [[paper](https://arxiv.org/abs/2601.22528)]
- [2026] **MERMAID: Memory-Enhanced Retrieval and Reasoning with Multi-Agent Iterative Knowledge Grounding for Veracity Assessment** [[paper](https://arxiv.org/abs/2601.22361)]
- [2026] **EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents** [[paper](https://arxiv.org/abs/2601.16690)]
- [2026] **Cross-Modal Memory Compression for Efficient Multi-Agent Debate** [[paper](https://arxiv.org/abs/2602.00454)]
- [2026] **ScaleSim: Serving Large-Scale Multi-Agent Simulation with Invocation Distance-Based Memory Management** [[paper](https://arxiv.org/abs/2601.21473)]
- [2026] **MiTa: A Hierarchical Multi-Agent Collaboration Framework with Memory-integrated and Task Allocation** [[paper](https://arxiv.org/abs/2601.22974)]
- [2026] **Warp-Cortex: An Asynchronous, Memory-Efficient Architecture for Million-Agent Cognitive Scaling on Consumer Hardware** [[paper](https://arxiv.org/abs/2601.01298)]
- [2026] **Toward Efficient Agents: Memory, Tool learning, and Planning** [[paper](https://arxiv.org/abs/2601.14192)]
- [2026] **Agentic Memory Enhanced Recursive Reasoning for Root Cause Localization in Microservices** *https://doi.org/10.1145/3786583.3786853* [[paper](https://arxiv.org/abs/2601.02732)]
- [2026] **Field-Theoretic Memory for AI Agents: Continuous Dynamics for Context Preservation** [[paper](https://arxiv.org/abs/2602.21220)]
- [2026] **Active Context Compression: Autonomous Memory Management in LLM Agents** [[paper](https://arxiv.org/abs/2601.07190)]
- [2026] **MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents** [[paper](https://arxiv.org/abs/2601.05215)]

##### 2025

- [2025] **Beyond Heuristics: A Decision-Theoretic Framework for Agent Memory Management** [[paper](https://arxiv.org/abs/2512.21567)]
- [2025] **QwenLong-L1.5: Post-Training Recipe for Long-Context Reasoning and Memory Management** [[paper](https://arxiv.org/abs/2512.12967)]
- [2025] **AOI: Context-Aware Multi-Agent Operations via Dynamic Scheduling and Hierarchical Memory Compression** [[paper](https://arxiv.org/abs/2512.13956)]
- [2025] **Forgetful but Faithful: A Cognitive Memory Architecture and Benchmark for Privacy-Aware Generative Agents** [[paper](https://arxiv.org/abs/2512.12856)]
- [2025] **VideoARM: Agentic Reasoning over Hierarchical Memory for Long-Form Video Understanding** [[paper](https://arxiv.org/abs/2512.12360)]
- [2025] **Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks** [[paper](https://arxiv.org/abs/2510.12635)]
- [2025] **IterResearch: Rethinking Long-Horizon Agents via Markovian State Reconstruction** [[paper](https://arxiv.org/abs/2511.07327)]
- [2025] **MemSearcher: Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning** [[paper](https://arxiv.org/abs/2511.02805)]
- [2025] **History-Aware Reasoning for GUI Agents** [[paper](https://arxiv.org/abs/2511.09127)]
- [2025] **Multi-agent In-context Coordination via Decentralized Memory Retrieval** *https://doi.org/10.1609/aaai.v40i27.39394* [[paper](https://arxiv.org/abs/2511.10030)]
- [2025] **EvoMem: Improving Multi-Agent Planning with Dual-Evolving Memory** [[paper](https://arxiv.org/abs/2511.01912)]
- [2025] **A Benchmark for Procedural Memory Retrieval in Language Agents** [[paper](https://arxiv.org/abs/2511.21730)]
- [2025] **HaluMem: Evaluating Hallucinations in Memory Systems of Agents** [[paper](https://arxiv.org/abs/2511.03506)]
- [2025] **AgentFold: Long-Horizon Web Agents with Proactive Context Management** [[paper](https://arxiv.org/abs/2510.24699)]
- [2025] **PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning** [[paper](https://arxiv.org/abs/2509.22315)]
- [2025] **Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval** [[paper](https://arxiv.org/abs/2506.03141)]
- [2025] **DeepAgent: A General Reasoning Agent with Scalable Toolsets** [[paper](https://arxiv.org/abs/2510.21618)]
- [2025] **ACON: Optimizing Context Compression for Long-Horizon LLM Agents** [[paper](https://arxiv.org/abs/2510.00615)]
- [2025] **MGA: Memory-Driven GUI Agent for Observation-Centric Interaction** [[paper](https://arxiv.org/abs/2510.24168)]
- [2025] **Agent-ScanKit: Unraveling Memory and Reasoning of Multimodal Agents via Sensitivity Perturbations** [[paper](https://arxiv.org/abs/2510.00496)]
- [2025] **ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization** [[paper](https://arxiv.org/abs/2509.13313)]
- [2025] **Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents** *ICLR 2026* [[paper](https://arxiv.org/abs/2509.23040)]
- [2025] **Memory Management and Contextual Consistency for Long-Running Low-Code Agents** [[paper](https://arxiv.org/abs/2509.25250)]
- [2025] **Shell or Nothing: Real-World Benchmarks and Memory-Activated Agents for Automated Penetration Testing** [[paper](https://arxiv.org/abs/2509.09207)]
- [2025] **Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management** [[paper](https://arxiv.org/abs/2508.04664)]
- [2025] **Coarse-to-Fine Grounded Memory for LLM Agent Planning** [[paper](https://arxiv.org/abs/2508.15305)]
- [2025] **Narrative Memory in Machines: Multi-Agent Arc Extraction in Serialized TV** [[paper](https://arxiv.org/abs/2508.07010)]
- [2025] **MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent** [[paper](https://arxiv.org/abs/2507.02259)]
- [2025] **MemoCue: Empowering LLM-Based Agents for Human Memory Recall via Strategy-Guided Querying** [[paper](https://arxiv.org/abs/2507.23633)]
- [2025] **Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents** [[paper](https://arxiv.org/abs/2506.14852)]
- [2025] **Task Memory Engine: Spatial Memory for Robust Multi-Step LLM Agents** [[paper](https://arxiv.org/abs/2505.19436)]
- [2025] **MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning** [[paper](https://arxiv.org/abs/2505.20096)]
- [2025] **CAIM: Development and Evaluation of a Cognitive AI Memory Framework for Long-Term Interaction with Intelligent Agents** [[paper](https://arxiv.org/abs/2505.13044)]
- [2025] **Agentic Feature Augmentation: Unifying Selection and Generation with Teaming, Planning, and Memories** [[paper](https://arxiv.org/abs/2505.15076)]
- [2025] **Efficiently Enhancing General Agents With Hierarchical-categorical Memory** [[paper](https://arxiv.org/abs/2505.22006)]
- [2025] **Interpretable Locomotion Prediction in Construction Using a Memory-Driven LLM Agent With Chain-of-Thought Reasoning** [[paper](https://arxiv.org/abs/2504.15263)]
- [2025] **Echo: A Large Language Model with Temporal Episodic Memory** [[paper](https://arxiv.org/abs/2502.16090)]
- [2025] **Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG** [[paper](https://arxiv.org/abs/2501.09136)]
- [2025] **GeAR: Graph-enhanced Agent for Retrieval-augmented Generation** [[paper](https://doi.org/https://doi.org/10.18653/v1/2025.findings-acl.624)]
- [2025] **ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents** [[paper](https://doi.org/https://doi.org/10.18653/v1/2025.emnlp-main.464)]

##### 2024

- [2024] **Unraveling the Complexity of Memory in RL Agents: an Approach for Classification and Evaluation** [[paper](https://arxiv.org/abs/2412.06531)]
- [2024] **HiMemFormer: Hierarchical Memory-Aware Transformer for Multi-Agent Action Anticipation** *NeurIPS 2024* [[paper](https://arxiv.org/abs/2411.01455)]
- [2024] **Agent S: An Open Agentic Framework That Uses Computers Like a Human** [[paper](https://arxiv.org/abs/2410.08164)]
- [2024] **Emotional RAG: Enhancing Role-Playing Agents through Emotional Retrieval** [[paper](https://arxiv.org/abs/2410.23041)]
- [2024] **GEM-RAG: Graphical Eigen Memories For Retrieval Augmented Generation** [[paper](https://arxiv.org/abs/2409.15566)]
- [2024] **Towards a Realistic Long-Term Benchmark for Open-Web Research Agents** [[paper](https://arxiv.org/abs/2409.14913)]
- [2024] **HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model** [[paper](https://arxiv.org/abs/2408.09559)]
- [2024] **Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks** [[paper](https://arxiv.org/abs/2408.03615)]
- [2024] **TaskGen: A Task-Based, Memory-Infused Agentic Framework using StrictJSON** [[paper](https://arxiv.org/abs/2407.15734)]
- [2024] **Retrieval-Augmented Generation and LLM Agents for Biomimicry Design Solutions** [[paper](https://doi.org/https://doi.org/10.1609/aaaiss.v3i1.31210)]
- [2024] **Evaluating Very Long-Term Conversational Memory of LLM Agents** [[paper](https://arxiv.org/abs/2402.17753)]
- [2024] **RAP: Retrieval-Augmented Planning with Contextual Memory for Multimodal LLM Agents** [[paper](https://arxiv.org/abs/2402.03610)]

##### 2023

- [2023] **Empowering Working Memory for Large Language Model Agents** [[paper](https://arxiv.org/abs/2312.17259)]
- [2023] **Persistent memory for AI coding agents: a pre-registered SWE-bench Verified benchmark** [[paper](https://arxiv.org/abs/2310.06770)]
- [2023] **Memory Gym: Towards Endless Tasks to Benchmark Memory Capabilities of Agents** *JMLR* [[paper](https://arxiv.org/abs/2309.17207)]

##### 2011

- [2011] **Agent based reasoning for the non-linear stochastic models of long-range memory** *https://doi.org/10.1016/j.physa.2011.08.061* [[paper](https://arxiv.org/abs/1106.2685)]

[⬆ Back to top](#paper-list)

#### Parametric

##### 2026

- [2026] **MemTX: Transactional Belief Commit for Stateful Agent Memory** [[paper](https://arxiv.org/abs/2607.23929)]
- [2026] **The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL** [[paper](https://arxiv.org/abs/2607.19749)]
- [2026] **Memory Merge DQN: Sensitivity Weighted Target Updates for Stable Value Learning** [[paper](https://arxiv.org/abs/2607.19397)]
- [2026] **In-Context Reinforcement Learning under Non-Stationarity: A Survey** [[paper](https://arxiv.org/abs/2607.11906)]
- [2026] **MolMem: Memory-Augmented Agentic Reinforcement Learning for Sample-Efficient Molecular Optimization** [[paper](https://arxiv.org/abs/2604.12237)]
- [2026] **Social Hippocampus Memory Learning** [[paper](https://arxiv.org/abs/2603.25614)]
- [2026] **Explore with Long-term Memory: A Benchmark and Multimodal LLM-based Reinforcement Learning Framework for Embodied Exploration** [[paper](https://arxiv.org/abs/2601.10744)]
- [2026] **Learning to Remember: End-to-End Training of Memory Agents for Long-Context Reasoning** [[paper](https://arxiv.org/abs/2602.18493)]

##### 2024

- [2024] **Various Lengths, Constant Speed: Efficient Language Modeling with Lightning Attention** [[paper](https://openreview.net/forum?id=5wm6TiUP4X)]
- [2024] **Efficient Streaming Language Models with Attention Sinks** [[paper](https://openreview.net/forum?id=NG7sS51zVF)]

[⬆ Back to top](#paper-list)

#### Latent

##### 2026

- [2026] **Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents** [[paper](https://arxiv.org/abs/2607.08395)]
- [2026] **Akashic: A Low-Overhead LLM Inference Service with MemAttention** [[paper](https://arxiv.org/abs/2607.05708)]
- [2026] **Memory-Conditioned Tool Calling for Camera-First Visual Agents** [[paper](https://arxiv.org/abs/2607.09822)]
- [2026] **ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair** [[paper](https://arxiv.org/abs/2607.01916)]
- [2026] **MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference** [[paper](https://arxiv.org/abs/2607.10582)]
- [2026] **AAFLOW+ Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows** [[paper](https://arxiv.org/abs/2607.10987)]
- [2026] **KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling** [[paper](https://arxiv.org/abs/2607.09153)]
- [2026] **Co-Evolving Graph and Text Memory for Training-Free Multi-Hop Question Answering** [[paper](https://arxiv.org/abs/2607.23278)]
- [2026] **Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability** [[paper](https://arxiv.org/abs/2605.22142)]
- [2026] **Engram: A Bi-Temporal Memory Engine for LLM Agents** [[paper](https://arxiv.org/abs/2606.09900)]
- [2026] **DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings** [[paper](https://arxiv.org/abs/2606.22877)]
- [2026] **Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering** [[paper](https://arxiv.org/abs/2606.10921)]
- [2026] **MADRAG: Multi-Agent Debate with Retrieval-Augmented Generation for Training-Free Analytic Essay Scoring** [[paper](https://arxiv.org/abs/2606.06754)]
- [2026] **IntentKV: Cross-Turn Intent-Aware KV Cache Pruning for Agent Inference** [[paper](https://arxiv.org/abs/2606.09916)]
- [2026] **InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain** [[paper](https://arxiv.org/abs/2606.03329)]
- [2026] **Human-Inspired Memory Architecture for LLM Agents** [[paper](https://arxiv.org/abs/2605.08538)]
- [2026] **TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks** [[paper](https://arxiv.org/abs/2605.17170)]
- [2026] **SCM: Sleep-Consolidated Memory with Algorithmic Forgetting for Large Language Models** [[paper](https://arxiv.org/abs/2604.20943)]
- [2026] **PRIME: Training Free Proactive Reasoning via Iterative Memory Evolution for User-Centric Agent** [[paper](https://arxiv.org/abs/2604.07645)]
- [2026] **CodeComp: Structural KV Cache Compression for Agentic Coding** [[paper](https://arxiv.org/abs/2604.10235)]
- [2026] **ForkKV: Scaling Multi-LoRA Agent Serving via Copy-on-Write Disaggregated KV Cache** [[paper](https://arxiv.org/abs/2604.06370)]
- [2026] **Neural Paging: Learning Context Management Policies for Turing-Complete Agents** [[paper](https://arxiv.org/abs/2603.02228)]
- [2026] **DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity** [[paper](https://arxiv.org/abs/2602.08005)]
- [2026] **Learning to Evict from Key-Value Cache** [[paper](https://arxiv.org/abs/2602.10238)]
- [2026] **SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning** [[paper](https://arxiv.org/abs/2602.22603)]
- [2026] **Efficient Long-Horizon GUI Agents via Training-Free KV Cache Compression** [[paper](https://arxiv.org/abs/2603.00188)]
- [2026] **LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents** [[paper](https://arxiv.org/abs/2602.01053)]
- [2026] **Continuum Memory Architectures for Long-Horizon LLM Agents** [[paper](https://arxiv.org/abs/2601.09913)]

##### 2025

- [2025] **VisMem: Latent Vision Memory Unlocks Potential of Vision-Language Models** [[paper](https://arxiv.org/abs/2511.11007)]
- [2025] **MemGen: Weaving Generative Latent Memory for Self-Evolving Agents** [[paper](https://arxiv.org/abs/2509.24704)]
- [2025] **Conflict-Aware Soft Prompting for Retrieval-Augmented Generation** [[paper](https://arxiv.org/abs/2508.15253)]
- [2025] **MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation** [[paper](https://arxiv.org/abs/2508.19236)]
- [2025] **GraphCogent: Mitigating LLMs' Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding** [[paper](https://arxiv.org/abs/2508.12379)]
- [2025] **MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents** [[paper](https://arxiv.org/abs/2506.15841)]
- [2025] **Mem4Nav: Boosting Vision-and-Language Navigation with Hierarchical Spatial-Cognition Memory** [[paper](https://arxiv.org/abs/2506.19433)]
- [2025] **RazorAttention: Efficient KV Cache Compression Through Retrieval Heads** [[paper](https://openreview.net/forum?id=tkiZQlL04w)]
- [2025] **MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation** [[paper](https://doi.org/10.1145/3696410.3714805)]
- [2025] **SnapKV: LLM Knows What You are Looking for Before Generation** [[paper](https://papers.nips.cc/paper_files/paper/2024/hash/28ab418242603e0f7323e54185d19bde-Abstract-Conference.html)]
- [2025] **LM2: Large Memory Models** [[paper](https://arxiv.org/abs/2502.06049)]
- [2025] **Time-VLM: Exploring Multimodal Vision-Language Models for Augmented Time Series Forecasting** [[paper](https://arxiv.org/abs/2502.04395)]
- [2025] **Titans: Learning to Memorize at Test Time** [[paper](https://arxiv.org/abs/2501.00663)]
- [2025] **SoftCoT: Soft Chain-of-Thought for Efficient Reasoning with LLMs** [[paper](https://aclanthology.org/2025.acl-long.1137/)]

##### 2024

- [2024] **Memory-Augmented Agent Training for Business Document Understanding** [[paper](https://arxiv.org/abs/2412.15274)]
- [2024] **Augmenting Language Models with Long-Term Memory** [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/ebd82705f44793b6f9ade5a669d0f0bf-Abstract-Conference.html)]
- [2024] **Taking a Deep Breath: Enhancing Language Modeling of Large Language Models with Sentinel Tokens** [[paper](https://doi.org/10.18653/v1/2024.findings-emnlp.233)]
- [2024] **Adapting Language Models to Compress Contexts** [[paper](https://doi.org/10.18653/v1/2023.emnlp-main.232)]
- [2024] **Learning to Compress Prompts with Gist Tokens** [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/3d77c6dcc7f143aa2154e7f4d5e22d68-Abstract-Conference.html)]
- [2024] **Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time** [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/a452a7c6c463e4ae8fbdc614c6e983e6-Abstract-Conference.html)]
- [2024] **Focused Transformer: Contrastive Training for Context Scaling** [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/8511d06d5590f4bda24d42087802cc81-Abstract-Conference.html)]

##### 2023

- [2023] **Think-in-Memory: Recalling and Post-thinking Enable LLMs with Long-Term Memory** [[paper](https://arxiv.org/abs/2311.08719)]
- [2023] **In-Context Autoencoder for Context Compression in a Large Language Model** [[paper](https://arxiv.org/abs/2307.06945)]
- [2023] **H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models** [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html)]
- [2023] **Think Before You Act: Decision Transformers with Working Memory** *ICML 2024* [[paper](https://arxiv.org/abs/2305.16338)]

##### 2022

- [2022] **Memorizing Transformers** [[paper](https://openreview.net/forum?id=TrjbxzRcnf-)]
- [2022] **XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model** [[paper](https://arxiv.org/abs/2207.07115)]

[⬆ Back to top](#paper-list)

## 🔗 Related Projects

- [Agent Memory Benchmark (AMBench)](https://github.com/tobias-weiss-ai-xr/agent-memory-bench) — Unified benchmark for agent memory systems covering all 27 taxonomy cells
- [Agentic VR Survey](https://github.com/tobias-weiss-ai-xr/agentic-vr-research) — Living survey of 4,942 agentic AI in VR papers
- [Skill Survey](https://github.com/tobias-weiss-ai-xr/agent-skill-research) — Living survey of AI agent skills (tool use, planning, reasoning, code generation, etc.)
- [Skill Bench](https://github.com/tobias-weiss-ai-xr/agent-skill-bench) — Unified benchmark for evaluating AI agent skills

## 📖 Citation

If you find this repository helpful, please cite the original survey paper:

```bibtex
@article{DBLP:journals/corr/abs-2512-13564,
  author       = {Yuyang Hu and Shichun Liu and Yanwei Yue and Guibin Zhang and Boyang Liu and Fangyi Zhu and Jiahang Lin and Honglin Guo and Shihan Dou and Zhiheng Xi and Senjie Jin and Jiejun Tan and Yanbin Yin and Jiongnan Liu and Zeyu Zhang and Zhongxiang Sun and Yutao Zhu and Hao Sun and Boci Peng and Zhenrong Cheng and Xuanbo Fan and Jiaxin Guo and Xinlei Yu and Zhenhong Zhou and Zewen Hu and Jiahao Huo and Junhao Wang and Yuwei Niu and Yu Wang and Zhenfei Yin and Xiaobin Hu and Yue Liao and Qiankun Li and Kun Wang and Wangchunshu Zhou and Yixin Liu and Dawei Cheng and Qi Zhang and Tao Gui and Shirui Pan and Yan Zhang and Philip Torr and Zhicheng Dou and Ji{-}Rong Wen and Xuanjing Huang and Yu{-}Gang Jiang and Shuicheng Yan},
  title        = {Memory in the Age of {AI} Agents},
  journal      = {CoRR},
  volume       = {abs/2512.13564},
  year         = {2025},
  url          = {https://doi.org/10.48550/arXiv.2512.13564},
  doi          = {10.48550/ARXIV.2512.13564},
  eprinttype    = {arXiv},
  eprint       = {2512.13564},
  timestamp    = {Mon, 26 Jan 2026 16:10:18 +0100},
  biburl       = {https://dblp.org/rec/journals/corr/abs-2512-13564.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```

## ⭐️ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=tobias-weiss-ai-xr/agent-memory-research&type=date&legend=top-left)](https://www.star-history.com/#Shichun-Liu/Agent-Memory-Paper-List&type=date&legend=top-left)

