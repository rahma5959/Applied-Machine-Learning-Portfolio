# 03_Significance_Tests - Wilcoxon Test

## Overview
This notebook demonstrates the Wilcoxon signed-rank test for comparing the performance of two models on related samples.

## Purpose
The Wilcoxon test is a non-parametric statistical test used to compare two related samples. It's the alternative to the paired t-test when the data does not follow a normal distribution.

## Key Concepts
- **Non-parametric**: Does not assume normal distribution
- **Paired samples**: Measurements from the same subjects or related groups
- **Rank-based**: Uses ranks rather than raw values
- **Robust**: Less sensitive to outliers than t-test

## Expected Workflow
1. Load benchmark results from `01_Fundamentals/benchmark_results.csv`
2. Select two models to compare
3. Extract paired measurements (e.g., latency for same prompts)
4. Check if differences are normally distributed
5. Apply Wilcoxon signed-rank test
6. Interpret p-value and effect size

## Requirements
```bash
pip install numpy pandas scipy
```

## Notes
- Use when sample size is small (<30) or distribution is non-normal
- More robust than t-test but less powerful when assumptions are met
- Tests if median difference is zero
