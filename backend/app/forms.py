from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.core import DateField, TimeField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, IMAGES

photos = UploadSet('photos', IMAGES)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('No file selected')])
    submit = SubmitField('Upload')

class EventForm(FlaskForm):
     date = DateField('Date (YYYY-MM-DD)') 
     startTime = TimeField('Start Time (HH:MM)')
     endTime = TimeField('End Time (HH:MM)')
     eventName = StringField('Event Name')
     eventVenueName = StringField('Venue Name')
     eventVenueAddress = StringField('Venue Address')
     eventVenueCity = StringField('City')
     country = StringField('Country')
     submit = SubmitField('Next')

class ProcessForm(FlaskForm):
    submit = SubmitField('Process')
    
class CompleteForm(FlaskForm):
    submit = SubmitField('Complete')