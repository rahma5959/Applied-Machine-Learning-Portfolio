import os 
import numpy as np 
import cv2

# Load the images
input_images = "input_images"
output_images = "output_images"
os.makedirs(output_images, exist_ok=True)

def preprocess_image(image_path):
    img=cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None
    #resizing
    img_resized=cv2.resize(img,(224,224))

    #conversion
    img_gray=cv2.cvtColor(img_resized,cv2.COLOR_BGR2GRAY)

    #noise reduction
    img_denoised=cv2.GaussianBlur(img_gray,(3,3),0)

    #contrast enhancement
    img_contrast=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8)).apply(img_denoised)

    return img_contrast

def main():
    for filename in os.listdir(input_images):
        if filename.lower().endswith((".jpg",".jpeg",".png")):
            input_path=os.path.join(input_images,filename)
            output_path=os.path.join(output_images,filename)
            preprocessed_image=preprocess_image(input_path)
            if preprocessed_image is not None:
                cv2.imwrite(output_path,preprocessed_image)
                print(f"Processed and saved: {output_path}")

if __name__ == "__main__":
    main()
    print("All images have been processed and saved to the output_images directory.")



    