import os
import cv2
import numpy as np
from skimage.feature import hog
import pickle

# Paths
input_images = "input_images"
output_features = "output_features"
os.makedirs(output_features, exist_ok=True)

# HOG parameters
hog_params = {
    "orientations": 9,
    "pixels_per_cell": (8, 8),
    "cells_per_block": (2, 2),
    "block_norm": "L2-Hys"
}

def extract_hog_features(image_path):
    """
    Reads an image, converts to grayscale, extracts HOG features.
    Returns a 1D numpy array.
    """
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Extract HOG features
    features, hog_image = hog(gray, visualize=True, **hog_params)

    
    return features, hog_image

def main():
    feature_dict = {} 

    for filename in os.listdir(input_images):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_images, filename)
            features, hog_image = extract_hog_features(input_path)
            if features is not None:
                feature_dict[filename] = features
                output_hog_path = os.path.join(output_features, f"{filename}")
                hog_img= (hog_image * 255).astype(np.uint8)
                cv2.imwrite(output_hog_path, hog_img)
                print(f"Extracted HOG features for {filename} → length: {len(features)}")

    # Save feature dictionary to a file
    with open(os.path.join(output_features, "hog_features.pkl"), "wb") as f:
        pickle.dump(feature_dict, f)
        print(f"\n All features saved to {os.path.join(output_features,'hog_features.pkl')}")

if __name__ == "__main__":
    main()
