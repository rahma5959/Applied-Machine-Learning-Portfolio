import os
import numpy as np
import cv2
import csv
from skimage.feature import graycomatrix, graycoprops

# Folders
input_images = "input_images"
output_images = "output_images"
os.makedirs(output_images, exist_ok=True)

def segment_image(image_path, writer, slice_thickness=5):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None

    print(f"Processing {os.path.basename(image_path)}")

    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Denoising
    denoised = cv2.GaussianBlur(gray, (5,5), 0)

    # Brain mask using Otsu
    _, brain_mask = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3,3), np.uint8)
    brain_mask = cv2.morphologyEx(brain_mask, cv2.MORPH_OPEN, kernel)

    # Apply brain mask
    brain_only = cv2.bitwise_and(gray, gray, mask=brain_mask)

    # Tumor segmentation
    _, tumor_mask = cv2.threshold(brain_only, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    tumor_mask = cv2.morphologyEx(tumor_mask, cv2.MORPH_OPEN, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(tumor_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print(f"No tumor detected in {os.path.basename(image_path)}")

    total_volume = 0

    for idx, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area < 20:  # ignore small noise
            continue

        # Volume estimation
        volume = area * slice_thickness
        total_volume += volume

        # Draw contour
        cv2.drawContours(output, [cnt], -1, (0, 0, 255), 2)

        # Create mask for this tumor
        mask_region = np.zeros_like(gray, dtype=np.uint8)
        cv2.drawContours(mask_region, [cnt], -1, 255, -1)

        # Apply mask to isolate tumor
        tumor_region = cv2.bitwise_and(gray, gray, mask=mask_region)

        # Texture feature (GLCM contrast)
        glcm = graycomatrix(
            tumor_region,
            distances=[1],
            angles=[0, np.pi/4, np.pi/2, 3*np.pi/4],
            levels=256,
            symmetric=True,
            normed=True
        )
        contrast = graycoprops(glcm, 'contrast').mean()

        # Write to CSV
        writer.writerow([
            os.path.basename(image_path),
            idx,
            round(area,2),
            round(volume,2),
            round(contrast,4)
        ])

    # Put total volume on the image
    cv2.putText(
        output,
        f"Total Volume: {round(total_volume,2)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    return output

def main():
    os.makedirs(output_images, exist_ok=True)
    csv_path = os.path.join(output_images, "tumor_report.csv")

    with open(csv_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Image", "Tumor_ID", "Area(px)", "Volume(px³ approx)", "GLCM_Contrast"])

        for filename in os.listdir(input_images):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                print(filename)
                path = os.path.join(input_images, filename)
                print(path)
                path = os.path.join(input_images, filename)
                print("Absolute path:", os.path.abspath(path))
                print("Exists?", os.path.exists(path))
                result = segment_image(path, writer)

                if result is not None:
                    cv2.imwrite(os.path.join(output_images, filename), result)

    print(f"Processing completed. Output saved in '{output_images}'")
    print(f"CSV report saved as '{csv_path}'")

if __name__ == "__main__":
    main()
