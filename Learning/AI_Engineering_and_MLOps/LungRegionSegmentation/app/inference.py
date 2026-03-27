import cv2
import numpy as np

def predict_overlay(file):
    # Convert file to grayscale image
    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    original = img.copy()  # garder l'original

    # --- Preprocessing ---
    img = cv2.resize(img, (256, 256))
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.equalizeHist(img)

    # --- Segmentation ---
    _, mask = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # --- Morphology ---
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # --- Overlay ---
    original = cv2.resize(original, (256, 256))
    mask_colored = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    overlay = cv2.addWeighted(cv2.cvtColor(original, cv2.COLOR_GRAY2BGR), 0.7, mask_colored, 0.3, 0)

    return overlay