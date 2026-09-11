# Brain MRI Tumor & Necrotic Spot Detection

This project performs tumor segmentation and necrotic spot detection
from grayscale brain MRI images using classical computer vision techniques.

## Objective

- Detect and count separate tumor regions
- Detect necrotic (dark) spots inside each tumor
- Visualize segmentation results

##  Methods Used

- Gaussian Blur (noise reduction)
- Otsu Thresholding
- Morphological Operations
- Distance Transform
- Watershed Segmentation
- Connected Components
- Contour Detection

##  Project Structure

images/        → input MRI images  
results/       → output segmented images  
train.py       → main processing script  


## How to Run

1. Place MRI images inside the `images` folder.
2. Run:

python Brain_MRI_Tumor_Detection.py
