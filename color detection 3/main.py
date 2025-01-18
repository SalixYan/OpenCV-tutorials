import cv2
from util import get_limits
from PIL import Image
import numpy as np

def nothing(x):
    pass

# Create a window for the trackbars
cv2.namedWindow("Trackbars")
cv2.createTrackbar("LowH", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("HighH", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("LowS", "Trackbars", 50, 255, nothing)
cv2.createTrackbar("HighS", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("LowV", "Trackbars", 50, 255, nothing)
cv2.createTrackbar("HighV", "Trackbars", 255, 255, nothing)

cap = cv2.VideoCapture(0)
yellow = [0, 255, 255]

if not cap.isOpened():
    print("Error: Camera could not be opened.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        continue

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(yellow)

    # Override limits with trackbar positions
    lowerLimit = np.array([cv2.getTrackbarPos("LowH", "Trackbars"),
                           cv2.getTrackbarPos("LowS", "Trackbars"),
                           cv2.getTrackbarPos("LowV", "Trackbars")])
    upperLimit = np.array([cv2.getTrackbarPos("HighH", "Trackbars"),
                           cv2.getTrackbarPos("HighS", "Trackbars"),
                           cv2.getTrackbarPos("HighV", "Trackbars")])

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    bbox = Image.fromarray(mask).getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
