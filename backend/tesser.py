import cv2
import numpy as np
from PIL import Image
import pytesseract
import os
from app import db
from app.models import OCROutput

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    filename = np.array(Image.open(filename).convert('L'))
    filename = cv2.resize(filename, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    text = pytesseract.image_to_string(Image.fromarray(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


dir = '/Users/leejiahui/GEMA_SetListScanner/backend/uploads'
for filename in os.listdir(dir):
    fullname = os.path.join(dir, filename)
    c = ocr_core(fullname) 
    d = c.splitlines() # split string into arrays
    e = [a for a in d if a.strip()]   # remove empty spaces
    for i in e:                       # each item in array
        f = OCROutput(content = i)   # store into database
        db.session.add(f)
        db.session.commit()    