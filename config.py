
IMAGE_DIR = "input_images"
OUTPUT_DIR = "output"

PAD_CAPACITY = {"pink": 3, "blue": 4, "grey": 2}
AGE_PRIORITY = {"star": 3, "triangle": 2, "square": 1}
EMERGENCY_PRIORITY = {"red": 3, "yellow": 2, "green": 1}

HSV_THRESHOLDS = {
    "ocean": ((90, 50, 50), (130, 255, 255)),
    "land1": ((20, 40, 40), (35, 255, 255)),
    "land2": ((36, 40, 40), (85, 255, 255)),
    "red1": ((0, 80, 70), (10, 255, 255)),
    "red2": ((170, 80, 70), (180, 255, 255)),
    "yellow": ((20, 80, 80), (35, 255, 255)),
    "green": ((36, 80, 60), (85, 255, 255)),
    "pink": ((140, 80, 80), (170, 255, 255)),
    "blue": ((90, 80, 80), (130, 255, 255)),
    "grey": ((0, 0, 50), (180, 50, 255)),
}

