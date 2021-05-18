from app import app, db
from app.models import User, Setlist, Event, ProgrammeManager, Organiser, Interpreter, Song

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Setlist': Setlist, 'Event': Event, 'ProgrammeManager': ProgrammeManager, 'Organiser': Organiser, 'Interpreter': Interpreter, 'Song': Song}
