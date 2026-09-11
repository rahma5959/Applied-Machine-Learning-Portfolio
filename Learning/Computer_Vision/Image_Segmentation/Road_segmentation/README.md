# Road Segmentation

## Objective

Segment road regions from a road image using color information in the HSV color space.

## Problem

The goal is to identify pixels that are likely to belong to the road and separate them from other regions such as trees, buildings, cars, and sky.

Unlike the previous segmentation projects, the road is not necessarily a closed object and its appearance can vary depending on illumination and scene conditions.

## Pipeline

```text
Input Image
     ↓
BGR → HSV
     ↓
HSV Thresholding
     ↓
Road Mask
     ↓
Morphological Opening
     ↓
Morphological Closing
     ↓
Clean Road Mask
     ↓
Bitwise AND
     ↓
Final Segmentation
```

## Techniques

### HSV Color Space

The image is converted from BGR to HSV.

HSV separates:

* Hue → color information
* Saturation → color intensity
* Value → brightness

This makes it easier to select pixels based on their color and brightness characteristics.

### HSV Thresholding

`cv2.inRange()` is used to select pixels inside a predefined HSV range.

Example:

```python
lower = (0, 0, 40)
upper = (180, 80, 220)
```

This range mainly selects pixels with relatively low saturation and intermediate brightness, which can correspond to road surfaces such as gray asphalt.

### Morphological Opening

Opening is applied to remove small isolated regions and noise from the binary road mask.

Opening consists of:

```text
Erosion
   ↓
Dilation
```

### Morphological Closing

Closing is used to fill small holes and connect small gaps in the road mask.

Closing consists of:

```text
Dilation
   ↓
Erosion
```

### Bitwise AND

`cv2.bitwise_and()` applies the final mask to the original image.

Pixels corresponding to white regions in the mask are preserved, while pixels corresponding to black regions are removed.

## Project Structure

```text
Road_Segmentation/
├── input_images/
│   └── road.jpg
├── output_images/
│   └── final_segmentation.png
├── src/
│   └── main.py
└── README.md
```

## Run

From the `Road_Segmentation` directory:

```bash
python src/main.py
```

## Result

The final segmented image is saved in:

```text
output_images/final_segmentation.png
```

## Limitations

The method is based on manually selected HSV thresholds.

Therefore, the segmentation may not work correctly when:

* the road has a different color,
* illumination changes significantly,
* the road is wet,
* strong shadows are present,
* other objects have similar colors to the road.

This project demonstrates a classical color-based segmentation approach rather than a deep learning segmentation model.

## Tools

Python · OpenCV · Matplotlib
