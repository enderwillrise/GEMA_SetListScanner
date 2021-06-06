try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('/Users/abdullahtayyab/Desktop/GEMA_SetListScanner/iOSApp/fronted/SetListScannerFrontend/test2.jpeg'))


''' 
# additional codes for data cleaning / processing

dir = '/Users/leejiahui/GEMA_SetListScanner/backend/uploads' # specify directory to retrieve file

for filename in os.listdir(dir):
    fullname = os.path.join(dir, filename)  # configure filepath
    c = ocr_core(fullname)                  # OCR processing
    d = c.splitlines() # split string into arrays
    e = [a for a in d if a.strip()]   # remove empty spaces
    
    for i in e:                       # each item in array
        f = OCROutput(content = i)   # store into database
        db.session.add(f)
        db.session.commit()     '''