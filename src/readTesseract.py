import cv2
import pytesseract
from pytesseract import Output

IMAGE_PATH = './DNI_ImanolAreizaga_A.jpeg'

img = cv2.imread(IMAGE_PATH)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)
print(f"text {text}")

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(f"image2data {d.keys()}")

h, w = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
