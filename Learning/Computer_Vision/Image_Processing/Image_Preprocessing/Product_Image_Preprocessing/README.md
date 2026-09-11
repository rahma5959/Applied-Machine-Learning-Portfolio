# Product Image Preprocessing

## Objective
Preprocess product images to make them ready for downstream tasks like classification, segmentation, or feature extraction.

## Problem Type
Image preprocessing for structured and consistent input to computer vision models.

## Dataset
- Raw product images of different sizes, lighting, and quality.
- Stored in `input_images/`.

## Preprocessing Steps
1. Resize images to a target size (224x224) while keeping aspect ratio.
2. Pad images with black borders to maintain uniform size.
3. Convert images to grayscale.
4. Normalize pixel values to [0,1].
5. Apply Gaussian blur to reduce noise.

## Output
- Preprocessed images saved in `output_images/`.
- Ready for machine learning or deep learning models.

## How to Run
```bash
python Product_Image_Preprocessing.py
