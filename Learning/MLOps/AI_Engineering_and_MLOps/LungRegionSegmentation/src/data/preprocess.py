import cv2
import os

INPUT_DIR = "data/raw"
OUTPUT_DIR = "data/processed"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for img_name in os.listdir(INPUT_DIR):
    path = os.path.join(INPUT_DIR, img_name)

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error loading {img_name}")
        continue

    # Resize
    img = cv2.resize(img, (256, 256))

    # Denoise
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # Contrast enhancement
    img = cv2.equalizeHist(img)

    cv2.imwrite(os.path.join(OUTPUT_DIR, img_name), img)

print("Preprocessing done")