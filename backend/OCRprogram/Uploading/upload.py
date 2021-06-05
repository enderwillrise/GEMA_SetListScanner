import os
from flask import Flask, flash, request, redirect, url_for ,  render_template
from ocr import ocr_core
from flask import jsonify
from werkzeug.utils import secure_filename, xhtml

UPLOAD_FOLDER = '/Users/abdullahtayyab/Documents/GEMA_SetListScanner/backend/OCRprogram/Uploading'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

'''def home():
    return render_template('index.html')'''

def allowed_file(filename):
    global x
    x = filename
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', name=filename))
    return render_template('index.html')
    '''<!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <h1>Welcome to the HomePage!</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/my-link/')

def my_link():
    response = jsonify(ocr_core(os.path.join('/Users/abdullahtayyab/Documents/GEMA_SetListScanner/backend/OCRprogram/Uploading/', x)))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    '''print ('I got clicked!')
    return x'''

if __name__ == '__main__':
    app.run()



'''def my_link():
  print ('I got clicked!')
  return 'Click.'''