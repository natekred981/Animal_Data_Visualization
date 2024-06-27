import pandas as pd
import sqlite3

# Load CSV into pandas DataFrame
df = pd.read_csv('animal_slaughter_statistics.csv')

# Connect to SQLite database (or create it)
conn = sqlite3.connect('animal_slaughter.db')

# Save DataFrame to SQLite database
df.to_sql('slaughter_stats', conn, if_exists='replace', index=False)