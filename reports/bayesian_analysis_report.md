# Bayesian Analysis of Agent Memory Paper Corpus

## Executive Summary

This report presents a comprehensive Bayesian analysis of the agent memory research corpus (952 papers as of July 2026). The analysis reveals explosive growth in the field, with significant heterogeneity across research categories and clear identification of underexplored research areas.

---

## 1. Overall Growth Dynamics

### Key Findings

- **Total papers**: 952 (2011-2026)
- **Recent period (2023-2026)**: 939 papers (98.6% of corpus)
- **Growth rate (2023-2026)**: **138.7% per year** [95% CI: 76.1%, 204.9%]
- **Model fit**: R² = 0.986 (exponential growth model)

### Interpretation

The field is experiencing **explosive exponential growth**, doubling approximately every 6-8 months. The wide credible interval reflects the uncertainty in extrapolating from only 4 years of recent data, but even the lower bound (76%/year) indicates rapid expansion.

---

## 2. Category-Wise Analysis

### Distribution

| Category | Papers | Proportion | 95% CI | Growth Rate |
|----------|--------|------------|--------|-------------|
| Factual | 490 | 51.4% | [48.3%, 54.6%] | 129%/yr |
| Working | 273 | 28.7% | [25.9%, 31.6%] | 184%/yr |
| Experiential | 176 | 18.5% | [16.2%, 21.1%] | 111%/yr |

### Key Insights

1. **Factual memory dominates** (51% of papers), reflecting the field's roots in retrieval-augmented generation (RAG)
2. **Working memory is growing fastest** (184%/year), driven by context management and efficiency concerns
3. **Experiential memory is underrepresented** (18.5%) despite being critical for long-horizon autonomy

### Statistical Significance

All categories show significant growth (p < 0.01), but working memory shows the highest R² (0.996), indicating the most consistent exponential trajectory.

---

## 3. Subcategory Analysis (27 Cells)

### Top 5 Cells

| Cell | Papers | Proportion | 95% CI |
|------|--------|------------|--------|
| factual/token-level | 452 | 47.5% | [44.3%, 50.7%] |
| working/token-level | 220 | 23.1% | [20.5%, 25.9%] |
| experiential/token-level | 153 | 16.1% | [13.9%, 18.5%] |
| working/latent | 53 | 5.6% | [4.3%, 7.2%] |
| factual/latent | 28 | 2.9% | [2.0%, 4.2%] |

### Sparse Cells (< 20 papers)

| Cell | Papers | Proportion | 95% CI | Research Gap |
|------|--------|------------|--------|--------------|
| working/parametric | 3 | 0.3% | [0.1%, 0.9%] | **Critical gap** |
| experiential/parametric | 10 | 1.1% | [0.6%, 1.9%] | **Major gap** |
| experiential/latent | 13 | 1.4% | [0.8%, 2.3%] | **Major gap** |

### Interpretation

The **token-level paradigm dominates** (86.7% of papers), while **parametric approaches are severely underexplored** (only 33 papers, 3.5%). This suggests a significant research opportunity in parametric memory mechanisms, particularly for working and experiential memory.

---

## 4. Change Point Analysis

### Finding

The Bayesian change point detection identifies **2025** as the most likely acceleration point:

- **Before 2025**: ~17 papers/year
- **After 2025**: ~407 papers/year
- **Acceleration factor**: ~24x

### Interpretation

The field experienced a **phase transition in 2025**, likely driven by:
1. Widespread adoption of LLMs in autonomous agents
2. Recognition of memory as a first-class primitive
3. Emergence of standardized benchmarks

---

## 5. Predictive Analysis

### Projected Corpus Size

Using posterior predictive distributions:

| Year | Median Prediction | 95% CI |
|------|-------------------|--------|
| 2027 | 1,300 | [800, 2,200] |
| 2028 | 3,100 | [1,500, 6,000] |
| 2029 | 7,500 | [2,800, 18,000] |
| 2030 | 18,000 | [5,000, 50,000] |

**Note**: Wide credible intervals reflect uncertainty in extrapolating exponential growth. The median suggests the corpus could reach **18,000 papers by 2030** if current trends continue.

---

## 6. Research Implications

### Priority Areas

1. **Parametric memory mechanisms** (especially working/parametric: only 3 papers)
2. **Experiential latent representations** (13 papers)
3. **Cross-category integration** (most papers focus on single cells)

### Methodological Recommendations

1. **Adopt Bayesian methods** for uncertainty quantification in memory system evaluation
2. **Report credible intervals** alongside point estimates
3. **Pre-register studies** to reduce publication bias in sparse cells

### Community Actions

1. **Develop benchmarks** for underexplored cells (working/parametric, experiential/latent)
2. **Encourage replication studies** to validate findings in sparse areas
3. **Create shared datasets** to accelerate progress in parametric approaches

---

## 7. Limitations

1. **Short time series**: Only 4 years of recent data limits precision of growth estimates
2. **Selection bias**: arXiv-centric corpus may miss conference-only publications
3. **Classification uncertainty**: Some papers may be misclassified in the taxonomy
4. **Extrapolation risk**: Exponential growth may not continue indefinitely

---

## 8. Data & Code

- **Raw data**: `papers.yaml` (952 entries)
- **Analysis code**: `scripts/bayesian_analysis_robust.py`
- **Results**: `docs/bayesian_analysis_results.json`
- **Dependencies**: Python 3.10+, scipy, numpy, PyYAML

---

## 9. Citation

```bibtex
@misc{weiss2026agentmemorybayesian,
  author = {Weiß, Tobias},
  title = {Bayesian Analysis of Agent Memory Paper Corpus},
  year = {2026},
  howpublished = {\url{https://github.com/tobias-weiss-ai-xr/agent-memory-research}},
  note = {v1.1.0}
}
```

---

*Analysis performed: July 2026*
*Corpus version: 952 papers*
*Methodology: Bootstrap-based Bayesian inference with Metropolis-Hastings sampling*
