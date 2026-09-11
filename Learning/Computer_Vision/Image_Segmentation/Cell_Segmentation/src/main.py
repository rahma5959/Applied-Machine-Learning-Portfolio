
import cv2
import matplotlib.pyplot as plt


# Load the image
image = cv2.imread("../input_image/celles.jpg")

if image is None:
    print("Error: Image not found")
    exit()

print("Image loaded successfully")


# Convert to grayscale
image_gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)


# Enhance local contrast
clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

image_clahe = clahe.apply(image_gray)


# Apply adaptive thresholding
image_thresh = cv2.adaptiveThreshold(
    image_clahe,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    31,
    5
)


# Apply morphological operations
kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (5, 5)
)

image_opened = cv2.morphologyEx(
    image_thresh,
    cv2.MORPH_OPEN,
    kernel
)

image_closed = cv2.morphologyEx(
    image_opened,
    cv2.MORPH_CLOSE,
    kernel
)


# Apply Euclidean Distance Transform
distance = cv2.distanceTransform(
    image_closed,
    cv2.DIST_L2,
    5
)


# Extract Sure Foreground
_, sure_foreground = cv2.threshold(
    distance,
    0.5 * distance.max(),
    255,
    cv2.THRESH_BINARY
)

sure_foreground = sure_foreground.astype("uint8")


# Extract Sure Background
sure_background = cv2.dilate(
    image_closed,
    kernel,
    iterations=3
)


# Identify the Unknown Region
unknown = cv2.subtract(
    sure_background,
    sure_foreground
)


# Generate Watershed Markers
num_markers, markers = cv2.connectedComponents(
    sure_foreground
)

markers = markers + 1
markers[unknown == 255] = 0


# Convert Grayscale Image to BGR
color_image = cv2.cvtColor(
    image_gray,
    cv2.COLOR_GRAY2BGR
)


# Apply Watershed Segmentation
markers = cv2.watershed(
    color_image,
    markers
)


# Highlight Watershed Boundaries
segmentation = color_image.copy()

segmentation[markers == -1] = [0, 0, 255]


# Save the final segmentation
output_path = "output_images/final_segmentation.png"

cv2.imwrite(
    output_path,
    segmentation
)


# Display the final result
segmentation_rgb = cv2.cvtColor(
    segmentation,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(10, 7))
plt.imshow(segmentation_rgb)
plt.title("Cell Segmentation - Watershed")
plt.axis("off")
plt.show()

