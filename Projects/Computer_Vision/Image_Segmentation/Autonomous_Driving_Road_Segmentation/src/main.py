
import cv2
import matplotlib.pyplot as plt


# Load the image
image = cv2.imread("../inputs_images/road.jpg")

if image is None:
    print("Error: Image not found")
    exit()

print("Image loaded successfully")


# Convert BGR to HSV
image_hsv = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2HSV
)


# Define the HSV range
lower = (0, 0, 0)
upper = (180, 255, 255)


# Apply HSV thresholding
mask = cv2.inRange(
    image_hsv,
    lower,
    upper
)


# Create a morphological kernel
kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (5, 5)
)


# Apply morphological opening
mask = cv2.morphologyEx(
    mask,
    cv2.MORPH_OPEN,
    kernel
)


# Apply morphological closing
mask = cv2.morphologyEx(
    mask,
    cv2.MORPH_CLOSE,
    kernel
)


# Apply the mask to the original image
segmentation = cv2.bitwise_and(
    image,
    image,
    mask=mask
)


# Save the final segmentation
output_path = "../output_images/final_segmentation.png"

cv2.imwrite(
    output_path,
    segmentation
)


# Convert BGR to RGB for Matplotlib
segmentation_rgb = cv2.cvtColor(
    segmentation,
    cv2.COLOR_BGR2RGB
)


# Display the final result
plt.figure(figsize=(10, 7))
plt.imshow(segmentation_rgb)
plt.title("Road Segmentation")
plt.axis("off")
plt.show()

