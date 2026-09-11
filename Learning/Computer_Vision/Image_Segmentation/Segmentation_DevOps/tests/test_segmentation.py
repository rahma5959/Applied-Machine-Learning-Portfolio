import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.segmentation import segment_image


def test_segmentation_creates_mask():
    # Define input and output paths
    input_path = "input_images/pomme.jpg"
    output_path = "output_images/test_mask.png"

    # Run the segmentation
    segment_image(input_path, output_path)

    # Check that the mask was created
    assert os.path.exists(output_path)

    # Check that the mask is not empty
    assert os.path.getsize(output_path) > 0

def test_mask_is_not_empty():
    # Define input and output paths
    input_path = "input_images/pomme.jpg"
    output_path = "output_images/test_mask_2.png"

    # Run the segmentation
    segment_image(input_path, output_path)

    # Read the generated mask
    import cv2

    mask = cv2.imread(output_path, cv2.IMREAD_GRAYSCALE)

    # Check that the mask was successfully read
    assert mask is not None

    # Check that the mask contains pixels
    assert mask.size > 0