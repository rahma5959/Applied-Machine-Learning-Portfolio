# Cell Segmentation Using Classical Image Processing

## Objective
Segment cells from microscope images using traditional computer vision methods without deep learning.

## Steps
1. Convert image to grayscale
2. Apply Gaussian blur
3. Use Otsu thresholding
4. Apply morphological opening
5. Detect contours
6. Count cells

## Requirements
- Python 3.x
- OpenCV
- NumPy

Install dependencies:
pip install opencv-python numpy

## Run
python cell_segmentation.py
