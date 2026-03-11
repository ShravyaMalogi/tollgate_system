from ultralytics import YOLO
import pytesseract
import cv2
import re

# load YOLO license plate detector
model = YOLO("best.pt")

def number_plate_detection(img):

    results = model(img)

    for r in results:
        boxes = r.boxes.xyxy

        for box in boxes:
            x1, y1, x2, y2 = map(int, box)

            plate = img[y1:y2, x1:x2]

            text = pytesseract.image_to_string(plate, config="--psm 7")

            text = "".join(re.split("[^a-zA-Z0-9]*", text))
            text = text.strip().upper()

            return text

    return None
