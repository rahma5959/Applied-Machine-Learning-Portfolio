from PIL import Image
import os
from tqdm import tqdm

# chemins
trimap_dir = "datasets/OxfordPets/annotations/annotations/trimaps"
mask_dir = "datasets/OxfordPets/masks_binary"
list_file = "datasets/OxfordPets/annotations/annotations/list.txt"

os.makedirs(mask_dir, exist_ok=True)

# lire list.txt et récupérer les noms d'images
image_names = []
with open(list_file, "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        name = line.split()[0]  # récupère le nom de l'image
        image_names.append(name + ".png")  # ajouter l'extension

# traiter les images
for file in tqdm(image_names):
    # ignorer fichiers invisibles
    if file.startswith("._"):
        continue
    path = os.path.join(trimap_dir, file)
    if not os.path.exists(path):
        print(f"{file} not found, skipping.")
        continue
    img = Image.open(path).convert("L")
    # conversion binaire: foreground=255, background=0
    img = img.point(lambda p: 255 if p == 3 else 0)
    img.save(os.path.join(mask_dir, file))

print("All masks converted to binary successfully!")