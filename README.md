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
- [2026/06] 📄 **Extended survey released!** See [Agent Memory Research in 2026: A Data-Driven Survey and Extended Taxonomy](paper/main.pdf) — 19 pages, 220 papers, expanded 6-dimension taxonomy
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


## 📚 Paper list

### Factual Memory

#### Token-level

- [2026/06] Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory. [[paper](https://arxiv.org/abs/2606.10677)]
- [2026/06] RaMem: Contextual Reinstatement for Long-term Agentic Memory. [[paper](https://arxiv.org/abs/2606.22844)] [[code](https://github.com/weiyang930/RaMem-Release.git)]
- [2026/06] MemProbe: Probing Long-Term Agent Memory via Hidden User-State Recovery. [[paper](https://arxiv.org/abs/2606.24595)] [[code](https://github.com/sora1998/MemProbe)]
- [2026/06] Are We Ready For An Agent-Native Memory System?. [[paper](https://arxiv.org/abs/2606.24775)]
- [2026/06] Rosetta Memory: Adaptive Memory for Cross-LLM Agents. [[paper](https://arxiv.org/abs/2606.07711)]
- [2026/04] Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework. [[paper](https://arxiv.org/abs/2604.01707)]
- [2026/04] Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering. [[paper](https://arxiv.org/abs/2604.08224)]
- [2026/04] Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents. [[paper](https://arxiv.org/abs/2604.22085)]
- [2026/03] Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers. [[paper](https://arxiv.org/abs/2603.07670)]
- [2026/01] Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning. [[paper](https://arxiv.org/abs/2601.04726)]
- [2026/01] MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents. [[paper](https://arxiv.org/abs/2601.03236)]
- [2026/01] EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning. [[paper](https://arxiv.org/abs/2601.02163)]
- [2025/12] From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition. [[paper](https://arxiv.org/abs/2512.14244)]
- [2025/12] MemVerse: Multimodal Memory for Lifelong Learning Agents. [[paper](https://arxiv.org/abs/2512.03627)]
- [2025/12] MMAG: Mixed Memory-Augmented Generation for Large Language Models Applications. [[paper](https://arxiv.org/abs/2512.01710)]
- [2025/12] Sophia: A Persistent Agent Framework of Artificial Life. [[paper](https://arxiv.org/abs/2512.18202)]
- [2025/12] WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning. [[paper](https://arxiv.org/abs/2512.02425)]
- [2025/12] Memoria: A Scalable Agentic Memory Framework for Personalized Conversational AI. [[paper](https://arxiv.org/abs/2512.12686)]
- [2025/12] Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects. [[paper](https://arxiv.org/abs/2512.12818)]
- [2025/11] A Simple Yet Strong Baseline for Long-Term Conversational Memory of LLM Agents. [[paper](https://arxiv.org/abs/2511.17208)]
- [2025/11] General Agentic Memory Via Deep Research. [[paper](https://arxiv.org/abs/2511.18423)]
- [2025/11] O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents. [[paper](https://arxiv.org/abs/2511.13593)]
- [2025/11] RCR-Router: Efficient Role-Aware Context Routing for Multi-Agent LLM Systems with Structured Memory. [[paper](https://arxiv.org/abs/2508.04903)]
- [2025/11] Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory and User Profiles. [[paper](https://arxiv.org/abs/2510.07925)]
- [2025/10] Livia: An Emotion-Aware AR Companion Powered by Modular AI Agents and Progressive Memory Compression. [[paper](https://arxiv.org/abs/2509.05298)]
- [2025/10] D-SMART: Enhancing LLM Dialogue Consistency via Dynamic Structured Memory And Reasoning Tree. [[paper](https://arxiv.org/abs/2510.13363)]
- [2025/10] WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research. [[paper](https://arxiv.org/abs/2509.13312)]
- [2025/10] CAM: A Constructivist View of Agentic Memory for LLM-Based Reading Comprehension. [[paper](https://arxiv.org/abs/2510.05520)]
- [2025/10] Pre-Storage Reasoning for Episodic Memory: Shifting Inference Burden to Memory for Personalized Dialogue. [[paper](https://arxiv.org/abs/2509.10852)]
- [2025/10] LightMem: Lightweight and Efficient Memory-Augmented Generation. [[paper](https://arxiv.org/abs/2510.18866)]
- [2025/10] RGMem: Renormalization Group-based Memory Evolution for Language Agent User Profile. [[paper](https://arxiv.org/abs/2510.16392)]
- [2025/09] Mem-α: Learning Memory Construction via Reinforcement Learning. [[paper](https://arxiv.org/abs/2509.25911)]
- [2025/09] SGMem: Sentence Graph Memory for Long-Term Conversational Agents. [[paper](https://arxiv.org/abs/2509.21212)]
- [2025/09] Nemori: Self-Organizing Agent Memory Inspired by Cognitive Science. [[paper](https://arxiv.org/abs/2508.03341)]
- [2025/09] MOOM: Maintenance, Organization and Optimization of Memory in Ultra-Long Role-Playing Dialogues. [[paper](https://arxiv.org/abs/2509.11860)]
- [2025/09] Multiple Memory Systems for Enhancing the Long-term Memory of Agent. [[paper](https://arxiv.org/abs/2508.15294)]
- [2025/09] Semantic Anchoring in Agentic Memory: Leveraging Linguistic Structures for Persistent Conversational Context. [[paper](https://arxiv.org/abs/2508.12630)]
- [2025/09] ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning. [[paper](https://arxiv.org/abs/2508.10419)]
- [2025/08] Building Self-Evolving Agents via Experience-Driven Lifelong Learning: A Framework and Benchmark. [[paper](https://arxiv.org/abs/2508.19005)]
- [2025/08] Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory. [[paper](https://arxiv.org/abs/2508.09736)]
- [2025/08] Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning. [[paper](https://arxiv.org/abs/2508.19828)]
- [2025/08] Intrinsic Memory Agents: Heterogeneous Multi-Agent LLM Systems through Structured Contextual Memory. [[paper](https://arxiv.org/abs/2508.08997)]
- [2025/07] MIRIX: Multi-Agent Memory System for LLM-Based Agents. [[paper](https://arxiv.org/abs/2507.07957)]
- [2025/07] Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents. [[paper](https://arxiv.org/abs/2507.22925)]
- [2025/07] MemoryAgentBench: Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions. [[paper](https://arxiv.org/abs/2507.05257)]
- [2025/06] G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems. [[paper](https://arxiv.org/abs/2506.07398)]
- [2025/06] Embodied Agents Meet Personalization: Exploring Memory Utilization for Personalized Assistance. [[paper](https://arxiv.org/abs/2505.16348)]
- [2025/06] MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents. [[paper](https://arxiv.org/abs/2506.21605)] [[code](https://github.com/import-myself/Membench)]
- [2025/05] MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents. [[paper](https://arxiv.org/abs/2505.20231)]
- [2025/05] Pre-training Limited Memory Language Models with Internal and External Knowledge. [[paper](https://arxiv.org/abs/2505.15962)]
- [2025/05] Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding. [[paper](https://arxiv.org/abs/2501.00358)]
- [2025/04] Mem0: Building production-ready ai agents with scalable long-term memory. [[paper](https://arxiv.org/abs/2504.19413)]
- [2025/03] In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents. [[paper](https://aclanthology.org/2025.acl-long.413/)]
- [2025/02] SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents. [[paper](https://openreview.net/forum?id=xKDZAW0He3)]
- [2025/02] Zep: A Temporal Knowledge Graph Architecture for Agent Memory. [[paper](https://arxiv.org/abs/2501.13956)]
- [2025/02] R³Mem: Bridging Memory Retention and Retrieval via Reversible Compression. [[paper](https://arxiv.org/abs/2502.15957)]
- [2025/02] A-MEM: Agentic Memory for LLM Agents. [[paper](https://arxiv.org/abs/2502.12110)]
- [2025/02] Unveiling Privacy Risks in LLM Agent Memory. [[paper](https://arxiv.org/abs/2502.13172)]
- [2025/02] Mem2Ego: Empowering Vision-Language Models with Global-to-Ego Memory for Long-Horizon Embodied Navigation. [[paper](https://arxiv.org/abs/2502.14254)]
- [2024/12] AI PERSONA: Towards Life-long Personalization of LLMs. [[paper](https://arxiv.org/abs/2412.13103)]
- [2024/11] OASIS: Open Agent Social Interaction Simulations with One Million Agents. [[paper](https://arxiv.org/abs/2411.11581)]
- [2024/10] Video-RAG: Visually-aligned Retrieval-Augmented Long Video Comprehension. [[paper](https://arxiv.org/abs/2411.13093)]
- [2024/10] Memolet: Reifying the Reuse of User-AI Conversational Memories. [[paper](https://doi.org/10.1145/3654777.3676388)]
- [2024/10] From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs. [[paper](https://arxiv.org/abs/2410.14052)]
- [2024/10] Enhancing Long Context Performance in LLMs Through Inner Loop Query Mechanism. [[paper](https://arxiv.org/abs/2410.12859)]
- [2024/10] LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. [[paper](https://arxiv.org/abs/2410.10813)] [[code](https://github.com/xiaowu0162/LongMemEval)]
- [2024/09] Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs. [[paper](https://arxiv.org/abs/2409.19401)]
- [2024/07] Human-inspired Episodic Memory for Infinite Context LLMs. [[paper](https://openreview.net/forum?id=BI2int5SAC)]
- [2024/07] Arigraph: Learning knowledge graph world models with episodic memory for llm agents. [[paper](https://arxiv.org/abs/2407.04363)]
- [2024/07] ChatHaruhi: Reviving Anime Character in Reality via Large Language Model. [[paper](https://arxiv.org/abs/2308.09597)]
- [2024/07] Toward Conversational Agents with Context and Time Sensitive Long-term Memory. [[paper](https://arxiv.org/abs/2406.00057)]
- [2024/06] Enhancing Long-Term Memory using Hierarchical Aggregate Tree for Retrieval Augmented Generation. [[paper](https://arxiv.org/abs/2406.06124)]
- [2024/06] Towards Lifelong Dialogue Agents via Timeline-based Memory Management. [[paper](https://arxiv.org/abs/2406.10996)]
- [2024/05] HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models. [[paper](https://arxiv.org/abs/2405.14831)]
- [2024/05] Memory Sharing for Large Language Model based Agents. [[paper](https://arxiv.org/abs/2404.09982)]
- [2024/05] Knowledge Graph Tuning: Real-time Large Language Model Personalization based on Human Feedback. [[paper](https://arxiv.org/abs/2405.19686)]
- [2024/04] From Local to Global: A Graph RAG Approach to Query-Focused Summarization. [[paper](https://arxiv.org/abs/2404.16130)]
- [2024/03] Memoro: Using Large Language Models to Realize a Concise Interface for Real-Time Memory Augmentation. [[paper](https://doi.org/10.1145/3613904.3642450)]
- [2023/10] RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models. [[paper](https://doi.org/10.18653/v1/2024.findings-acl.878)]
- [2023/10] MemGPT: Towards LLMs as Operating Systems. [[paper](https://arxiv.org/abs/2310.08560)]
- [2023/10] GameGPT: Multi-agent Collaborative Framework for Game Development. [[paper](https://arxiv.org/abs/2310.08067)]
- [2023/10] Lyfe Agents: Generative agents for low-cost real-time social interactions. [[paper](https://arxiv.org/abs/2310.02172)]
- [2023/08] CALYPSO: LLMs as Dungeon Masters' Assistants. [[paper](https://doi.org/10.1609/aiide.v19i1.27534)]
- [2023/08] MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. [[paper](https://arxiv.org/abs/2308.00352)]
- [2023/08] Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations. [[paper](https://doi.org/10.1145/3731446)]
- [2023/08] MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation. [[paper](https://arxiv.org/abs/2308.08239)]
- [2023/08] Recursively summarizing enables long-term dialogue memory in large language models. [[paper](https://arxiv.org/abs/2308.15022)]
- [2023/07] MovieChat: From Dense Token to Sparse Memory for Long Video Understanding. [[paper](https://doi.org/10.1109/CVPR52733.2024.01725)]
- [2023/07] S³: Social-network Simulation System with Large Language Model-Empowered Agents. [[paper](https://arxiv.org/abs/2307.14984)]
- [2023/05] Prompted LLMs as Chatbot Modules for Long Open-domain Conversation. [[paper](https://doi.org/10.18653/v1/2023.findings-acl.277)]
- [2023/05] RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text. [[paper](https://arxiv.org/abs/2305.13304)]
- [2023/05] Memorybank: Enhancing large language models with long-term memory. [[paper](https://arxiv.org/abs/2305.10250)]
- [2023/05] RET-LLM: Towards a general read-write memory for large language models. [[paper](https://arxiv.org/abs/2305.14322)]
- [2023/04] Generative agents: Interactive simulacra of human behavior. [[paper](https://arxiv.org/abs/2304.03442)]
- [2023/04] HuaTuo: Tuning LLaMA Model with Chinese Medical Knowledge. [[paper](https://arxiv.org/abs/2304.06975)]
- [2023/04] SCM: Enhancing Large Language Model with Self-Controlled Memory Framework. [[paper](https://arxiv.org/abs/2304.13343)]

#### Parametric

- [2025/10] MemLoRA: Distilling Expert Adapters for On-Device Memory Systems. [[paper](https://arxiv.org/abs/2512.04763)]
- [2025/10] Pretraining with hierarchical memories: separating long-tail and common knowledge. [[paper](https://arxiv.org/abs/2510.02375)]
- [2025/08] Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models. [[paper](https://arxiv.org/abs/2508.09874)]
- [2025/08] MLP Memory: Language Modeling with Retriever-pretrained External Memory. [[paper](https://arxiv.org/abs/2508.01832)]
- [2024/10] Self-Updatable Large Language Models by Integrating Context into Model Parameters. [[paper](https://openreview.net/forum?id=aCPFCDL9QY)]
- [2024/10] AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models. [[paper](https://arxiv.org/abs/2410.02355)]
- [2024/08] ELDER: Enhancing Lifelong Model Editing with Mixture-of-LoRA. [[paper](https://doi.org/10.1609/aaai.v39i23.34622)]
- [2024/05] WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models. [[paper](https://papers.nips.cc/paper_files/paper/2024/hash/60960ad78868fce5c165295fbd895060-Abstract-Conference.html)]
- [2024/03] Online Adaptation of Language Models with a Memory of Amortized Contexts. [[paper](https://papers.nips.cc/paper_files/paper/2024/hash/eaf956b52bae51fbf387b8be4cc3ce18-Abstract-Conference.html)]
- [2024/01] Neighboring Perturbations of Knowledge Editing on Large Language Models. [[paper](https://openreview.net/forum?id=K9NTPRvVRI)]
- [2023/11] CharacterGLM: Customizing Social Characters with Large Language Models. [[paper](https://doi.org/10.18653/v1/2024.emnlp-industry.107)]
- [2023/10] Character-LLM: A Trainable Agent for Role-Playing. [[paper](https://doi.org/10.18653/v1/2023.emnlp-main.814)]
- [2021/10] Fast Model Editing at Scale. [[paper](https://openreview.net/forum?id=0DcZxeWfOPt)]
- [2021/04] Editing Factual Knowledge in Language Models. [[paper](https://arxiv.org/abs/2104.08164)]
- [2020/02] K-Adapter: Infusing Knowledge into Pre-Trained Models with Adapters. [[paper](https://doi.org/10.18653/v1/2021.findings-acl.121)]
- [2013/02] ELLA: An Efficient Lifelong Learning Algorithm. [[paper](https://proceedings.mlr.press/v28/ruvolo13.html)]

#### Latent

- [2026/06] MRAgent: Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents. [[paper](https://arxiv.org/abs/2606.06036)] [[code](https://github.com/Ji-shuo/MRAgent)]
- [2026/06] EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory. [[paper](https://arxiv.org/abs/2606.21649)]
- [2026/05] ElasticMem: Latent Memory as a Learnable Resource for LLM Agents. [[paper](https://arxiv.org/abs/2605.30690)]
- [2025/09] Similarity-Distance-Magnitude Activations. [[paper](https://arxiv.org/abs/2509.12760)]
- [2025/08] Towards General Continuous Memory for Vision-Language Models. [[paper](https://arxiv.org/abs/2505.17670)]
- [2025/03] M+: Extending MemoryLLM with Scalable Long-Term Memory. [[paper](https://arxiv.org/abs/2502.00592)]
- [2025/02] R3Mem: Bridging Memory Retention and Retrieval via Reversible Compression. [[paper](https://arxiv.org/abs/2502.15957)]
- [2024/07] Memory³: Language Modeling with Explicit Memory. [[paper](https://arxiv.org/abs/2407.01178)]
- [2024/03] Efficient Episodic Memory Utilization of Cooperative Multi-Agent Reinforcement Learning. [[paper](https://openreview.net/forum?id=LjivA1SLZ6)]
- [2023/10] Memoria: Resolving Fateful Forgetting Problem through Human-Inspired Memory Architecture. [[paper](https://arxiv.org/abs/2310.03052)]
- [2021/12] Detecting Local Insights from Global Labels: Supervised & Zero-Shot Sequence Labeling via a Convolutional Decomposition. [[paper](https://doi.org/10.1162/coli_a_00416)]

### Experiential Memory

#### Token-level

- [2026/06] AdMem: Advanced Memory for Task-solving Agents. [[paper](https://arxiv.org/abs/2606.06787)]
- [2026/05] From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms. [[paper](https://arxiv.org/abs/2605.06716)]
- [2026/05] LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues. [[paper](https://arxiv.org/abs/2605.12493)]
- [2026/04] GAM: Hierarchical Graph-based Agentic Memory for LLM Agents. [[paper](https://arxiv.org/abs/2604.12285)]
- [2026/02] ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents. [[paper](https://arxiv.org/abs/2602.01869)]
- [2026/02] UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory. [[paper](https://arxiv.org/abs/2602.10652)]
- [2026/01] MCMA: Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory. [[paper](https://arxiv.org/abs/2601.07470)]
- [2026/01] MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory. [[paper](https://arxiv.org/abs/2601.03192)]
- [2026/01] FadeMem: Biologically-Inspired Forgetting for Efficient Agent Memory. [[paper](https://arxiv.org/abs/2601.18642)]
- [2025/12] MemEvolve: Meta-Evolution of Agent Memory Systems. [[paper](https://arxiv.org/abs/2512.18746)]
- [2025/12] Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution. [[paper](https://arxiv.org/abs/2512.10696)]
- [2025/12] Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects. [[paper](https://arxiv.org/abs/2512.12818)]
- [2025/11] Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models. [[paper](https://arxiv.org/abs/2510.04618)]
- [2025/11] FLEX: Continuous Agent Evolution via Forward Learning from Experience. [[paper](https://arxiv.org/abs/2511.06449)]
- [2025/11] Scaling Agent Learning via Experience Synthesis. [[paper](https://arxiv.org/abs/2511.03773)]
- [2025/11] UFO2: The Desktop AgentOS. [[paper](https://arxiv.org/abs/2504.14603)]
- [2025/10] PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agents. [[paper](https://arxiv.org/abs/2509.17459)]
- [2025/10] Training-Free Group Relative Policy Optimization. [[paper](https://arxiv.org/abs/2510.08191)]
- [2025/10] ToolMem: Enhancing Multimodal Agents with Learnable Tool Capability Memory. [[paper](https://arxiv.org/abs/2510.06664)]
- [2025/10] H²R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents. [[paper](https://arxiv.org/abs/2509.12810)]
- [2025/10] BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions. [[paper](https://arxiv.org/abs/2510.10666)]
- [2025/10] LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation. [[paper](https://arxiv.org/abs/2510.04851)]
- [2025/10] Alita-G: Self-Evolving Generative Agent for Agent Generation. [[paper](https://arxiv.org/abs/2510.23601)]
- [2025/09] ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory. [[paper](https://arxiv.org/abs/2509.25140)]
- [2025/09] Memento: Fine-tuning LLM Agents without Fine-tuning LLMs. [[paper](https://arxiv.org/abs/2508.16153)]
- [2025/08] Memp: Exploring Agent Procedural Memory. [[paper](https://arxiv.org/abs/2508.06433)]
- [2025/08] SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience. [[paper](https://arxiv.org/abs/2508.04700)]
- [2025/07] Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving. [[paper](https://arxiv.org/abs/2507.06229)]
- [2025/07] MemTool: Optimizing short-term memory management for dynamic tool calling in llm agent multi-turn conversations. [[paper](https://arxiv.org/abs/2507.21428)]
- [2025/05] Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents. [[paper](https://arxiv.org/abs/2505.22954)]
- [2025/05] Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution. [[paper](https://arxiv.org/abs/2505.20286)]
- [2025/05] SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills. [[paper](https://arxiv.org/abs/2504.07079)]
- [2025/05] LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark. [[paper](https://arxiv.org/abs/2504.13805)]
- [2025/05] Retrieval Models Aren't Tool-Savvy: Benchmarking Tool Retrieval for Large Language Models. [[paper](https://arxiv.org/abs/2503.01763)]
- [2025/04] Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory. [[paper](https://arxiv.org/abs/2504.07952)]
- [2025/04] Inducing Programmatic Skills for Agentic Tasks. [[paper](https://arxiv.org/abs/2504.06821)]
- [2025/03] COLA: A Scalable Multi-Agent Framework For Windows UI Task Automation. [[paper](https://arxiv.org/abs/2503.09263)]
- [2025/03] Memory-augmented Query Reconstruction for LLM-based Knowledge Graph Reasoning. [[paper](https://arxiv.org/abs/2503.05193)]
- [2025/02] From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions. [[paper](https://arxiv.org/abs/2410.08197)]
- [2025/02] From RAG to Memory: Non-Parametric Continual Learning for Large Language Models. [[paper](https://arxiv.org/abs/2502.14802)]
- [2024/12] Planning from Imagination: Episodic Simulation and Episodic Memory for Vision-and-Language Navigation. [[paper](https://arxiv.org/abs/2412.01857)]
- [2024/10] RepairAgent: An Autonomous, LLM-Based Agent for Program Repair. [[paper](https://arxiv.org/abs/2403.17134)]
- [2024/09] SAGE: Self-evolving Agents with Reflective and Memory-augmented Abilities. [[paper](https://doi.org/10.1016/j.neucom.2025.130470)]
- [2024/07] Agent Workflow Memory. [[paper](https://openreview.net/forum?id=NTAhi2JEEE)]
- [2024/07] Fincon: A synthesized llm multi-agent system with conceptual verbal reinforcement for enhanced financial decision making. [[paper](https://arxiv.org/abs/2407.06567)]
- [2024/06] Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models. [[paper](https://papers.nips.cc/paper_files/paper/2024/hash/cde328b7bf6358f5ebb91fe9c539745e-Abstract-Conference.html)]
- [2024/05] COLT: Towards Completeness-Oriented Tool Retrieval for Large Language Models. [[paper](https://arxiv.org/abs/2405.16089)]
- [2023/11] JARVIS-1: Open-World Multi-Task Agents With Memory-Augmented Multimodal Language Models. [[paper](https://doi.org/10.1109/TPAMI.2024.3511593)]
- [2023/08] RecMind: Large Language Model Powered Agent For Recommendation. [[paper](https://doi.org/10.18653/v1/2024.findings-naacl.271)]
- [2023/08] ExpeL: LLM Agents Are Experiential Learners. [[paper](https://doi.org/10.1609/aaai.v38i17.29936)]
- [2023/07] ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. [[paper](https://arxiv.org/abs/2307.16789)]
- [2023/05] CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models. [[paper](https://doi.org/10.18653/v1/2023.findings-emnlp.462)]
- [2023/03] Reflexion: Language agents with verbal reinforcement learning. [[paper](https://arxiv.org/abs/2303.11366)]
- [2023/02] Toolformer: Language models can teach themselves to use tools. [[paper](https://arxiv.org/abs/2302.04761)]

#### Parametric

- [2025/11] AgentEvolver: Towards Efficient Self-Evolving Agent System. [[paper](https://arxiv.org/abs/2511.10395)]
- [2025/10] Agent Learning via Early Experience. [[paper](https://arxiv.org/abs/2510.08558)]
- [2025/10] Scaling Agents via Continual Pre-training. [[paper](https://arxiv.org/abs/2509.13310)]
- [2024/10] ToolGen: Unified Tool Retrieval and Calling via Generation. [[paper](https://arxiv.org/abs/2410.03439)]
- [2023/08] Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization. [[paper](https://arxiv.org/abs/2308.02151)]
- [2023/06] A Machine with Short-Term, Episodic, and Semantic Memory Systems. [[paper](https://doi.org/10.1609/aaai.v37i1.25075)]

#### Latent

- [2026/03] All-Mem: Agentic Lifelong Memory via Dynamic Topology Evolution. [[paper](https://arxiv.org/abs/2603.19595)] [[code](https://github.com/LvCan926/All-Mem)]
- [2026/01] TeleMem: Building Long-Term and Multimodal Memory for Agentic AI. [[paper](https://arxiv.org/abs/2601.06037)]
- [2025/11] Auto-scaling Continuous Memory for GUI Agent. [[paper](https://arxiv.org/abs/2510.09038)]

### Working Memory

#### Token-level

- [2026/07] SelfMem: Self-Optimizing Memory for AI Agents. [[paper](https://arxiv.org/abs/2607.03726)]
- [2026/07] Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents. [[paper](https://arxiv.org/abs/2607.08716)]
- [2026/06] MemRefine: LLM-Guided Compression for Long-Term Agent Memory. [[paper](https://arxiv.org/abs/2606.13177)]
- [2026/06] Joint Agent Memory and Exploration Learning via Novelty Signals. [[paper](https://arxiv.org/abs/2606.01528)]
- [2026/03] CraniMem: Cranial Inspired Gated and Bounded Memory for Agentic Systems. [[paper](https://arxiv.org/abs/2603.15642)] [[code](https://github.com/PearlMody05/Cranimem)]
- [2026/02] FluxMem: Choosing How to Remember: Adaptive Memory Structures for LLM Agents. [[paper](https://arxiv.org/abs/2602.14038)]
- [2026/02] BudgetMem: Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory. [[paper](https://arxiv.org/abs/2602.06025)] [[code](https://github.com/ViktorAxelsen/BudgetMem)]
- [2026/02] EMPO2: Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization. [[paper](https://arxiv.org/abs/2602.23008)]
- [2026/01] MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory. [[paper](https://arxiv.org/abs/2601.03192)]
- [2026/01] MemoBrain: Executive Memory as an Agentic Brain for Reasoning. [[paper](https://arxiv.org/abs/2601.08079)]
- [2026/01] Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents. [[paper](https://arxiv.org/abs/2601.01885)]
- [2025/11] Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks. [[paper](https://arxiv.org/abs/2510.12635)]
- [2025/11] IterResearch: Rethinking Long-Horizon Agents via Markovian State Reconstruction. [[paper](https://arxiv.org/abs/2511.07327)]
- [2025/11] MemSearcher: Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning. [[paper](https://arxiv.org/abs/2511.02805)]
- [2025/10] AgentFold: Long-Horizon Web Agents with Proactive Context Management. [[paper](https://arxiv.org/abs/2510.24699)]
- [2025/10] PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning. [[paper](https://arxiv.org/abs/2509.22315)]
- [2025/10] Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval. [[paper](https://arxiv.org/abs/2506.03141)]
- [2025/10] DeepAgent: A General Reasoning Agent with Scalable Toolsets. [[paper](https://arxiv.org/abs/2510.21618)]
- [2025/10] ACON: Optimizing Context Compression for Long-Horizon LLM Agents. [[paper](https://arxiv.org/abs/2510.00615)]
- [2025/09] ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization. [[paper](https://arxiv.org/abs/2509.13313)]
- [2025/08] Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management. [[paper](https://arxiv.org/abs/2508.04664)]
- [2025/07] MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent. [[paper](https://arxiv.org/abs/2507.02259)]
- [2024/10] Agent S: An Open Agentic Framework That Uses Computers Like a Human. [[paper](https://arxiv.org/abs/2410.08164)]

#### Parametric

- [2026/02] Learning to Remember: End-to-End Training of Memory Agents for Long-Context Reasoning. [[paper](https://arxiv.org/abs/2602.18493)]
- [2024/05] Various Lengths, Constant Speed: Efficient Language Modeling with Lightning Attention. [[paper](https://openreview.net/forum?id=5wm6TiUP4X)]
- [2024/01] Efficient Streaming Language Models with Attention Sinks. [[paper](https://openreview.net/forum?id=NG7sS51zVF)]

#### Latent

- [2026/06] Engram: A Bi-Temporal Memory Engine for LLM Agents. [[paper](https://arxiv.org/abs/2606.09900)]
- [2026/05] Human-Inspired Memory Architecture for LLM Agents. [[paper](https://arxiv.org/abs/2605.08538)]
- [2026/04] SCM: Sleep-Consolidated Memory with Algorithmic Forgetting for Large Language Models. [[paper](https://arxiv.org/abs/2604.20943)]
- [2026/03] Neural Paging: Learning Context Management Policies for Turing-Complete Agents. [[paper](https://arxiv.org/abs/2603.02228)]
- [2026/01] Continuum Memory Architectures for Long-Horizon LLM Agents. [[paper](https://arxiv.org/abs/2601.09913)]
- [2025/11] VisMem: Latent Vision Memory Unlocks Potential of Vision-Language Models. [[paper](https://arxiv.org/abs/2511.11007)]
- [2025/09] MemGen: Weaving Generative Latent Memory for Self-Evolving Agents. [[paper](https://arxiv.org/abs/2509.24704)]
- [2025/09] Conflict-Aware Soft Prompting for Retrieval-Augmented Generation. [[paper](https://arxiv.org/abs/2508.15253)]
- [2025/09] MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation. [[paper](https://arxiv.org/abs/2508.19236)]
- [2025/06] MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents. [[paper](https://arxiv.org/abs/2506.15841)]
- [2025/05] RazorAttention: Efficient KV Cache Compression Through Retrieval Heads. [[paper](https://openreview.net/forum?id=tkiZQlL04w)]
- [2025/04] MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation. [[paper](https://doi.org/10.1145/3696410.3714805)]
- [2025/04] SnapKV: LLM Knows What You are Looking for Before Generation. [[paper](https://papers.nips.cc/paper_files/paper/2024/hash/28ab418242603e0f7323e54185d19bde-Abstract-Conference.html)]
- [2025/03] LM2: Large Memory Models. [[paper](https://arxiv.org/abs/2502.06049)]
- [2025/02] SoftCoT: Soft Chain-of-Thought for Efficient Reasoning with LLMs. [[paper](https://aclanthology.org/2025.acl-long.1137/)]
- [2025/02] Time-VLM: Exploring Multimodal Vision-Language Models for Augmented Time Series Forecasting. [[paper](https://arxiv.org/abs/2502.04395)]
- [2025/02] Titans: Learning to Memorize at Test Time. [[paper](https://arxiv.org/abs/2501.00663)]
- [2024/08] Augmenting Language Models with Long-Term Memory. [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/ebd82705f44793b6f9ade5a669d0f0bf-Abstract-Conference.html)]
- [2024/06] Taking a Deep Breath: Enhancing Language Modeling of Large Language Models with Sentinel Tokens. [[paper](https://doi.org/10.18653/v1/2024.findings-emnlp.233)]
- [2024/04] Adapting Language Models to Compress Contexts. [[paper](https://doi.org/10.18653/v1/2023.emnlp-main.232)]
- [2024/03] Learning to Compress Prompts with Gist Tokens. [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/3d77c6dcc7f143aa2154e7f4d5e22d68-Abstract-Conference.html)]
- [2024/03] Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time. [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/a452a7c6c463e4ae8fbdc614c6e983e6-Abstract-Conference.html)]
- [2024/03] Focused Transformer: Contrastive Training for Context Scaling. [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/8511d06d5590f4bda24d42087802cc81-Abstract-Conference.html)]
- [2023/07] In-Context Autoencoder for Context Compression in a Large Language Model. [[paper](https://arxiv.org/abs/2307.06945)]
- [2023/06] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models. [[paper](https://papers.nips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html)]
- [2022/08] Memorizing Transformers. [[paper](https://openreview.net/forum?id=TrjbxzRcnf-)]
- [2022/07] XMem: Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model. [[paper](https://arxiv.org/abs/2207.07115)]

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

