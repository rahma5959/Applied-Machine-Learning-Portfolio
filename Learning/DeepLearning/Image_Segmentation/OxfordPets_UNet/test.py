# test.py
"""
Test script for UNet on OxfordPets segmentation dataset

- Loads the trained UNet model
- Loads test dataset using dataset_loader.py
- Evaluates Dice score on test set
- Visualizes some predictions
"""

import torch
from torch.utils.data import DataLoader
from dataset_loader import OxfordPetsDataset
from model_unet import UNet
import matplotlib.pyplot as plt
import os

# -------------------- PARAMETERS --------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
batch_size = 8
img_size = (256, 256)
test_txt = "datasets/OxfordPets/annotations/annotations/test.txt"
images_dir = "datasets/OxfordPets/images/images"
masks_dir = "datasets/OxfordPets/masks_binary"
model_path = "OxfordPets_UNet_unet.pth"

# -------------------- LOAD TEST DATA --------------------
test_dataset = OxfordPetsDataset(test_txt, images_dir, masks_dir, img_size, augment=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# -------------------- LOAD MODEL --------------------
model = UNet(in_channels=3, out_channels=1).to(device)
model.load_state_dict(torch.load(model_path, map_location=device))
model.eval()

# -------------------- EVALUATION --------------------
dice_score = 0
with torch.no_grad():
    for imgs, masks in test_loader:
        imgs, masks = imgs.to(device), masks.to(device)
        outputs = torch.sigmoid(model(imgs))
        outputs = (outputs > 0.5).float()
        dice_score += (2*(outputs*masks).sum()) / (outputs.sum() + masks.sum())

dice_score /= len(test_loader)
print(f"Test Dice Score: {dice_score:.4f}")

# -------------------- VISUALIZATION --------------------
imgs, masks = next(iter(test_loader))
imgs, masks = imgs.to(device), masks.to(device)
with torch.no_grad():
    preds = torch.sigmoid(model(imgs))
    preds = (preds > 0.5).float()

# Show first 3 predictions
for i in range(3):
    img = imgs[i].permute(1,2,0).cpu()
    mask = masks[i][0].cpu()
    pred = preds[i][0].cpu()

    plt.figure(figsize=(10,3))
    plt.subplot(1,3,1)
    plt.title("Image")
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(1,3,2)
    plt.title("Ground Truth")
    plt.imshow(mask)
    plt.axis('off')

    plt.subplot(1,3,3)
    plt.title("Prediction")
    plt.imshow(pred)
    plt.axis('off')

    plt.show()