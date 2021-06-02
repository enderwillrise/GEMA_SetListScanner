from app import app, db
from app.models import User, Setlist, Event, ProgrammeManager, Organiser, Interpreter, Song
from flask_uploads import configure_uploads, patch_request_class

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Setlist': Setlist, 'Event': Event, 'ProgrammeManager': ProgrammeManager, 'Organiser': Organiser, 'Interpreter': Interpreter, 'Song': Song, 'Photo': Photo, 'OCROutput': OCROutput}

configure_uploads(app, photos)
patch_request_class(app)

if __name__ == '__main__': 
    app.run(debug = True)