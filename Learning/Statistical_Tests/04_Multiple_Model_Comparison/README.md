# 04_Multiple_Model_Comparison - Friedman Test

## Overview
This notebook demonstrates the Friedman test for comparing multiple models across multiple datasets or prompts.

## Purpose
The Friedman test is a non-parametric statistical test used to detect differences between multiple models when tested on the same datasets. It's the alternative to repeated measures ANOVA for non-normal data.

## Key Concepts
- **Non-parametric**: Does not assume normal distribution
- **Multiple comparisons**: Tests 3+ models simultaneously
- **Blocked design**: Each prompt/dataset is a "block"
- **Rank-based**: Ranks models within each block

## Expected Workflow
1. Load benchmark results from `01_Fundamentals/benchmark_results.csv`
2. Organize data by model and prompt (blocks)
3. Rank models within each prompt
4. Apply Friedman test
5. If significant, perform post-hoc tests (e.g., Nemenyi)
6. Visualize results with critical difference diagrams

## Requirements
```bash
pip install numpy pandas scipy matplotlib seaborn
```

## Notes
- Use when comparing 3+ models on same datasets
- Controls for family-wise error rate
- Post-hoc tests needed to identify which models differ
- More conservative than ANOVA but robust to violations
