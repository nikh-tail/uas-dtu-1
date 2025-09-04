import cv2
import numpy as np
from config import HSV_THRESHOLDS, AGE_PRIORITY, EMERGENCY_PRIORITY

def classify_color(hsv_pixel):
    for color, (low, high) in HSV_THRESHOLDS.items():
        if isinstance(low, tuple):  # skip land/ocean
         cv2.inRange(
    np.uint8([[hsv_pixel]]), 
      np.array(low),            
      np.array(high)           
    )[0][0] == 255                

                return color
    return None

def detect_casualties(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #color detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale bcz shape detection
    _, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY) #separates shapes from background
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    casualties = []

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
        x, y, w, h = cv2.boundingRect(cnt)
        center = (x + w // 2, y + h // 2)
        hsv_pixel = hsv[center[1], center[0]]
        color = classify_color(hsv_pixel)

        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            shape = "square"
        elif len(approx) > 5:
            shape = "star"
        else:
            continue

        age_score = AGE_PRIORITY.get(shape, 0)
        emergency_score = EMERGENCY_PRIORITY.get(color, 0)
        priority = age_score * emergency_score

        casualties.append({"shape": shape, "color": color, "center": center, "priority": priority})

    return casualties
