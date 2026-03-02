import os 
import cv2
import numpy as np

# Load the images
input_images = "input_images"
output_images = "output_images"
target_size = (224, 224)

if not os.path.exists(output_images):
    os.makedirs(output_images)

def preprocess_image(image_path):
    img=cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None
    #resizing
    h,w=img.shape[:2]
    scale=min(target_size[0]/w,target_size[1]/h)
    new_w,new_h=int(w*scale),int(h*scale)
    img_resized=cv2.resize(img,(int(w*scale),int(h*scale)))

    #padding
    pad_w= target_size[0]-new_w
    pad_h= target_size[1]-new_h
    top,bottom=pad_h//2,pad_h-pad_h//2
    left,right=pad_w//2,pad_w-pad_w//2
    img_padded=cv2.copyMakeBorder(img_resized,top,bottom,left,right,cv2.BORDER_CONSTANT,value=[0,0,0])

    #conversion 
    img_gray=cv2.cvtColor(img_padded,cv2.COLOR_BGR2GRAY)

    #normalization
    img_normalized=img_gray/255.0

    #noise reduction
    img_denoised=cv2.GaussianBlur(img_normalized,(3,3),0)

    #the preprocessed image
    img_out=(img_denoised*255).astype(np.uint8)
    return img_out

for filename in os.listdir(input_images):
    if filename.lower().endswith((".jpg",".jpeg",".png")):
        input_path=os.path.join(input_images,filename)
        output_path=os.path.join(output_images,filename)
        preprocessed_image=preprocess_image(input_path)
        if preprocessed_image is not None:
            cv2.imwrite(output_path,preprocessed_image)
            print(f"Processed and saved: {output_path}")

print("All images have been processed and saved to the output_images directory.")