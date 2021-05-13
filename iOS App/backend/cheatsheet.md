# Cheatsheet

## Install packages
$   pip install flask
$   pip install python-dotenv
$   pip install flask-wtf
$   pip install flask-sqlalchemy
$   pip install flask-migrate
$   pip install flask-login
$   pip install babel
$   pip install sqlalchemy-utils

## Run virtual environment
$   python3 -m venv venv               // *only run this once!*
$   source venv/bin/activate            // *activate venv*

## Import a flask and run test
>>>> import flask
$   export FLASK_APP=loginpage.py
$   flask run

## Flask configurations
$   FLASK_APP = loginpage.py
$   FLASK_ENV = development

## Create database
$   flask db init
$   flask db migrate -m "users table"
$   flask db upgrade

## Install sqlalchemy-utils for database
$   git clone git://github.com/kvesteri/sqlalchemy-utils.git
$   cd sqlalchemy-utils
$   pip install -e .

## Create new user
$   flask shell
>>> u = User(username='john', email='john@example.com')       // add new user
>>> u.set_password('pass1')
>>> db.session.add(u)

>>> for u in users:                 //delete all users in one go
        db.session.delete(u)

>>> db.session.commit()

## Imports before running Python / Flask Shell
>>> from loginpage import app
>>> from app.models import User, Post

# Git commands
git status
git add -name-
git commit -m "description"
git push

# Troubleshooting errors
from app import db
from: can't read /var/mail/app
> $ python // go into python mode first

$ flask shell 
NameError: name 'User' is not defined
> name of folder "loginpage" should not be same as name of python file "loginpage1", flask shell will not know which to recognise
