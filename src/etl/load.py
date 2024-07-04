from sqlalchemy import create_engine
import pandas as pd

def load_data(df, db_uri, table_name):
    engine = create_engine(db_uri)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
