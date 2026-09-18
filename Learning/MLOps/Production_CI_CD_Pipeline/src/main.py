import cv2
import os


# Define input and output paths
input_path = "../input_images/pomme.jpg"
output_path = "../output_images/mask.png"


# Read the image
image = cv2.imread(input_path)

if image is None:
    raise FileNotFoundError(f"Image not found: {input_path}")


# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Apply Otsu thresholding
threshold, mask = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)


# Save the segmentation mask
cv2.imwrite(output_path, mask)


print("=== SEGMENTATION COMPLETED ===")
print(f"Otsu threshold: {threshold}")
print(f"Mask saved to: {output_path}")