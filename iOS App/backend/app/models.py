from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy_utils import CountryType, Country
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Setlist', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Setlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    status = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Setlist {}>'.format(self.id)

class Event(db.Model):           
     id = db.Column(db.Integer, primary_key=True)
     date = db.Column(db.Date, default=datetime.utcnow)
     startTime = db.Column(db.Time)
     endTime = db.Column(db.Time)
     eventName = db.Column(db.String(100))
     eventVenueName = db.Column(db.String(100))
     eventVenueAddress = db.Column(db.String(100))
     eventVenueOrt = db.Column(db.String(100))
     
     def __repr__(self):
        return '<Event {}>'.format(self.eventName)

class ProgrammeManager(db.Model,Base):
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(20))
    firstName = db.Column(db.String(20))
    country = db.Column(CountryType)

    def __repr__(self):
        return '<Manager {}>'.format(self.firstName)

class Organiser(db.Model,Base):
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(20))
    firstName = db.Column(db.String(20))
    ort = db.Column(db.String(20))
    country = db.Column(CountryType)

    def __repr__(self):
        return '<Organiser {}>'.format(self.firstName)

class Interpreter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    performanceType = db.Column(db.Enum('Sole band/ensemble','Several equal bands/artists','Opening act','Main act','DJ live act', 'Stage/theatre performance'))
    interpreterName = db.Column(db.String(50))

    def __repr__(self):
        return '<Interpreter {}>'.format(self.interpreterName)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    oneComposer = db.Column('yes',db.Boolean(), nullable=True)

    def __repr__(self):
        return '<Song {}>'.format(self.title)

