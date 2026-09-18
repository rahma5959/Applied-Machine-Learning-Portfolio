# Industrial Automated Inspection

## Objective

Segment coins and objects from the background and separate touching items using classical computer vision techniques for industrial quality control and automated inspection systems.

## Use Case

This project demonstrates industrial computer vision applications for quality control, automated counting, and defect detection in manufacturing environments.

## Pipeline

```
Input Image
 ↓
Grayscale Conversion
 ↓
Gaussian Blur (Noise Reduction)
 ↓
Otsu Thresholding
 ↓
Morphological Opening
 ↓
Morphological Closing
 ↓
Distance Transform
 ↓
Marker Creation
 ↓
Watershed Algorithm
 ↓
Final Segmentation
```

## Techniques

* **Grayscale** → Simplify the image for processing
* **Gaussian Blur** → Reduce noise and smooth the image
* **Otsu Thresholding** → Automatically separate foreground and background
* **Morphological Operations** → Clean the binary mask and remove artifacts
* **Distance Transform** → Find object centers accurately
* **Connected Components** → Create markers for watershed
* **Watershed Algorithm** → Separate touching/overlapping objects

## Project Structure

```text
Industrial_Automated_Inspection/
├── input_images/
│   └── coins.jpg
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

- Automated object detection and separation
- Robust to touching/overlapping items
- Industrial quality control applications
- High-precision segmentation for manufacturing
- Classical computer vision approach (real-time performance)

## Tools & Technologies

Python · OpenCV · Matplotlib · NumPy

## Industrial Applications

- Quality control in manufacturing
- Automated counting systems
- Defect detection
- Production line monitoring
- Inventory management
- Precision manufacturing inspection