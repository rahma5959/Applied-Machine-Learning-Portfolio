import os 
import cv2
import numpy as np
from skimage.feature import local_binary_pattern
import pickle

# Load the images
input_images = "input_images"
output_images = "output_images"
os.makedirs(output_images, exist_ok=True)

radius=1
n_points=8*radius

def extract_lbp_features(image_path):
    img=cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None
    
    # Convert to grayscale
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Extract LBP features
    lbp=local_binary_pattern(gray,n_points,radius,method="uniform")

    # Convert LBP to histogram
    n_bins=int(lbp.max()+1)
    lbp_hist,_=np.histogram(lbp.ravel(),bins=n_bins,range=(0,n_bins),density=True)

    hist=lbp_hist.astype(np.float32)
    hist /= (hist.sum() + 1e-6)  # Normalize histogram
    
    return hist

def main():
    feature_dict={}  # To save all features

    for filename in os.listdir(input_images):
        if filename.lower().endswith((".jpg",".jpeg",".png")):
            input_path=os.path.join(input_images,filename)
            features=extract_lbp_features(input_path)
            if features is not None:
                feature_dict[filename]=features
                print(f"Extracted LBP features for {filename} → length: {len(features)}")

    # Save feature dictionary to a file
    with open(os.path.join(output_images,"lbp_features.pkl"),"wb") as f:
        pickle.dump(feature_dict,f)
        print(f"\n All features saved to {os.path.join(output_images,'lbp_features.pkl')}")

if __name__=="__main__":
    main()