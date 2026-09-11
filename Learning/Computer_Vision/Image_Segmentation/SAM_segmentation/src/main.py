
print("=== MAIN.PY STARTED ===")
import torch
print("Torch imported")
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from transformers import Sam2Processor, Sam2Model

print("Imports completed")
# ============================================================
# 1. Load the image
# ============================================================

image = Image.open("input_images/cars.jpg").convert("RGB")

print("Image loaded successfully")


# ============================================================
# 2. Load SAM 2
# ============================================================

model_name = "facebook/sam2.1-hiera-large"

processor = Sam2Processor.from_pretrained(
    model_name
)

model = Sam2Model.from_pretrained(
    model_name
)

model.eval()

print("SAM 2 loaded successfully")


# ============================================================
# 3. Define the point prompt
# ============================================================

# Point located on the object we want to segment
input_points = [[[250, 300]]]

# 1 = positive point
# We tell SAM that this point belongs to the object
input_labels = [[1]]


# ============================================================
# 4. Prepare the inputs for SAM
# ============================================================

inputs = processor(
    images=image,
    input_points=input_points,
    input_labels=input_labels,
    return_tensors="pt"
)


# ============================================================
# 5. Run SAM
# ============================================================

with torch.no_grad():

    outputs = model(**inputs)


# ============================================================
# 6. Post-process the predicted mask
# ============================================================

masks = processor.post_process_masks(
    outputs.pred_masks.cpu(),
    inputs["original_sizes"].cpu(),
    inputs["reshaped_input_sizes"].cpu()
)


# Get the first mask
mask = masks[0][0][0].numpy()


# Convert the mask to binary
mask = mask > 0


print("Mask generated successfully")


# ============================================================
# 7. Create the segmentation result
# ============================================================

image_array = np.array(image)

segmentation = image_array.copy()

# Keep only the pixels selected by SAM
segmentation[~mask] = 0


# ============================================================
# 8. Save the result
# ============================================================

output_path = "../output_images/final_segmentation.png"

Image.fromarray(segmentation).save(
    output_path
)

print("Segmentation saved to:", output_path)


# ============================================================
# 9. Display the result
# ============================================================

plt.figure(figsize=(10, 7))

plt.imshow(segmentation)

plt.scatter(
    input_points[0][0][0],
    input_points[0][0][1],
    color="red",
    marker="*",
    s=150
)

plt.title("SAM 2 - Point Prompt Segmentation")

plt.axis("off")

plt.show()

