# CCTV Texture Feature Extraction using LBP

## Objective
Extract texture-based features from CCTV images to support anomaly detection and clustering.

## Problem Type
Feature extraction (unsupervised preprocessing step).

## Method
Local Binary Patterns (LBP)

LBP captures local texture patterns by comparing each pixel with its neighboring pixels and encoding the result as a binary number.

## Why LBP?

- Captures micro-texture information
- Computationally efficient
- Robust to illumination changes
- Suitable for anomaly detection and clustering
- No deep learning required

## LBP Hyperparameters

| Parameter | Value | Description |
|-----------|--------|-------------|
| Radius (R) | 1 | Distance from center pixel |
| Points (P) | 8 | Number of neighbors |
| Method | uniform | Reduces dimensionality and improves robustness |

## Input
Images placed in `input_images/`

## Output
- Feature vectors saved in:
  `output_features/lbp_features.pkl`
- Each image corresponds to one normalized histogram vector.

## How to Run

```bash
python CCTV_Texture.py
