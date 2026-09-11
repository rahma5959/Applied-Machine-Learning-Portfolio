# 01_Fundamentals - Local Models Metrics

## Overview
This notebook evaluates and compares the performance of small language models (SLMs) on various prompts, measuring latency and response characteristics.

## Models Tested
- **TinyLlama**: TinyLlama/TinyLlama-1.1B-Chat-v1.0
- **Qwen2.5**: Qwen/Qwen2.5-1.5B-Instruct
- **SmolLM2**: HuggingFaceTB/SmolLM2-1.7B-Instruct

## Prompts Used
1. Explain overfitting in machine learning.
2. What is the difference between precision and recall?
3. Summarize the role of transformers in NLP.
4. Why is statistical significance important in AI research?
5. Explain the concept of uncertainty estimation.

## Metrics Collected
- **Latency**: Time taken to generate response (seconds)
- **Response Length**: Number of characters in generated response
- **Response**: Full generated text

## Output
Results are saved to `benchmark_results.csv` with columns:
- model
- prompt
- latency
- response_length
- response

## Requirements
```bash
pip install torch transformers pandas
```

## Usage
Run the notebook cells in order. The evaluation loop will test each model on each prompt and collect performance metrics.
