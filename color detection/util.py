# An "util file" or "utility file" in software development generally refers to a module 
# or file that contains utility functions or classes which are helpful across various 
# parts of an application or across multiple projects. 
# These utilities are typically generic, designed to perform common tasks that are not 
# specific to any single feature or business logic of an application. 

# designed to convert a specific color from the BGR (Blue, Green, Red) color space to 
# the HSV (Hue, Saturation, Value) color space and create a range around this color. 
# This range is typically used for color detection or filtering within an image.
import numpy as np
import cv2
def get_limits(color):
    # e.g., color = [255, 0, 0] 
    # Strong blue, no green or red
    c = np.uint8([[color]])
    # Insert the bgr values which you want to convert to hsv.
    # Create a numpy array to represent this color as a single pixel
    # Shape will be (1, 1, 3)
    # [[[120 255 255]]]

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    lowerLimit = hsvC[0][0][0] - 5, 100, 100
    upperLimit = hsvC[0][0][0] + 5, 255, 255
    # The goal of setting these limits is to define a range of colors that are considered "similar" to 
    # a target color for the purpose of filtering an image. 
    # The hsvC[0][0][0] fetches the hue component of the converted color from BGR to HSV.

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit