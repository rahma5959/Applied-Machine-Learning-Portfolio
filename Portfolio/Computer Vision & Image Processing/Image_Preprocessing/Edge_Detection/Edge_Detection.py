import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image=cv2.imread("image.jpg")
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#apply sobel edge detection
sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
sobel_magnitude = np.sqrt(sobelx**2 + sobely**2)
sobel_magnitude = np.uint8(sobel_magnitude)


# Apply Canny edge detection
edges=cv2.Canny(gray,100,200)

#visualisation 

plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.title("Original Image")
plt.imshow(gray,cmap='gray')

plt.subplot(1,3,2)
plt.title("Sobel Edges")
plt.imshow(sobel_magnitude,cmap='gray')


plt.subplot(1,3,3)
plt.title("Canny Edges")
plt.imshow(edges,cmap='gray')

plt.tight_layout()
plt.savefig("result.png", dpi=300)
plt.show()