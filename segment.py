import cv2, numpy as np
def segment_ocean_land(img_path):
    img = cv2.imread(img_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue, upper_blue = np.array([90, 50, 50]), np.array([130, 255, 255])
    lower_land, upper_land = np.array([15, 40, 40]), np.array([85, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_land = cv2.inRange(hsv, lower_land, upper_land) 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)
    mask_land = cv2.morphologyEx(mask_land, cv2.MORPH_CLOSE, kernel)
    overlay = img.copy()
    overlay[mask_blue > 0] = (200, 200, 255)   # light-blue
    overlay[mask_land > 0] = (200, 180, 150)   # light-brown
    return overlay, mask_blue, mask_land
