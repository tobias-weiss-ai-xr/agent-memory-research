<h1 align="center">
  <strong>Agent Memory Research</strong>
</h1>
<h3 align="center">A data-driven, auto-validated reading list for Agent Memory research</h3>

### 🔗 Links

- **GitHub**: https://github.com/tobias-weiss-ai-xr/agent-memory-research
- **License**: https://github.com/tobias-weiss-ai-xr/agent-memory-research/blob/main/LICENSE
- **CI**: https://github.com/tobias-weiss-ai-xr/agent-memory-research/actions/workflows/validate.yml
- **Survey Paper (Original)**: https://arxiv.org/abs/2512.13564
- **HF Dataset**: https://huggingface.co/papers/2512.13564
- **Agent Learning**: https://github.com/tobias-weiss-ai-xr/agent-learning-research
- **Agent Skill**: https://github.com/tobias-weiss-ai-xr/agent-skill-research
- **Agentic VR**: https://github.com/tobias-weiss-ai-xr/agentic-vr-research


> 💾 **Agent memory research corpus:** curated papers for the survey
> "Memory in the Age of AI Agents" (arXiv:2512.13564). Part of the family of
> consistent `*-research` corpora.

<p align="center">
  <img src="https://raw.githubusercontent.com/tobias-weiss-ai-xr/agent-memory-research/main/assets/visualizations/category_distribution.png" alt="Teaser" width="600" />
</p>

---

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


## 📊 Corpus Statistics

**3,576 papers** across **3 categories**.  
Sources: **arXiv** 2,883 (80%) · **DOI** 530 (14%) · **Other** 163 (4%).  
Full paper list: [GitHub Pages site](https://tobias-weiss-ai-xr.github.io/agent-memory-research).

### Top categories

| Category | Papers | Recent | |
|----------|--------|--------|-|
| factual | **1,771** | 0 | ████████████ |
| experiential | **903** | 0 | ██████░░░░░░ |
| working | **902** | 0 | ██████░░░░░░ |


### By year

| Year | Papers | |
|------|--------|-|
| 2024 | 393 | ██░░░░░░░░░░ |
| 2025 | 966 | ██████░░░░░░ |
| 2026 | 1,769 | ████████████ |


### Momentum (hottest categories)

| Category | Total | Rate | Recent | Score |
|----------|-------|------|--------|-------|
| Experiential | 903 | 50.7/mo | 67% | 338 |
| Factual | 1,771 | 99.3/mo | 67% | 307 |
| Working | 902 | 38.3/mo | 51% | 217 |


### Trending keywords

| Keyword | Papers | Burst |
|---------|--------|-------|
| agentic | 613 | 1.41 |
| opponent | 8 | 1.38 |
| policy | 299 | 1.28 |
| uncertainty | 58 | 1.28 |
| benchmark | 1,119 | 1.26 |
| skill | 202 | 1.24 |
| transfer | 173 | 1.24 |
| hierarchical | 271 | 1.23 |


### Top venues

| Venue | Papers |
|-------|--------|
| arXiv (Cornell University) | 46 |
| CoRR | 31 |
| Zenodo (CERN European Organization for Nuclear Research) | 22 |
| MED | 10 |
| Neural Networks | 9 |
| ACL 2026 | 8 |
| Journal of Memory and Language | 8 |
| Open MIND | 8 |


### Research gaps (thinnest cells)

| Cell | Papers |
|------|--------|
| `working/mechanism` | 9 |
| `experiential/application` | 10 |
| `experiential/theory` | 10 |
| `experiential/mechanism` | 15 |
| `factual/development` | 18 |



*Generated 2026-08 by `scripts/standard_stats.py`.*


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

## 🔗 Related Projects

| Project | Description |
|---------|-------------|
| [Agent Memory Bench](https://github.com/tobias-weiss-ai-xr/agent-memory-bench) | Benchmark for agent memory systems |
| [Agentic VR Research](https://github.com/tobias-weiss-ai-xr/agentic-vr-research) | Survey of agentic VR systems |
| [Agent Skill Research](https://github.com/tobias-weiss-ai-xr/agent-skill-research) | Survey of skill acquisition in AI agents |
| [Agent Skill Bench](https://github.com/tobias-weiss-ai-xr/agent-skill-bench) | Benchmark for agent skill systems |
| [Agent Learning Research](https://github.com/tobias-weiss-ai-xr/agent-learning-research) | Survey of learning in AI agents |
| [Learning Research](https://github.com/tobias-weiss-ai-xr/learning-research) | Interdisciplinary survey of learning across all disciplines |
## 📊 Corpus Statistics

**3,576 papers** across **4 categories**.  
Sources: **arXiv** 2,883 (80%) · **DOI** 530 (14%) · **Other** 163 (4%).  
Full paper list: [GitHub Pages site](https://tobias-weiss-ai-xr.github.io/agent-memory-research).

### Top categories

| Category | Papers | Recent | |
|----------|--------|--------|-|
| factual | **1,759** | 0 | ████████████ |
| working | **902** | 0 | ██████░░░░░░ |
| experiential | **901** | 0 | ██████░░░░░░ |
|  | **14** | 0 | ░░░░░░░░░░░░ |


### By year

| Year | Papers | |
|------|--------|-|
| 2025 | 966 | ██████░░░░░░ |
| 2026 | 1,768 | ████████████ |
| 2027 | 1 | ░░░░░░░░░░░░ |


### Momentum (hottest categories)

| Category | Total | Rate | Recent | Score |
|----------|-------|------|--------|-------|
|  | 14 | 1.1/mo | 93% | 1293 |
| Experiential | 901 | 50.5/mo | 67% | 337 |
| Factual | 1,759 | 98.4/mo | 67% | 304 |
| Working | 902 | 38.3/mo | 51% | 217 |


### Trending keywords

| Keyword | Papers | Burst |
|---------|--------|-------|
| agentic | 613 | 1.41 |
| opponent | 8 | 1.38 |
| policy | 299 | 1.28 |
| uncertainty | 58 | 1.28 |
| benchmark | 1,119 | 1.26 |
| skill | 202 | 1.24 |
| transfer | 173 | 1.24 |
| hierarchical | 271 | 1.23 |


### Top venues

| Venue | Papers |
|-------|--------|
| arXiv (Cornell University) | 46 |
| CoRR | 31 |
| Zenodo (CERN European Organization for Nuclear Research) | 22 |
| MED | 10 |
| Neural Networks | 9 |
| ACL 2026 | 8 |
| Journal of Memory and Language | 8 |
| Open MIND | 8 |


### Research gaps (thinnest cells)

| Cell | Papers |
|------|--------|
| `working/mechanism` | 9 |
| `experiential/application` | 10 |
| `experiential/theory` | 10 |
| `/` | 14 |
| `experiential/mechanism` | 15 |



*Generated 2027-01 by `scripts/standard_stats.py`.*


## ⭐️ Star History

[**Star History Chart**](https://www.star-history.com/#Shichun-Liu/Agent-Memory-Paper-List&type=date&legend=top-left)

