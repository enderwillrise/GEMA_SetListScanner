import pandas as pd
from app import db

engine = db.get_engine()
csv_file_path = '/Users/leejiahui/GEMA_SetlistScanner/Backend/User.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('user',
          con=engine,
          index=False,
          index_label='id',
          if_exists='replace')