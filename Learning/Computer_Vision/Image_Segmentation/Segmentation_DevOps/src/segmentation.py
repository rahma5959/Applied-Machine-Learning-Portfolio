
import cv2
import numpy as np


def segment_image(input_path, output_path):
    # Read the input image
    image = cv2.imread(input_path)

    if image is None:
        raise FileNotFoundError(f"Image not found: {input_path}")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu thresholding
    threshold, mask = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Save the segmentation mask
    cv2.imwrite(output_path, mask)

    # Create a copy of the original image
    result = image.copy()

    # Create a colored overlay from the mask
    overlay = np.zeros_like(image)
    overlay[:, :, 2] = mask

    # Blend the original image with the overlay
    result = cv2.addWeighted(
        result,
        0.7,
        overlay,
        0.3,
        0
    )

    # Define the result path
    result_path = output_path.replace(
        "mask.png",
        "segmentation_result.png"
    )

    # Save the segmentation result
    cv2.imwrite(result_path, result)

    # Return the Otsu threshold
    return threshold

