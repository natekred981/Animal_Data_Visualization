import sqlite3
import yaml

# Load configuration
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

db_uri = config['database']['db_uri']
db_path = db_uri.split('///')[-1]  # Extract the path to the database file

# Setup database connection
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS slaughter_stats (
        id INTEGER PRIMARY KEY,
        date TEXT,
        animal_type TEXT,
        quantity INTEGER,
        year INTEGER
    )
''')

# Commit and close connection
conn.commit()
conn.close()
