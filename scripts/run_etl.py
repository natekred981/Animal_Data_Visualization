import yaml
from src.etl.extract import extract_data
#from src.etl.transform import transform_data
from src.etl.load import load_data

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract
df = extract_data(config['file_paths']['raw_data'])

# Transform
#df = transform_data(df)

# Load
load_data(df, config['database']['db_uri'], 'slaughter_stats')
