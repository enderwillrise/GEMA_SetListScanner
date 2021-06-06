from flask import render_template, flash, redirect, url_for, request, jsonify, make_response, session
from app import app, db
from app.forms import UploadForm, LoginForm
from app.models import User, OCROutput
from flask_login import logout_user
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import jwt
import datetime
from functools import wraps

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

def token_required(f):                      #wrapper for token auth
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if 'x-access-token' in request.headers:         #check if there is a token in the headers
           token = request.headers['x-access-token']

        if not token:                                   #if there is no token in the page
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:                                            #try to validate the token 
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])    # take the token + secret key
            current_user = db.session.query(User).filter_by(username=data['user']).first()      # identify user based on username
        except:                                                                            # unable to find user
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)   #return f(current_user, *args, **kwargs)

    return decorated


@app.route('/')

@app.route('/index')
@token_required
def index(current_user):
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

    current_user = db.session.query(User).filter_by(username=auth.username).first()

    if not current_user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm = "Login Required!"'})

    if current_user.check_password(auth.password): 
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2)}, app.config['SECRET_KEY'])
          
        return jsonify({'message': 'hello ' + current_user.username}, {'token': token})
    
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm = "Login Required!"'})   

@app.route('/upload', methods=['GET', 'POST'])
@token_required
def upload(current_user):
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
def protected(current_user):
    return jsonify({'message' : 'This is only for people with valid tokens'})
