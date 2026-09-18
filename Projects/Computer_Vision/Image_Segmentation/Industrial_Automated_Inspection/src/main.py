import cv2
import matplotlib.pyplot as plt


# Load the image in grayscale
image = cv2.imread("../input_images/coins.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Image not found")


# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)


# Apply Otsu Thresholding
threshold_value, binary = cv2.threshold(
    blurred,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)


# Apply Morphological Opening
kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (5, 5)
)

opened = cv2.morphologyEx(
    binary,
    cv2.MORPH_OPEN,
    kernel
)


# Apply Morphological Closing
closed = cv2.morphologyEx(
    opened,
    cv2.MORPH_CLOSE,
    kernel
)


# Detect Connected Components
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    closed,
    connectivity=8
)

print(f"Number of connected objects: {num_labels - 1}")


# Apply Euclidean Distance Transform
distance = cv2.distanceTransform(
    closed,
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
    closed,
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
    image,
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


# Save the Final Segmentation
output_path = "../output_images/final_segmentation.png"

cv2.imwrite(
    output_path,
    segmentation
)


# Display the Final Result
segmentation_rgb = cv2.cvtColor(
    segmentation,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(10, 7))
plt.imshow(segmentation_rgb)
plt.title("Final Coin Segmentation - Watershed")
plt.axis("off")
plt.show()