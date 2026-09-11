# Color-Based Object Detection

## Objective
Detect red objects in images using classical computer vision techniques (no ML, no DL).

## Method
1. Convert image from BGR to HSV color space.
2. Apply color threshold to isolate red pixels (create mask).
3. Remove small noise with morphological operations.
4. Find object contours in the mask.
5. Draw bounding boxes around detected objects.

## Input
- Place images in `input_images/` folder
- Supported formats: .jpg, .png, .jpeg

## Output
- Processed images with bounding boxes are saved in `output_images/`

## How to Run
```bash
python 01_color_based_detection.py
