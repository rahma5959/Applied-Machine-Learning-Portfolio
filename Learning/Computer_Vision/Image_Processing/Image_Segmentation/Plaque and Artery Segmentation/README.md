# CardioScope-Stenosis

CardioScope-Stenosis is a cardiovascular image processing pipeline designed to simulate coronary artery plaque detection and stenosis estimation from CT Angiography images.

This project demonstrates practical knowledge in:

- Medical Image Processing
- Computer Vision
- Radiomics Feature Extraction
- Cardiovascular Disease Analysis

---

## Objective

To:

1. Segment coronary arteries from CT images
2. Detect atherosclerotic plaques
3. Estimate stenosis percentage
4. Extract texture features (GLCM contrast)
5. Generate a structured CSV report

---

## Methodology

### 1. Preprocessing
- Grayscale conversion
- Gaussian denoising
- CLAHE contrast enhancement

### 2. Artery Segmentation
- Otsu thresholding
- Morphological opening

### 3. Plaque Detection
- Masked thresholding
- Contour extraction

### 4. Feature Extraction
- Plaque area (pixels)
- GLCM texture contrast
- Global stenosis estimation

---

## Stenosis Estimation

Stenosis (%) is approximated as:

Stenosis = (Total Plaque Area / Artery Area) * 100

This simplified approach mimics lumen narrowing estimation in clinical practice.

---

## Output

For each image:

- Annotated output image
- CSV report including:
  - Image name
  - Plaque ID
  - Plaque area
  - Texture contrast

---

## Technical Stack

- Python
- OpenCV
- NumPy
- scikit-image

---

## Recruiter-Level Discussion Points

- Why use CLAHE for vascular structures?
- Limitations of threshold-based segmentation in CTA
- Differences between calcified and non-calcified plaques
- Extension to Deep Learning (U-Net)
- 3D volumetric stenosis estimation using DICOM

---

## Future Improvements

- DICOM support
- 3D vessel reconstruction
- Skeleton-based diameter estimation
- CNN-based plaque classification
- Risk prediction modeling

---

## Author

Rahma – AI & Computer Vision Portfolio Project
