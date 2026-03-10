import cv2
import pytesseract
import numpy as np
from PIL import Image
import re


def number_plate_detection(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5),0)

    edges = cv2.Canny(blur,100,200)

    contours,_ = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours,key=cv2.contourArea,reverse=True)[:10]

    plate = None

    for cnt in contours:

        x,y,w,h = cv2.boundingRect(cnt)

        ratio = w/h

        if 2 < ratio < 6:

            plate = img[y:y+h,x:x+w]
            break

    if plate is None:
        return None

    text = pytesseract.image_to_string(plate)

    text = "".join(re.split("[^a-zA-Z0-9]*", text))

    text = text.strip().upper()

    return text
