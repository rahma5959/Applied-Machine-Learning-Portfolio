# Autonomous Driving Road Segmentation

## Objective

Segment road regions from driving scenarios using color information in the HSV color space for autonomous vehicle navigation and driver assistance systems.

## Use Case

This project demonstrates computer vision techniques for autonomous driving applications, specifically road detection and lane identification for self-driving vehicles and ADAS (Advanced Driver Assistance Systems).

## Problem

The goal is to identify pixels that belong to the road surface and separate them from other regions such as vehicles, pedestrians, buildings, vegetation, and sky.

Unlike traditional object segmentation, road regions are not necessarily closed objects and their appearance can vary significantly depending on:
- Weather conditions (rain, snow, fog)
- Illumination changes (day/night, shadows)
- Road surface materials (asphalt, concrete, gravel)
- Environmental factors (wet roads, markings)

## Pipeline

```
Input Image
     ↓
BGR → HSV Color Space Conversion
     ↓
HSV Thresholding (Road Color Detection)
     ↓
Road Mask Generation
     ↓
Morphological Opening (Noise Removal)
     ↓
Morphological Closing (Gap Filling)
     ↓
Clean Road Mask
     ↓
Bitwise AND (Final Segmentation)
     ↓
Final Road Segmentation
```

## Techniques

### HSV Color Space

The image is converted from BGR to HSV for robust color-based segmentation.

HSV separates:
- **Hue** → Color information (0-180°)
- **Saturation** → Color intensity (0-255)
- **Value** → Brightness (0-255)

This makes it easier to select pixels based on their color and brightness characteristics, which is crucial for road detection under varying lighting conditions.

### HSV Thresholding

`cv2.inRange()` is used to select pixels inside a predefined HSV range that corresponds to typical road surface colors.

Example range for gray asphalt roads:

```python
lower = (0, 0, 40)   # Low saturation, moderate brightness
upper = (180, 80, 220) # Wide hue range, controlled saturation/brightness
```

This range mainly selects pixels with relatively low saturation and intermediate brightness, which typically correspond to road surfaces like gray asphalt.

### Morphological Opening

Opening is applied to remove small isolated regions and noise from the binary road mask.

Opening consists of:
```
Erosion → Removes small objects
   ↓
Dilation → Restores object sizes
```

### Morphological Closing

Closing is used to fill small holes and connect small gaps in the road mask, ensuring continuous road detection.

Closing consists of:
```
Dilation → Fills small holes
   ↓
Erosion → Restores boundary precision
```

### Bitwise AND

`cv2.bitwise_and()` applies the final mask to the original image.

Pixels corresponding to white regions in the mask are preserved (road), while pixels corresponding to black regions are removed (non-road).

## Project Structure

```text
Autonomous_Driving_Road_Segmentation/
├── input_images/
│   └── road.jpg
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

The final segmented image is saved in:

```text
output_images/final_segmentation.png
```

## Limitations & Future Improvements

The current method uses manually selected HSV thresholds, which may not work optimally when:
- Road surface colors vary significantly
- Extreme illumination changes occur
- Road is wet or has different reflectivity
- Strong shadows are present
- Other objects have similar colors to the road

**Future improvements for production autonomous driving:**
- Deep learning-based semantic segmentation (U-Net, DeepLab)
- Multi-spectral camera integration
- Real-time video processing
- Adaptive thresholding based on scene analysis
- Integration with GPS and mapping data

## Tools & Technologies

Python · OpenCV · Matplotlib · NumPy

## Autonomous Driving Applications

- Lane detection and tracking
- Road boundary identification
- Drivable area detection
- Autonomous navigation
- Driver assistance systems (ADAS)
- Path planning for self-driving vehicles