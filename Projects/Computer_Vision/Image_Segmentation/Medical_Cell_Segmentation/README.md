# Medical Cell Segmentation

## Objective

Segment cells in microscopic medical images and separate cells that are close or touching using advanced computer vision techniques.

## Use Case

This project demonstrates medical image analysis capabilities for cell counting and detection in histopathology, cytology, and other biomedical applications.

## Pipeline

```
Image
 ↓
Grayscale
 ↓
CLAHE (Contrast Limited Adaptive Histogram Equalization)
 ↓
Adaptive Thresholding
 ↓
Morphological Opening
 ↓
Morphological Closing
 ↓
Distance Transform
 ↓
Sure Foreground / Background
 ↓
Markers
 ↓
Watershed Algorithm
 ↓
Final Segmentation
```

## Techniques

* **Grayscale** → Simplify the image for processing
* **CLAHE** → Improve local contrast and enhance cell boundaries
* **Adaptive Thresholding** → Handle local intensity variations in medical images
* **Morphological Operations** → Clean the binary mask and remove noise
* **Distance Transform** → Find cell centers accurately
* **Connected Components** → Create markers for watershed
* **Watershed Algorithm** → Separate touching/overlapping cells

## Project Structure

```text
Medical_Cell_Segmentation/
├── input_images/
│   └── cells.png
├── output_images/
│   └── final_segmentation.png
├── src/
│   └── main.py
└── README.md
```

## Installation

```bash
pip install opencv-python matplotlib numpy
```

## Run

```bash
python src/main.py
```

## Result

The final segmentation is saved in:

```text
output_images/final_segmentation.png
```

## Key Features

- Handles overlapping cells in medical images
- Adaptive thresholding for varying illumination conditions
- Watershed algorithm for precise cell separation
- CLAHE for enhanced contrast in microscopic images

## Tools & Technologies

Python · OpenCV · Matplotlib · NumPy

## Applications

- Medical diagnostics
- Cell counting in pathology
- Biomedical research
- Histopathology analysis
- Cytology automation