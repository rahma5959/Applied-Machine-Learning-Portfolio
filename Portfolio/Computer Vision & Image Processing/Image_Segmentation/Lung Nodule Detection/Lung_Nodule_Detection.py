import os
import cv2
import numpy as np
import csv


def segment_lung_nodules(image_path, writer):

    img = cv2.imread(image_path)
    if img is None:
        print(f"Error loading {image_path}")
        return None

    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Denoising
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Lung segmentation
    _, thresh = cv2.threshold(
        blur, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    kernel = np.ones((3, 3), np.uint8)

    opening = cv2.morphologyEx(
        thresh, cv2.MORPH_OPEN, kernel, iterations=2
    )

    # Watershed preparation
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(
        dist, 0.5 * dist.max(), 255, 0
    )

    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Markers
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    markers = cv2.watershed(img, markers)

    lung_mask = np.zeros(gray.shape, dtype=np.uint8)
    lung_mask[markers > 1] = 255

    # Draw lung contour
    contours_lung, _ = cv2.findContours(
        lung_mask, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    cv2.drawContours(output, contours_lung, -1, (0, 255, 0), 2)

    # Nodule detection
    lung_region = cv2.bitwise_and(gray, gray, mask=lung_mask)

    _, nodules = cv2.threshold(
        lung_region, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    nodules = cv2.morphologyEx(
        nodules, cv2.MORPH_OPEN, kernel
    )

    contours_nodules, _ = cv2.findContours(
        nodules,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    nodule_count = 0
    high_risk = 0

    for idx, cnt in enumerate(contours_nodules):

        area = cv2.contourArea(cnt)

        if area < 30:
            continue

        nodule_count += 1

        diameter = np.sqrt(4 * area / np.pi)

        if diameter < 10:
            risk = "Low"
            color = (0, 255, 0)
        elif diameter < 20:
            risk = "Medium"
            color = (0, 165, 255)
        else:
            risk = "High"
            color = (0, 0, 255)
            high_risk += 1

        cv2.drawContours(output, [cnt], -1, color, 2)

        # Write one line in CSV
        writer.writerow(
            [image_path, idx, round(area, 2),
             round(diameter, 2), risk]
        )

    cv2.putText(
        output,
        f"Nodules: {nodule_count} | High Risk: {high_risk}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 255, 255),
        2,
    )

    return output


def main():

    input_folder = "input_images"
    output_folder = "output_images"

    os.makedirs(output_folder, exist_ok=True)

    with open("nodule_report.csv", mode="w", newline="") as file:

        writer = csv.writer(file)

        # Write header
        writer.writerow(
            ["Image", "Nodule_ID", "Area(px)",
             "Diameter(px)", "Risk"]
        )

        for filename in os.listdir(input_folder):

            path = os.path.join(input_folder, filename)

            result = segment_lung_nodules(path, writer)

            if result is not None:
                cv2.imwrite(
                    os.path.join(output_folder, filename),
                    result
                )

    print("Processing completed.")


if __name__ == "__main__":
    main()
