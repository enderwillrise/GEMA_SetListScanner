from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app import app
from app.forms import UploadForm
from app.models import User
from flask_login import logout_user
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import jwt
import datetime
from functools import wraps

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(*args, **kwargs)   #return f(current_user, *args, **kwargs)

    return decorated

@app.route('/')

@app.route('/index')
@token_required
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
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm = "Login Required!"'})

    user = User.query.filter_by(username=auth.username).first()

    if not user:
            return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm = "Login Required!"'})

    if user.check_password(auth.password): 
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2)}, app.config['SECRET_KEY'])
        
        return jsonify({'message': 'hello ' + user.username}, {'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm = "Login Required!"'})

@app.route('/upload', methods=['GET', 'POST'])
@token_required
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

@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this!'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'This is only for people with valid tokens'})
