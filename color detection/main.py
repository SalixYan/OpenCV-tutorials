import cv2
from util import get_limits
from PIL import Image
# for boundary detection

yellow = [0, 255, 255]
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera could not be opened.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        continue

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color = yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # The mask is a binary image where pixels that fall within the specified HSV color 
    # range (defined by lowerLimit and upperLimit) are set to 255 (white), and all others 
    # are set to 0 (black). This mask effectively isolates pixels based on color 
    # characteristics, making it useful for segmenting out parts of an image that match the specified color.

    mask_ = Image.fromarray(mask)
    
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    # Decide the bounding of the box.
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()