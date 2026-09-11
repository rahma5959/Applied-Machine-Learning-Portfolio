# Lung Nodule Detection & Risk Scoring

This project performs automatic lung segmentation and pulmonary nodule detection from CT scan images using classical computer vision techniques.

##  Objectives

- Segment lung regions
- Detect nodules inside lungs
- Compute:
  - Number of nodules
  - Equivalent diameter
  - Risk classification
- Export a CSV medical-style report

##  Techniques Used

- Gaussian Blur (noise reduction)
- Otsu Thresholding
- Morphological Operations
- Distance Transform
- Watershed Segmentation
- Connected Components
- Contour Detection
- Feature Extraction (area, diameter)

## Project Structure

images/              → Input CT images  
results/             → Output annotated images  
Lung Nodule Detection.py             → Main processing script  
nodule_report.csv    → Generated risk report  

## How to Run

1. Put CT images inside the `images` folder.
2. Run:

python Lung Nodule Detection.py
