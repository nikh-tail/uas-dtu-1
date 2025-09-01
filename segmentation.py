import cv2
import numpy as np
from config import HSV_THRESHOLDS

def segment_land_ocean(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ocean_mask = cv2.inRange(hsv, *HSV_THRESHOLDS["ocean"])
    land_mask1 = cv2.inRange(hsv, *HSV_THRESHOLDS["land1"])
    land_mask2 = cv2.inRange(hsv, *HSV_THRESHOLDS["land2"])
    land_mask = cv2.bitwise_or(land_mask1, land_mask2)

    # Overlay masks
    overlay = img.copy()
    overlay[ocean_mask > 0] = [255, 128, 0]  # orange
    overlay[land_mask > 0] = [0, 255, 0]     # green

    return ocean_mask, land_mask, overlay
