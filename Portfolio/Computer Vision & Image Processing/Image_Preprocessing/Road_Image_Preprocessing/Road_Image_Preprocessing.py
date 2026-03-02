import os 
import cv2
import numpy as np

# Load the images

input_images = "input_images"
output_images = "output_images"
os.makedirs(output_images, exist_ok=True)

def preprocess_image(image_path):
    img=cv2.imread(image_path)

    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img_denoised=cv2.GaussianBlur(img_gray,(3,3),0)

    img_conrast=cv2.equalizeHist(img_denoised)

    height,width=img_conrast.shape

    roi = img_conrast[int(height * 0.5):height, 0:width]

    output=(roi*255.0).astype(np.uint8)
    return output

for filename in os.listdir(input_images):
    if filename.lower().endswith((".jpg",".jpeg",".png")):
        input_path=os.path.join(input_images,filename)
        output_path=os.path.join(output_images,filename)
        preprocessed_image=preprocess_image(input_path)
        if preprocessed_image is not None:
            cv2.imwrite(output_path,preprocessed_image)
            print(f"Processed and saved: {output_path}")

print("All images have been processed and saved to the output_images directory.")