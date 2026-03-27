import os 
import numpy as np
import cv2

# Load the images
input_images = "input_images"
output_images = "output_images"

os.makedirs(output_images, exist_ok=True)

def segment_cells(image_path):
    img=cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Denoise
    image_denoised = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding (Otsu)
    _, thresh = cv2.threshold(image_denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Morphological opening to remove small noise
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on original image
    output_contours = img.copy()
    cv2.drawContours(output_contours, contours, -1, (0, 255, 0), 2)

    print(f"Detected {len(contours)} objects in {os.path.basename(image_path)}")

    return img, opening, output_contours


if __name__ == "__main__":
    for filename in os.listdir(input_images):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_images, filename)

            # Segment cells
            original, mask, contoured = segment_cells(img_path)

            if original is not None:
                # Save binary mask
                cv2.imwrite(os.path.join(output_images, "mask_" + filename), mask)
                # Save image with contours
                cv2.imwrite(os.path.join(output_images, "contours_" + filename), contoured)

    print("All images processed and saved in", output_images)