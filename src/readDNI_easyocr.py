import os
import cv2
import easyocr
from matplotlib import pyplot as plt
import numpy as np

# IMAGE_PATH = './DNI_ImanolAreizaga_B.jpeg'
IMAGE_PATH = 'https://www.somewebsite.com/chinese_tra.jpg'

reader = easyocr.Reader(lang_list=['ch_tra', 'en'], gpu=False)
result = reader.readtext(IMAGE_PATH, paragraph="False")

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(IMAGE_PATH)
spacer = 100
for detection in result:
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
    img = cv2.putText(img, text, (20, spacer), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
    spacer += 15
plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.show()
