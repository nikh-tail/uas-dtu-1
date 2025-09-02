 import cv2
import numpy as np
from config import HSV_THRESHOLDS

def segment_land_ocean(img):
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Masks for ocean and land
    ocean_mask = cv2.inRange(hsv, HSV_THRESHOLDS["ocean"][0], HSV_THRESHOLDS["ocean"][1])
    land_mask1 = cv2.inRange(hsv, HSV_THRESHOLDS["land1"][0], HSV_THRESHOLDS["land1"][1])
    land_mask2 = cv2.inRange(hsv, HSV_THRESHOLDS["land2"][0], HSV_THRESHOLDS["land2"][1])
    land_mask = cv2.bitwise_or(land_mask1, land_mask2)

    # Overlay for visualization
    overlay = np.zeros_like(img)
    overlay[ocean_mask > 0] = [255, 128, 0]  # orange for ocean
    overlay[land_mask > 0] = [0, 255, 0]     # green for land

    return ocean_mask, land_mask, overlay

