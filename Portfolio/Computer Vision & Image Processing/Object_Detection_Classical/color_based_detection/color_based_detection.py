import cv2
import os
import numpy as np
import skimage.color as color

#load images
input_images = "input_images"
output_images = "output_images"
os.makedirs(output_images, exist_ok=True)


lower_color = np.array([0, 100, 100])
upper_color = np.array([10, 255, 255])


lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])
def detect_color_objects(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image at {image_path}")
        return

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create a mask for red color
    mask1=cv2.inRange(hsv, lower_color, upper_color)
    mask2=cv2.inRange(hsv, lower_red2, upper_red2)
    mask=cv2.bitwise_or(mask1,mask2)

    #remove noise
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #draw bounding boxes
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filter small contours
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return img

def main():
    for filename in os.listdir(input_images):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_images, filename)
            output_path = os.path.join(output_images, filename)
            result_img = detect_color_objects(input_path)
            if result_img is not None:
                cv2.imwrite(output_path, result_img)
                print(f"Processed and saved: {output_path}")

if __name__ == "__main__":
    main()
    print("All images have been processed and saved to the output_images directory.")