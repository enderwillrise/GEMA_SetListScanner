from flask import Flask
from ocr import ocr_core

from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = jsonify(ocr_core('/Users/abdullahtayyab/Desktop/GEMA_SetListScanner/iOSApp/fronted/SetListScannerFrontend/test2.jpeg'))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run()
