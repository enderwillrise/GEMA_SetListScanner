from flask import render_template, flash, redirect, url_for, request, jsonify, make_response, session, Response
from app import app, db
from app.forms import UploadForm, LoginForm, EventForm, CompleteForm
from app.models import User, OCROutput, Event
from flask_login import logout_user, login_required, current_user, login_user
from werkzeug.urls import url_parse
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from tesser import ocr_core
import os
from blob import upload_blob

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

@app.route('/')

@app.route('/index')
@login_required
def index():
    user = {'username': 'user'}
    posts = [
        {
            'author': {'username': 'jia1'},
            'id' : '12345',
            'status' : 'closed',
            'body': 'setlist1'
        },
        {
            'author': {'username': 'jia'},
            'id' : '12346',
            'status' : 'processed',
            'body': 'setlist2'
        }
    ]
    return render_template('welcome.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('welcome')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/setlists', methods=['GET', 'POST'])
@login_required
def setlists():
    return render_template('setlists.html')

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
        
        dir = '/Users/leejiahui/GEMA_SetListScanner/backend/uploads/'
        for file in os.listdir(dir):
            fullname = os.path.join(dir, file)
            upload_blob("testing-upload-image-bucket", fullname , file)    
    else:
        file_url = None
    return render_template('upload.html', form=form, file_url=file_url)
    
@app.route('/event', methods=['GET', 'POST'])
@login_required
def event():
    form = EventForm()

    if form.validate_on_submit():
        event = Event(date=form.date.data, startTime=form.startTime.data, endTime=form.endTime.data, eventName=form.eventName.data,
        eventVenueName=form.eventVenueName.data, eventVenueAddress=form.eventVenueAddress.data, eventVenueCity=form.eventVenueCity.data,
        country=form.country.data)
        db.session.add(event)
        db.session.commit()

        next_page = url_for('upload')
        return redirect(next_page)
    return render_template('event.html', form=form)

@app.route('/process', methods=['GET','POST'])
def process():
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
        os.remove(fullname)

    form = CompleteForm()
    if form.validate_on_submit():
        next_page = url_for('complete')
        return redirect(next_page)
    return render_template('process.html', e=e, form=form)

@app.route('/complete')
def complete():

    return render_template('complete.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))