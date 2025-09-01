
This project simulates a  Rescue mission using Python and OpenCV. The goal is to process aerial images, identify casualties and rescue pads, segment terrain into land and ocean, and assign victims to the most suitable pads based on urgency and proximity.  
---

 1. `config.py` — Your Control Center

This file holds all the adjustable settings for the pipeline:
- HSV color ranges for detecting land and ocean
- Rescue pad capacities based on color
- Priority values for different casualty shapes and emergency levels
- Scoring weights used in assignment and rescue ratio calculations

2. `segmentation.py` — Separating Land from Ocean

This module uses HSV color filtering to figure out which parts of the image are land and which are ocean:
- It creates binary masks for both terrain types
- Combines them into a visual overlay so you can see the segmentation
- Helps downstream modules ignore irrelevant regions (like casualties floating in the ocean)

---

3. `assignment.py` — Matching Casualties to Rescue Pads

This module handles the logic of who gets rescued and where they go:
- It calculates the distance between each casualty and each pad
- Scores each possible pairing based on urgency and proximity
- Assigns casualties to pads using a greedy approach, while respecting pad capacities

📐 **How scoring works**:
```python
score = age_priority × emergency_priority
utility = score - (distance / max_distance)

