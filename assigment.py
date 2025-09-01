import numpy as np
from config import PAD_CAPACITY, AGE_PRIORITY, EMERGENCY_PRIORITY
def assign_casualties(casualties, pads):
    assignments = {pad["color"]: [] for pad in pads}
    capacities = PAD_CAPACITY.copy()
