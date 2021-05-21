from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, UploadForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user, login_required
from werkzeug.urls import url_parse
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

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
    return render_template('index.html', title='Home', user=user, posts=posts)

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
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)    

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
    else:
        file_url = None
    return render_template('upload.html', form=form, file_url=file_url)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
