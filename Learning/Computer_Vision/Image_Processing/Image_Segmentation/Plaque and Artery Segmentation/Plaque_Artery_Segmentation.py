import csv
import os 
import cv2
import numpy as np
from skimage.feature import graycomatrix, graycoprops

input_images = "input_images"   
output_images = "output_images"
os.makedirs(output_images, exist_ok=True)

def segment_image(image_path, writer):

    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    image_denoised = cv2.GaussianBlur(gray, (5,5), 0)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    image_clahe = clahe.apply(image_denoised)

    # Artery segmentation
    _, artery_mask = cv2.threshold(
        image_clahe, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    kernel = np.ones((5,5), np.uint8)
    artery_mask = cv2.morphologyEx(
        artery_mask, cv2.MORPH_OPEN, kernel, iterations=2
    )

    # Keep only largest connected component as main artery
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(artery_mask)

    if num_labels > 1:
        largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
        artery_mask = np.uint8(labels == largest_label) * 255

    artery_region = cv2.bitwise_and(gray, gray, mask=artery_mask)

    # Plaque segmentation restricted inside artery
    _, plaque_mask = cv2.threshold(
        artery_region, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    plaque_mask = cv2.morphologyEx(
        plaque_mask, cv2.MORPH_OPEN, kernel, iterations=2
    )

    # Force plaque to remain inside artery
    plaque_mask = cv2.bitwise_and(plaque_mask, artery_mask)

    contours, _ = cv2.findContours(
        plaque_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    plaque_total = 0
    output = img.copy()

    for idx, cnt in enumerate(contours):

        area = cv2.contourArea(cnt)

        if area < 30:
            continue

        plaque_total += area

        cv2.drawContours(output, [cnt], -1, (0,0,255), 2)

        mask_region = np.zeros_like(gray)
        cv2.drawContours(mask_region, [cnt], -1, 255, -1)

        plaque_region = cv2.bitwise_and(gray, gray, mask=mask_region)

        # Reduce gray levels for more stable GLCM
        plaque_region_quantized = (plaque_region / 8).astype(np.uint8)

        glcm = graycomatrix(
            plaque_region_quantized,
            distances=[1],
            angles=[0, np.pi/4, np.pi/2, 3*np.pi/4],
            levels=32,
            symmetric=True,
            normed=True
        )

        contrast = graycoprops(glcm, 'contrast').mean()

        writer.writerow([
            os.path.basename(image_path),
            idx,
            round(area,2),
            round(contrast,4)
        ])

    artery_area = np.sum(artery_mask > 0)

    if artery_area > 0:
        stenosis_percent = min((plaque_total / artery_area) * 100, 100)
    else:
        stenosis_percent = 0

    cv2.putText(
        output,
        f"Stenosis: {round(stenosis_percent,2)}%",
        (10,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )

    return output


def main():

    csv_path = os.path.join(output_images, "report.csv")

    with open(csv_path, mode="w", newline="") as f:

        writer = csv.writer(f)
        writer.writerow([
            "Image",
            "Plaque_ID",
            "Plaque_Area(px)",
            "GLCM_Contrast"
        ])

        for filename in os.listdir(input_images):

            if filename.lower().endswith((".jpg",".png",".jpeg")):

                image_path = os.path.join(input_images, filename)

                result = segment_image(image_path, writer)

                if result is not None:
                    cv2.imwrite(
                        os.path.join(output_images, filename),
                        result
                    )

    print("\nProcessing completed.")
    print(f"Results saved in: {output_images}")


if __name__ == "__main__":
    main()
