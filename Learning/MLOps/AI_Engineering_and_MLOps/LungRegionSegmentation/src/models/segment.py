import cv2
import os

INPUT_DIR = "data/processed"
OUTPUT_DIR = "data/masks"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for img_name in os.listdir(INPUT_DIR):
    path = os.path.join(INPUT_DIR, img_name)

    img = cv2.imread(path, 0)

    if img is None:
        print(f"Error loading {img_name}")
        continue

    # --- Step 1: Otsu Thresholding ---
    _, mask = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # --- Step 2: Morphological Refinement ---
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    # Close small holes
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Optional: remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Save result
    cv2.imwrite(os.path.join(OUTPUT_DIR, img_name), mask)

print("Segmentation completed")