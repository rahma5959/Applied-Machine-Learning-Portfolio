# Product Image Feature Extraction (HOG)

## Objective
Extract meaningful features from product images (shoes, bags, clothes) using classical computer vision for downstream ML tasks.

## Problem Type
Feature extraction – numerical representation of images.

## Dataset
Images are placed in the `input_images/` folder. No labels are required at this stage.

## Input Features
- Raw product images (RGB)
- Grayscale conversion applied
- HOG features capture edge and shape information

## Output
- Feature vectors saved as a pickle file `hog_features.pkl` in `output_features/`
- Each image corresponds to a 1D numpy array

## Model / Method
**HOG (Histogram of Oriented Gradients)**

### Why HOG?
- Captures local edge orientation (shape)
- Robust to illumination changes
- Works well for classical ML algorithms like KNN, SVM
- Computationally efficient
- Easy to explain in interviews

## HOG Parameters
| Parameter         | Value       | Description                           |
|------------------|------------|---------------------------------------|
| orientations      | 9          | Number of gradient bins               |
| pixels_per_cell   | (8,8)      | Size of the cell for gradient histogram |
| cells_per_block   | (2,2)      | Number of cells per block             |
| block_norm        | 'L2-Hys'   | Normalization method                   |

## How to run
```bash
python Product_Image_Extraction.py
