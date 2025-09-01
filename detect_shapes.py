def classify_shapes(img, mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    results = []
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
        cx, cy = cv2.moments(cnt)['m10']/cv2.moments(cnt)['m00'], ...
        shape = "square" if len(approx)==4 else "triangle" if len(approx)==3 else "star"
        color = img[int(cy), int(cx)]  # BGR at centroid → map to red/yellow/green
        urgency = { (0,0,255):3, (0,255,255):2, (0,255,0):1 }[tuple(color)]
        results.append({'type':shape,'urgency':urgency,'coord':(cx,cy)})
    return results
