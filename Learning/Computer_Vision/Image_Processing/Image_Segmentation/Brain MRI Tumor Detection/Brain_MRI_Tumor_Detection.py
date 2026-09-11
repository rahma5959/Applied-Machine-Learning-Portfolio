import os 
import cv2
import numpy as np

# Load the images
input_images = "input_images"
output_images = "output_images"
os.makedirs(output_images, exist_ok=True)

def segment_tumor(image_path):
    img=cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None
    # Convert to grayscale
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Denoise
    img_denoised=cv2.GaussianBlur(gray,(5,5),0)

    # Thresholding (Otsu)
    _,thresh=cv2.threshold(img_denoised,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Morphological opening to remove small noise
    kernel=np.ones((3,3),np.uint8)
    opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

    #distance transform
    dist=cv2.distanceTransform(opening,cv2.DIST_L2,5)
    _,sure_fg=cv2.threshold(dist,0.4*dist.max(),255,0)
    sure_fg=np.uint8(sure_fg)
    sure_bg=cv2.dilate(opening,kernel,iterations=3)
    unknown=cv2.subtract(sure_bg,sure_fg)

    # Watershed
    _,markers=cv2.connectedComponents(sure_fg)
    markers=markers+1
    markers[unknown==255]=0
    markers=cv2.watershed(img,markers)

    tumor_count=0
    necrotic_total = 0
    output=img.copy()

    for marker_id in np.unique(markers):
        if marker_id<=1:
            continue

        tumor_mask=np.zeros(gray.shape,dtype=np.uint8)
        tumor_mask[markers==marker_id]=255
        contours,_=cv2.findContours(tumor_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            tumor_count+=1
            cv2.drawContours(output,contours,-1,(0,255,0),2)
            tumor_region=cv2.bitwise_and(img,img,mask=tumor_mask)
            
            _,necrotic_mask=cv2.threshold(cv2.cvtColor(tumor_region,cv2.COLOR_BGR2GRAY),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            
            kernel=np.ones((3,3),np.uint8)
            clean_tumor=cv2.morphologyEx(necrotic_mask,cv2.MORPH_OPEN,kernel,iterations=2)

            contours_necrotic,_=cv2.findContours(clean_tumor,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours_necrotic:
                area=cv2.contourArea(cnt)
                if area>100:
                    cv2.drawContours(output,[cnt],-1,(0,0,255),2)
                    necrotic_total+=1
    print(f"Tumors detected: {tumor_count}")
    print(f"Necrotic spots detected: {necrotic_total}")

    return output

if __name__ == "__main__":
    for filename in os.listdir(input_images):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path=os.path.join(input_images,filename)
            result=segment_tumor(img_path)
            if result is not None:
                cv2.imwrite(os.path.join(output_images,"segmented_"+filename),result)
    print("All images processed and saved in", output_images)
        