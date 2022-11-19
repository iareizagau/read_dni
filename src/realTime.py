import cv2
import pytesseract
from pytesseract import Output
import easyocr

# Captura de video
cap = cv2.VideoCapture(0)


# cap.set(3,1280)
# cap.set(4,720)

def tesserac_data(img):
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    print(f"image2data {d.keys()}")


def tesseract_boxes(img):
    h, w, c = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    cv2.imshow("ID BOXES", img)


def easy_ocr(img):
    reader = easyocr.Reader(lang_list=['es'], gpu=False)
    result = reader.readtext(img, paragraph="False")

    font = cv2.FONT_HERSHEY_SIMPLEX

    spacer = 100
    for detection in result:
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        img = cv2.putText(img, text, (20, spacer), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        spacer += 15
        print(text)
    cv2.imshow("ID easy_ocr", img)


while True:
    ret, frame = cap.read()
    if ret:
        # tesserac_data(frame)
        # tesseract_boxes(frame)
        easy_ocr(frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
