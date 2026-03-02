# Shelf Image Preprocessing

## Objective
Prepare raw supermarket shelf images for downstream computer vision tasks such as:
- Product detection
- Price tag recognition
- Shelf analytics

This project focuses on **image preprocessing**, not machine learning.

## Problem Type
Image Preprocessing (Computer Vision)

## Input
- RGB images of supermarket shelves
- Different lighting conditions
- Various resolutions
- Noise and blur

## Output
- Clean grayscale images
- Standardized resolution
- Reduced noise
- Enhanced contrast
- Saved in `output_images/`

## Preprocessing Steps

1. **Resize**
   - Ensures all images have the same dimensions

2. **Grayscale Conversion**
   - Reduces color variability
   - Focuses on structure and texture

3. **Gaussian Blur**
   - Reduces sensor noise

4. **CLAHE (Contrast Limited Adaptive Histogram Equalization)**
   - Handles uneven lighting
   - Improves visibility of products and text

## Folder Structure


