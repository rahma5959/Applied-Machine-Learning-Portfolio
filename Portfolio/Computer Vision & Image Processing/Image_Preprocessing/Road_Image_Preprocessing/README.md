# Road Image Preprocessing for Lane Detection

## Objective
Prepare raw road images for lane detection by applying classical image preprocessing techniques.

This project focuses on improving image quality before applying edge detection or lane detection algorithms.

## Problem Type
Computer Vision – Image Preprocessing  
(No machine learning, no deep learning)
## Dataset
Raw RGB road images with:
- Different lighting conditions
- Sensor noise
- Irrelevant background (sky, trees)

## Preprocessing Pipeline

### 1. Grayscale Conversion
- Simplifies image information
- Lane markings rely on intensity, not color

### 2. Noise Reduction (Gaussian Blur)
- Removes small noise
- Prevents false edge detection

### 3. Contrast Enhancement
- Histogram equalization improves lane visibility
- Works well under varying lighting conditions

### 4. Region of Interest (ROI)
- Keeps only the road area
- Removes sky and irrelevant regions

## Input / Output

### Input
- Raw road images (RGB)

### Output
- Enhanced grayscale images
- Cropped to focus on road area
- Saved in `output_images/`

## Folder Structure

