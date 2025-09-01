
from config import AGE_PRIORITY, EMERGENCY_PRIORITY

def compute_rescue_ratio(assignments, total_casualties):
    total_score = 0
    for pad_list in assignments.values():
        for c in pad_list:
            total_score += AGE_PRIORITY[c["shape"]] * EMERGENCY_PRIORITY[c["color"]]
    return round(total_score / total_casualties, 3) if total_casualties else 0
