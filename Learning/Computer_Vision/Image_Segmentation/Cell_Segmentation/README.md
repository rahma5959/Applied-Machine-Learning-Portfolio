# Cell Segmentation

## Objective

Segment cells in a microscopic image and separate cells that are close or touching.

## Pipeline

Image
↓
Grayscale
↓
CLAHE
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
Watershed
↓
Final Segmentation

## Techniques

* Grayscale → simplify the image
* CLAHE → improve local contrast
* Adaptive Thresholding → handle local intensity variations
* Morphology → clean the binary mask
* Distance Transform → find cell centers
* Connected Components → create markers
* Watershed → separate touching cells

## Project Structure

```text
Cell_Segmentation/
├── input_images/
│   └── celles.png
├── output_images/
│   └── final_segmentation.png
├── src/
│   └── main.py
└── README.md
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

## Tools

Python · OpenCV · Matplotlib
