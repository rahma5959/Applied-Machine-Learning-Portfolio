# Edge Detection

## Objective
Detect edges in an image to highlight object boundaries and structural information.

## Problem Type
Image preprocessing (Computer Vision – classical image processing).

## Why Edge Detection?
Edges correspond to:
- Object boundaries
- Shape information
- Important visual features

They are often used before:
- Object detection
- Image segmentation
- Feature extraction

## Methods Used
- Sobel Filter
- Canny Edge Detector

## Input
- RGB or grayscale image

## Output
- Binary or grayscale image showing detected edges

## Why Canny?
- Robust to noise
- Uses gradient + non-maximum suppression
- Produces thin and clean edges
- Widely used in industry

## Libraries
- OpenCV
- NumPy
- Matplotlib

## How to run
```bash
python Edge_Detection.py
