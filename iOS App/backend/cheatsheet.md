# Cheatsheet

# Quick set-up
## 1. Run virtual environment
$   python3 -m venv venv               #*only run this once!*
$   source venv/bin/activate           #*activate venv*

## 2. Install packages
$   pip install flask
$   pip install python-dotenv
$   pip install flask-wtf
$   pip install flask-sqlalchemy
$   pip install flask-migrate
$   pip install flask-login
! $   pip install babel
! $   pip install sqlalchemy-utils       //for country field
$   pip install pandas                 //for db mass upload from csv to db

## 3. Import a flask and run test
>>>> import flask
$   export FLASK_APP=loginpage.py
$   flask run

## 4. Flask configurations
$   FLASK_APP = loginpage.py
$   FLASK_ENV = development

## 5. Create database
$   flask db init
$   flask db migrate -m "update description e.g. users table"
$   flask db upgrade

! ## 6. Install sqlalchemy-utils for database
$   git clone git://github.com/kvesteri/sqlalchemy-utils.git
$   cd sqlalchemy-utils
$   pip install -e .

## 7(a). Upload mock User.csv
Update file name in code "data = pd.read_csv (r'_/Users/leejiahui/loginpage/User.csv_')"
$   python massdb.py

## 7(b). (Alternative) Create new user - CLI method
$   flask shell
>>> u = User(username='john', email='john@example.com')       //add new user
>>> u.set_password('haha')
>>> db.session.add(u)
>>> db.session.commit()

## 8. Imports before running Python / Flask Shell
>>> from loginpage import app
>>> from app.models import User, Setlist, ... _(Include the classes you need)_
>>> from app import db

## 9. Verify users created in db
>>> users = User.query.all()
>>> for u in users:
...     print(u.id,u.username,u.email)

>>> for u in users:                 //delete all users in one go
...     db.session.delete(u)

>>> db.session.commit()            //commit changes before exiting

## 10. Run flask
$   flask run
_mock user: user1, password: haha_

# Quick access
## Git commands
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

check tables in db
for t in db.metadata.tables.items():
        print(t)