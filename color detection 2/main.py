import cv2
from util import get_limits
from PIL import Image

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

    # Change frame from rgb to hsv
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Get the limit of the color
    lowerLimit, upperLimit = get_limits(yellow)
    # Identify the color
    
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    # Create a box
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

