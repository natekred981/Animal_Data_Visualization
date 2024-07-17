import yaml
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.etl.extract import extract
from src.etl.transform import transform
from src.etl.load import load_data

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract
df = extract(config['file_paths']['raw_data'])

# Transform
df = transform(df)

# Load
load_data(df, config['database']['db_uri'], 'slaughter_stats')
