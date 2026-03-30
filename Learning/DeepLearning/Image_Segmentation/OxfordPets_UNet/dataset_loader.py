# dataset_loader.py
"""
OxfordPets Dataset Loader for Image Segmentation (UNet)

- Reads image names from trainval.txt or test.txt
- Loads images and corresponding binary masks
- Optional data augmentation (flip, rotation)
- Resizes images and masks
- Converts images and masks to PyTorch tensors
"""

import os
import random
from PIL import Image
from torch.utils.data import Dataset
import torchvision.transforms as T
import torch

class OxfordPetsDataset(Dataset):
    def __init__(self, txt_file, images_dir, masks_dir, img_size=(256,256), augment=False):
        self.images_dir = images_dir
        self.masks_dir = masks_dir
        self.img_size = img_size
        self.augment = augment

        # Read image names
        self.image_names = []
        with open(txt_file, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("#") or line == "":
                    continue
                # store base name without extension
                self.image_names.append(line.split()[0])

    def __len__(self):
        return len(self.image_names)

    def __getitem__(self, idx):
        img_name = self.image_names[idx]
        img_path = os.path.join(self.images_dir, img_name + ".jpg")
        mask_path = os.path.join(self.masks_dir, img_name + ".png")

        # ignore hidden files
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"{img_path} not found.")
        if not os.path.exists(mask_path):
            raise FileNotFoundError(f"{mask_path} not found.")

        img = Image.open(img_path).convert("RGB")
        mask = Image.open(mask_path).convert("L")

        # Resize
        img = img.resize(self.img_size)
        mask = mask.resize(self.img_size, resample=Image.NEAREST)

        # Data augmentation
        if self.augment:
            if random.random() > 0.5:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
                mask = mask.transpose(Image.FLIP_LEFT_RIGHT)
            angle = random.uniform(-15,15)
            img = img.rotate(angle)
            mask = mask.rotate(angle, resample=Image.NEAREST)

        # Convert to tensor
        img = T.ToTensor()(img)
        mask = T.ToTensor()(mask)
        mask = (mask > 0.5).float()  # binary mask

        return img, mask

if __name__=="__main__":
    print("Testing dataset loader...")

    # train/val
    train_dataset = OxfordPetsDataset(
        txt_file="datasets/OxfordPets/annotations/annotations/trainval.txt",
        images_dir="datasets/OxfordPets/images/images",
        masks_dir="datasets/OxfordPets/masks_binary",
        img_size=(256,256),
        augment=True
    )

    # test
    test_dataset = OxfordPetsDataset(
        txt_file="datasets/OxfordPets/annotations/annotations/test.txt",
        images_dir="datasets/OxfordPets/images/images",
        masks_dir="datasets/OxfordPets/masks_binary",
        img_size=(256,256),
        augment=False
    )

    print("Train/Val dataset size:", len(train_dataset))
    print("Test dataset size:", len(test_dataset))

    # Visualize one sample
    import matplotlib.pyplot as plt
    img, mask = train_dataset[0]
    img_show = img.permute(1,2,0)  # [H,W,C] for plt

    plt.subplot(1,2,1)
    plt.title("Image")
    plt.imshow(img_show)
    plt.subplot(1,2,2)
    plt.title("Mask")
    plt.imshow(mask[0], cmap="gray")
    plt.show()