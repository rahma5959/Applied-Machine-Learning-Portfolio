# Statistical Tests for AI Model Evaluation

## Overview
This directory contains a structured learning path for applying statistical tests to evaluate and compare AI models, with a focus on small language models (SLMs).

## Learning Path

### 01_Fundamentals - Local Models Metrics
**Goal**: Establish baseline performance metrics for small language models

**Content**:
- Evaluation of TinyLlama, Qwen2.5, and SmolLM2 on ML/AI prompts
- Metrics collected: latency, response length, and generated responses
- Output: `benchmark_results.csv` for subsequent analysis

**Prerequisites**: 
- Python 3.9+
- PyTorch, Transformers, Pandas

**Duration**: Month 1

---

### 02_Confidence_Intervals - Bootstrap Confidence Interval
**Goal**: Learn to quantify uncertainty in performance metrics

**Content**:
- Bootstrap resampling techniques
- Computing confidence intervals for model metrics
- Non-parametric uncertainty estimation

**Prerequisites**: 
- Completion of 01_Fundamentals
- NumPy, Pandas, Matplotlib, Seaborn

**Duration**: Month 2

---

### 03_Significance_Tests - Wilcoxon Test
**Goal**: Compare two models statistically

**Content**:
- Wilcoxon signed-rank test for paired samples
- Non-parametric alternative to paired t-test
- Interpreting p-values and effect sizes

**Prerequisites**: 
- Completion of 02_Confidence_Intervals
- SciPy

**Duration**: Month 3

---

### 04_Multiple_Model_Comparison - Friedman Test
**Goal**: Compare multiple models simultaneously

**Content**:
- Friedman test for 3+ models on same datasets
- Post-hoc tests (Nemenyi)
- Critical difference diagrams

**Prerequisites**: 
- Completion of 03_Significance_Tests
- SciPy, Matplotlib, Seaborn

**Duration**: Later (advanced)

---

## Prerequisites

### System Requirements
- Python 3.9 or higher
- Jupyter Notebook or JupyterLab
- ~10GB disk space for model downloads

### Python Packages
```bash
pip install torch transformers pandas numpy scipy matplotlib seaborn
```

### Hardware
- GPU recommended for model inference (optional but faster)
- Minimum 8GB RAM
- Internet connection for downloading models from HuggingFace

## Workflow

1. **Start with 01_Fundamentals**: Run the evaluation notebook to generate benchmark results
2. **Progress sequentially**: Each module builds on the previous one's output
3. **Use real data**: All statistical tests use the benchmark results from module 01
4. **Document findings**: Update README files with your observations

## Notes

- All notebooks are designed to be run sequentially
- The `benchmark_results.csv` from 01_Fundamentals is used by all subsequent modules
- Focus on understanding the statistical concepts rather than just running code
- Modify prompts and models as needed for your specific use case

## Resources

- [Bootstrap Methods](https://en.wikipedia.org/wiki/Bootstrapping_(statistics))
- [Wilcoxon Signed-Rank Test](https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test)
- [Friedman Test](https://en.wikipedia.org/wiki/Friedman_test)
- [Statistical Significance in ML](https://arxiv.org/abs/1811.12808)
