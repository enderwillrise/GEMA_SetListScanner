from werkzeug.security import generate_password_hash
import pandas as pd
from app.models import User
from app import db
from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)

# Import CSV
data = pd.read_csv (r'/Users/leejiahui/loginpage/User.csv')   

# Convert to data frame
df = pd.DataFrame(data, columns= ['id','username','email'])

# Convert df to sql and connect to db
df.to_sql('User', con=db.engine, if_exists='append',index=False)  #if_exists can be 'append' or 'replace' depending on situation
engine.execute("SELECT * FROM User").fetchall()
