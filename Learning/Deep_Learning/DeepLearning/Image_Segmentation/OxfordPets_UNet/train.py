# train.py
"""
Training script for UNet on OxfordPets segmentation dataset

- Loads train/validation datasets using dataset_loader.py
- Defines UNet model
- Uses BCEWithLogitsLoss for binary segmentation
- Saves best model based on validation Dice score
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from dataset_loader import OxfordPetsDataset
from unet_model import UNet
from tqdm import tqdm
import os

# -------------------- PARAMETERS --------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
num_epochs = 20
batch_size = 8
learning_rate = 1e-4
img_size = (256, 256)

train_txt = "datasets/OxfordPets/annotations/annotations/trainval.txt"
images_dir = "datasets/OxfordPets/images/images"
masks_dir = "datasets/OxfordPets/masks_binary"
save_model_path = "OxfordPets_UNet_unet.pth"

# -------------------- DATASET AND DATALOADER --------------------
train_dataset = OxfordPetsDataset(train_txt, images_dir, masks_dir, img_size, augment=True)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

val_dataset = OxfordPetsDataset(train_txt, images_dir, masks_dir, img_size, augment=False)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# -------------------- MODEL, LOSS, OPTIMIZER --------------------
model = UNet(in_channels=3, out_channels=1).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# -------------------- TRAINING LOOP --------------------
best_val_dice = 0

for epoch in range(num_epochs):
    model.train()
    train_loss = 0
    for imgs, masks in tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs} - Training"):
        imgs, masks = imgs.to(device), masks.to(device)
        optimizer.zero_grad()
        outputs = model(imgs)
        loss = criterion(outputs, masks)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    train_loss /= len(train_loader)

    # -------------------- VALIDATION --------------------
    model.eval()
    val_dice = 0
    with torch.no_grad():
        for imgs, masks in val_loader:
            imgs, masks = imgs.to(device), masks.to(device)
            outputs = torch.sigmoid(model(imgs))
            outputs = (outputs > 0.5).float()
            val_dice += (2*(outputs*masks).sum()) / (outputs.sum() + masks.sum())
    val_dice /= len(val_loader)

    print(f"Epoch {epoch+1}: Train Loss={train_loss:.4f}, Val Dice={val_dice:.4f}")

    # Save best model
    if val_dice > best_val_dice:
        best_val_dice = val_dice
        torch.save(model.state_dict(), save_model_path)
        print(f"Saved best model with Dice={best_val_dice:.4f}")

print("Training complete!")