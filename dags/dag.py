from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('animal_slaughter_etl', default_args=default_args, schedule_interval='@daily')

def extract():
    df = extract_data('data/raw/yearly_slaughter_weight.csv')
    return df

# def transform(df):
#     df = transform_data(df)
#     return df

def load(df):
    load_data(df, 'sqlite:///data/processed/animal_slaughter_stats.db', 'slaughter_stats')

extract_task = PythonOperator(task_id='extract', python_callable=extract, dag=dag)
# transform_task = PythonOperator(task_id='transform', python_callable=transform, dag=dag)
load_task = PythonOperator(task_id='load', python_callable=load, dag=dag)

extract_task  >> load_task
