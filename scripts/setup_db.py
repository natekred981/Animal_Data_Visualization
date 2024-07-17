import sqlite3
import yaml

# Load configuration
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

db_uri = config['database']['db_uri']
db_path = db_uri.split('///')[-1]

# Setup database connection
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS slaughter_stats (
        year INTEGER PRIMARY KEY,
        less_than_one_point_four INTEGER,
        one_point_four_less_than_two_point_seven INTEGER,
        greater_than_two_point_seven INTEGER,
        total INTEGER
    )
''')

# Commit and close connection
conn.commit()
conn.close()
