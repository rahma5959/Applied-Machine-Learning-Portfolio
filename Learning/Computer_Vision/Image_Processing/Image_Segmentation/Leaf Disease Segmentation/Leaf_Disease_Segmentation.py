import os
import cv2
import numpy as np

# Folders
input_images = "input_images"
output_images = "output_images"
os.makedirs(output_images, exist_ok=True)

def segment_disease(image_path):
    """
    Segments diseased areas on leaf images using classical image processing.
    Returns:
        original image, binary mask, image with contours drawn
    """
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None, None, None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)

    # Denoise with Gaussian Blur
    denoised = cv2.GaussianBlur(enhanced, (5,5), 0)

    # Thresholding (invert binary for spots)
    _, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Morphological opening to remove small noise
    kernel = np.ones((3,3), np.uint8)
    cleaned_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Find contours of diseased areas
    contours, _ = cv2.findContours(cleaned_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on a copy of original image
    output_contours = img.copy()
    cv2.drawContours(output_contours, contours, -1, (0,255,0), 2)

    print(f"Detected {len(contours)} diseased areas in {os.path.basename(image_path)}")

    return img, cleaned_mask, output_contours


if __name__ == "__main__":
    for filename in os.listdir(input_images):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_images, filename)
            original, mask, contoured = segment_disease(img_path)

            if original is not None:
                # Save binary mask
                cv2.imwrite(os.path.join(output_images, "mask_" + filename), mask)
                # Save image with contours
                cv2.imwrite(os.path.join(output_images, "contours_" + filename), contoured)

    print("All images processed and saved in", output_images)
