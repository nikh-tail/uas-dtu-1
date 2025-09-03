 import numpy as np
from config import PAD_CAPACITY

def assign_casualties(casualties, pads):
    assignments = {pad["color"]: [] for pad in pads}
    capacities = PAD_CAPACITY.copy()

    for c in sorted(casualties, key=lambda x: x["priority"], reverse=True):
        best_pad = None
        best_dist = float("inf")
        for p in pads:
            if capacities[p["color"]] > 0:
                dist = np.linalg.norm(np.array(c["center"]) - np.array(p["center"]))
                if dist < best_dist:
                    best_dist = dist
                    best_pad = p
        if best_pad:
            assignments[best_pad["color"]].append(c)
            capacities[best_pad["color"]] -= 1
    return assignments
