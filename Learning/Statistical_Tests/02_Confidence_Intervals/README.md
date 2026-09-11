# 02_Confidence_Intervals - Bootstrap Confidence Interval

## Overview
This notebook demonstrates how to compute confidence intervals using bootstrap resampling for model performance metrics.

## Purpose
Bootstrap confidence intervals provide a non-parametric way to estimate the uncertainty around performance metrics when the underlying distribution is unknown or non-normal.

## Key Concepts
- **Bootstrap Resampling**: Sampling with replacement from the original dataset
- **Confidence Interval**: Range of values that likely contains the true population parameter
- **Non-parametric**: Does not assume a specific distribution (e.g., normal)

## Expected Workflow
1. Load benchmark results from `01_Fundamentals/benchmark_results.csv`
2. Define a metric of interest (e.g., latency, response_length)
3. Implement bootstrap resampling function
4. Compute confidence intervals (e.g., 95% CI)
5. Visualize results

## Requirements
```bash
pip install numpy pandas matplotlib seaborn
```

## Notes
- Bootstrap is computationally intensive but robust
- Recommended number of bootstrap samples: 1000-10000
- Use this method when sample size is small or distribution is unknown
