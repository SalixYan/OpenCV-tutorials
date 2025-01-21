import cv2
import easyocr
import matplotlib.pyplot as plt
img1 = cv2.imread('p1.jpg')
print(img1)

threshold = 0.25
# instance text detector
reader = easyocr.Reader(['en'], gpu = False)
# detect text on image
text_ = reader.readtext(img1)
# draw bbox and text
for t in text_:
    print(t)

    bbox, text, score = t
    if score > threshold:
        cv2.rectangle(img1, bbox[0], bbox[2], (0, 255, 0),5)
        cv2.putText(img1, text, bbox[0], cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 0, 0),2)

plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.show()