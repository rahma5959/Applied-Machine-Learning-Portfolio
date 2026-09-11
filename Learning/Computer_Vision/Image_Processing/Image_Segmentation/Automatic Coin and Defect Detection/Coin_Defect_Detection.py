import os
import cv2
import numpy as np


INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def process_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error loading {image_path}")
        return None

    original = img.copy()

    # Preprocessing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    blurred = cv2.GaussianBlur(enhanced, (5, 5), 0)

    # Thresholding
    _, thresh = cv2.threshold(
        blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Morphology (clean noise)
    kernel = np.ones((3, 3), np.uint8)
    clean_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Distance Transform (for separating touching coins)
    dist = cv2.distanceTransform(clean_mask, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist, 0.4 * dist.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    sure_bg = cv2.dilate(clean_mask, kernel, iterations=3)
    unknown = cv2.subtract(sure_bg, sure_fg)

    #  Watershed
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    markers = cv2.watershed(original, markers)

    coin_count = 0
    defect_total = 0

    output = original.copy()

    for marker_id in np.unique(markers):
        if marker_id <= 1:
            continue

        coin_mask = np.zeros(gray.shape, dtype=np.uint8)
        coin_mask[markers == marker_id] = 255

        # Count coin
        coin_count += 1

        # Detect defects inside this coin
        coin_region = cv2.bitwise_and(gray, gray, mask=coin_mask)

        # Threshold defects (dark spots)
        _, defect_mask = cv2.threshold(
            coin_region, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

        defect_mask = cv2.morphologyEx(
            defect_mask, cv2.MORPH_OPEN, kernel, iterations=1
        )

        contours, _ = cv2.findContours(
            defect_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 20:  # ignore very small noise
                defect_total += 1
                cv2.drawContours(output, [cnt], -1, (0, 0, 255), 1)

        # Draw coin boundary
        contours_coin, _ = cv2.findContours(
            coin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        cv2.drawContours(output, contours_coin, -1, (0, 255, 0), 2)

    print(f"{os.path.basename(image_path)} → Coins: {coin_count}, Defects: {defect_total}")

    return output


if __name__ == "__main__":
    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            path = os.path.join(INPUT_DIR, file)
            result = process_image(path)

            if result is not None:
                save_path = os.path.join(OUTPUT_DIR, "processed_" + file)
                cv2.imwrite(save_path, result)

    print("Processing completed.")
