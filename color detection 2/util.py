import numpy as np
import cv2

def get_limits(color_bgr):
    # Convert BGR to HSV
    color_bgr_np = np.uint8([[color_bgr]])
    color_hsv = cv2.cvtColor(color_bgr_np, cv2.COLOR_BGR2HSV)[0][0]
    # Define a range around the hue, maintaining saturation and value ranges more flexible
    hue = color_hsv[0]
    saturation = color_hsv[1]
    value = color_hsv[2]

    hue_range = 10
    lower_hue = max(hue - hue_range, 0)
    upper_hue = min(hue + hue_range, 180)

    lower_sat = max(saturation - 40, 50)  # Avoid very low saturation that represents more pastel colors
    upper_sat = 255
    lower_val = max(value - 40, 50)       # Avoid very dark values
    upper_val = 255

    lower_limit = np.array([lower_hue, lower_sat, lower_val], dtype=np.uint8)
    upper_limit = np.array([upper_hue, upper_sat, upper_val], dtype=np.uint8)

    return lower_limit, upper_limit