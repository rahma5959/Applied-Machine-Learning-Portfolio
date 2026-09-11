# dataset_loader_expert.py

"""
OxfordPets Dataset Loader - Expert Preprocessing

This dataset loader includes:
- Image & mask loading
- Advanced data augmentation
- Elastic deformation
- Normalization
- Binary mask enforcement
"""

# =========================
# 1. IMPORT LIBRARIES
# =========================

import os                      # handle file paths
import random                  # random operations for augmentation
import numpy as np            # numerical operations (arrays, noise)
from PIL import Image, ImageFilter   # image loading and filtering
from torch.utils.data import Dataset  # PyTorch dataset class
import torchvision.transforms as T    # transformations (tensor, normalize, etc.)
import torch
import matplotlib.pyplot as plt       # visualization
from scipy.ndimage import gaussian_filter, map_coordinates  # elastic transform


# =========================
# 2. ELASTIC TRANSFORMATION
# =========================

def elastic_transform(image, mask, alpha=1, sigma=10):
    """
    Apply elastic deformation to image and mask.

    Why?
    - Simulates natural deformation (very useful in segmentation, especially medical)
    """

    # Generate random displacement field
    random_state = np.random.RandomState(None)

    # Get image shape (height, width)
    shape = np.array(image.size[::-1])

    # Create smooth random displacement (dx, dy)
    dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma) * alpha
    dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma) * alpha

    # Create coordinate grid
    x, y = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))

    # Apply displacement
    indices = np.reshape(y + dy, (-1, 1)), np.reshape(x + dx, (-1, 1))

    # Convert image and mask to numpy
    img_np = np.array(image)
    mask_np = np.array(mask)

    # Apply transformation
    img_transformed = map_coordinates(img_np, indices, order=1).reshape(shape[0], shape[1], 3)
    mask_transformed = map_coordinates(mask_np, indices, order=0).reshape(shape[0], shape[1])

    # Convert back to PIL
    return Image.fromarray(img_transformed.astype(np.uint8)), Image.fromarray(mask_transformed.astype(np.uint8))


# =========================
# 3. DATASET CLASS
# =========================

class OxfordPetsDatasetExpert(Dataset):
    def __init__(self, txt_file, images_dir, masks_dir, img_size=(256,256), augment=False):

        # Store parameters
        self.images_dir = images_dir
        self.masks_dir = masks_dir
        self.img_size = img_size
        self.augment = augment

        # =========================
        # Load image names
        # =========================
        self.image_names = []
        with open(txt_file, "r") as f:
            for line in f:
                line = line.strip()

                # Skip comments or empty lines
                if line.startswith("#") or line == "":
                    continue

                # Extract image name
                self.image_names.append(line.split()[0] + ".png")

        # =========================
        # Define transformations
        # =========================

        # Color augmentation (only for image)
        self.color_jitter = T.ColorJitter(
            brightness=0.3,
            contrast=0.3,
            saturation=0.3,
            hue=0.05
        )

        # Convert image to tensor
        self.to_tensor = T.ToTensor()

        # Normalize image (ImageNet stats)
        self.normalize = T.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )


    def __len__(self):
        return len(self.image_names)


    def __getitem__(self, idx):

        # =========================
        # 1. Load image & mask
        # =========================
        img_name = self.image_names[idx]

        img_path = os.path.join(self.images_dir, img_name)
        mask_path = os.path.join(self.masks_dir, img_name)

        img = Image.open(img_path).convert("RGB")   # color image
        mask = Image.open(mask_path).convert("L")   # grayscale mask


        # =========================
        # 2. Resize
        # =========================
        img = img.resize(self.img_size)

        # IMPORTANT: NEAREST keeps mask labels intact
        mask = mask.resize(self.img_size, resample=Image.NEAREST)


        # =========================
        # 3. Data augmentation
        # =========================
        if self.augment:

            # ---- Flip ----
            if random.random() > 0.5:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
                mask = mask.transpose(Image.FLIP_LEFT_RIGHT)

            if random.random() > 0.5:
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
                mask = mask.transpose(Image.FLIP_TOP_BOTTOM)

            # ---- Rotation ----
            angle = random.uniform(-30, 30)
            img = img.rotate(angle)
            mask = mask.rotate(angle, resample=Image.NEAREST)

            # ---- Scaling ----
            scale = random.uniform(0.8, 1.2)
            new_size = (int(self.img_size[0]*scale), int(self.img_size[1]*scale))

            img = img.resize(new_size)
            mask = mask.resize(new_size, resample=Image.NEAREST)

            # Crop back to original size
            left = (new_size[0] - self.img_size[0]) // 2
            top = (new_size[1] - self.img_size[1]) // 2

            img = img.crop((left, top, left+self.img_size[0], top+self.img_size[1]))
            mask = mask.crop((left, top, left+self.img_size[0], top+self.img_size[1]))

            # ---- Color jitter (only image) ----
            img = self.color_jitter(img)

            # ---- Blur ----
            if random.random() > 0.5:
                img = img.filter(ImageFilter.GaussianBlur(radius=1.0))

            # ---- Noise ----
            if random.random() > 0.5:
                img_np = np.array(img)
                noise = np.random.normal(0, 5, img_np.shape)
                img_np = np.clip(img_np + noise, 0, 255).astype(np.uint8)
                img = Image.fromarray(img_np)

            # ---- Elastic deformation ----
            if random.random() > 0.5:
                img, mask = elastic_transform(img, mask)


        # =========================
        # 4. Convert to tensor
        # =========================
        img = self.to_tensor(img)
        mask = self.to_tensor(mask)


        # =========================
        # 5. Normalize image
        # =========================
        img = self.normalize(img)


        # =========================
        # 6. Ensure binary mask
        # =========================
        mask = (mask > 0.5).float()


        return img, mask


# =========================
# 4. TEST THE DATASET
# =========================

if __name__ == "__main__":

    dataset = OxfordPetsDatasetExpert(
        txt_file="datasets/OxfordPets/annotations/annotations/trainval.txt",
        images_dir="datasets/OxfordPets/images/images",
        masks_dir="datasets/OxfordPets/masks_binary",
        augment=True
    )

    print("Dataset size:", len(dataset))

    # Visualize samples
    for i in range(2):
        img, mask = dataset[i]

        img_show = img.permute(1,2,0)

        plt.subplot(1,2,1)
        plt.imshow((img_show - img_show.min())/(img_show.max()-img_show.min()))
        plt.title("Image")

        plt.subplot(1,2,2)
        plt.imshow(mask[0], cmap='gray')
        plt.title("Mask")

        plt.show()