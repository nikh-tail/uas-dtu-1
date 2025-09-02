# Priority mappings
AGE_PRIORITY = {"star": 3, "triangle": 2, "square": 1}
EMERGENCY_PRIORITY = {"red": 3, "yellow": 2, "green": 1}

#example_sample
casualties = [
    {"shape": "star", "color": "red", "center": (100, 150)},
    {"shape": "triangle", "color": "yellow", "center": (200, 120)},
    {"shape": "square", "color": "green", "center": (300, 180)},
]

# Calculation of priority
for i, c in enumerate(casualties):
    age_score = AGE_PRIORITY.get(c["shape"], 0)
    emergency_score = EMERGENCY_PRIORITY.get(c["color"], 0)
    priority = age_score * emergency_score
    print(f"Casualty {i+1}: Shape = {c['shape']}, Color = {c['color']}, Priority Score = {priority}")
