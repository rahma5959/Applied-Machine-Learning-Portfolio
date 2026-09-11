# Coin Segmentation

## Objective

Segment coins from the background and separate touching coins using classical computer vision techniques.

## Pipeline

```text
Image
 ↓
Grayscale
 ↓
Gaussian Blur
 ↓
Otsu Thresholding
 ↓
Morphological Opening
 ↓
Morphological Closing
 ↓
Distance Transform
 ↓
Markers
 ↓
Watershed
 ↓
Final Segmentation
```

## Project Structure

```text
Coin_Segmentation/
├── input_images/
│   └── coins.jpg
├── output_images/
│   └── final_segmentation.png
├── src/
│   └── main.py
└── README.md
```

## Techniques

* **Grayscale** → simplify the image
* **Gaussian Blur** → reduce noise
* **Otsu** → separate foreground and background
* **Morphology** → clean the binary mask
* **Distance Transform** → find coin centers
* **Connected Components** → create markers
* **Watershed** → separate touching coins

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
