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
$   pip install babel
$   pip install sqlalchemy-utils       //for country field
$   pip install pandas                 //for db mass upload from csv to db
$   pip install flask-uploads
$   pip install flask-jwt

## 3. Import a flask and run test
>>>> import flask
$   export FLASK_APP=backend1.py
$   flask run

## 4. Flask configurations
$   FLASK_APP = backend1.py
$   FLASK_ENV = development

## 5. Create database
$   flask db init
$   flask db migrate -m "update description e.g. users table"
$   flask db upgrade

## 6(a). Upload mock User.csv
Update filepath in massdb.py code "csv_file_path = '_/Users/leejiahui/GEMA_SetlistScanner/Backend/User.csv_'"
$   python massdb.py
$   flask db migrate -m "update db or any description"
$   flask db upgrade  #try "flask db stamp head" before upgrade if error

>>> users = User.query.all()
>>> for u in users:
...     u.set.password('haha')
...
>>> db.session.add(u)
>>> db.session.commit()

## 6(b). (Alternative) Create new user - CLI method
$   flask shell
>>> u = User(username='john', email='john@example.com')       //add new user
>>> u.set_password('haha')
>>> db.session.add(u)
>>> db.session.commit()

## 8. Imports before running Python / Flask Shell (If needed)
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

## 11. If creating upload function
- Create a folder "uploads" under ./backend 
- Create ocr script based on Abdullah's instructions
- Instead of print(ocr_core(file)), use this loop:
        dir = '/Users/leejiahui/GEMA_SetListScanner/backend/uploads'
        for filename in os.listdir(dir):
                fullname = os.path.join(dir, filename)
                print(ocr_core(fullname))

### 12. Init Google Cloud (For uploading picture)
$   gcloud init

## 13. Set google app credentials
$   export GOOGLE_APPLICATION_CREDENTIALS="/Users/leejiahui/desktop/Projects/ssa-poc-194d-1ae027d7536d.json"

# Quick access
## Git commands
git status
git add -name-
git commit -m "description"
git push

# Troubleshooting errors
! from app import db
! from: can't read /var/mail/app
        $ python // go into python mode first

! $ flask shell 
! NameError: name 'User' is not defined
name of folder "loginpage" should not be same as name of python file "loginpage1", flask shell will not know which to recognise

check tables in db
        for t in db.metadata.tables.items():
                print(t)

! "sqlalchemy_utils" is not defined
in migrations > mako
        import sqlalchemy_utils

! unexpected argument length = 255 for ChoiceType
in migrations > env.py, paste this:

        Sole_band_ensemble = u'1'
        Several_equal_bands_artists = u'2'
        Opening_act = u'3'
        Main_act = u'4'
        DJ_live_act = u'5'
        Stage_theatre_performance = u'6'

        perfType = [
                (u'Sole_band_ensemble', u'Sole band/ensemble'),
                (u'Several_equal_bands_artists', u'Several equal bands/artists'),
                (u'Opening_act', u'Opening act'),
                (u'Main_act', u'Main act'),
                (u'DJ_live_act', u'DJ live act'),
                (u'Stage_theatre_performance', u'Stage/theatre performance')
        ]

        def upgrade()
        ...

! table Event already exists 
go to models.py > copy and delete the entire "event" model
        db migrate -m "delete event" 
        db upgrade
add back event model again after upgrade