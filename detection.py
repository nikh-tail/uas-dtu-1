import cv2
import numpy as np

def detect(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    casualties = []
    pads = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 100: continue

        approx = cv2.approxPolyDP(cnt, 0.03 * cv2.arcLength(cnt, True), True)
        center = tuple(cnt[cnt[:, :, 1].argmin()][0])  # topmost point

        if len(approx) > 8:
            pads.append(center)
        else:
            casualties.append(center)

    return casualties, pads
