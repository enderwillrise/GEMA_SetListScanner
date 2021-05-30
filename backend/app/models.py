from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy_utils import CountryType, Country
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    setlists = db.relationship('Setlists', backref='author', lazy='dynamic')
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def init_db():
        db.create_all()

class Setlist(db.Model):
    __tablename__ = 'setlist'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    status = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

    def __repr__(self):
        return '<Setlist {}>'.format(self.id)

class Event(db.Model, Base): 
     __tablename__ = 'event'          
     id = db.Column(db.Integer, primary_key=True)
     date = db.Column(db.Date, default=datetime.utcnow)
     startTime = db.Column(db.Time)
     endTime = db.Column(db.Time)
     eventName = db.Column(db.String(100))
     eventVenueName = db.Column(db.String(100))
     eventVenueAddress = db.Column(db.String(100))
     eventVenueCity = db.Column(db.String(100))
     country = db.Column(CountryType)
     setlist = db.relationship('Setlist', backref='linked_event', lazy='dynamic')

     def __repr__(self):
        return '<Event {}>'.format(self.eventName)

class ProgrammeManager(db.Model):
    __tablename__ = 'manager'
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(20))
    firstName = db.Column(db.String(20))


    def __repr__(self):
        return '<Manager {}>'.format(self.firstName)

class Organiser(db.Model, Base):
    __tablename__ = 'organiser'
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(20))
    firstName = db.Column(db.String(20))
    city = db.Column(db.String(20))
    country = db.Column(CountryType)

    def __repr__(self):
        return '<Organiser {}>'.format(self.firstName)

class Interpreter(db.Model, Base):
    perfType = [
        (u'Sole-band-ensemble', u'Sole band/ensemble'),
        (u'Several-equal-bands-artists', u'Several equal bands/artists'),
        (u'Opening-act', u'Opening act'),
        (u'Main-act', u'Main act'),
        (u'DJ-live-act', u'DJ live act'),
        (u'Stage-theatre-performance', u'Stage/theatre performance')
    ]
    __tablename__ = 'interpreter'
    id = db.Column(db.Integer, primary_key=True)
    performanceType = db.Column(ChoiceType(perfType))
    interpreterName = db.Column(db.String(50))

    def __repr__(self):
        return '<Interpreter {}>'.format(self.interpreterName)

class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    oneComposer = db.Column('yes',db.Boolean(), nullable=True)

    def __repr__(self):
        return '<Song {}>'.format(self.title)

