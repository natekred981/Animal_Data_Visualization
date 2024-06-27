# from airflow import DAG
# from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime, timedelta
# from google.cloud import bigquery
# import pandas as pd

# # Define default arguments
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2024, 5, 2),
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# # Define DAG
# dag = DAG(
#     dag_id='chicken_death_analysis',
#     default_args=default_args,
#     description='An Airflow DAG to analyze chicken death data',
#     schedule_interval='@daily',
# )

# # Function to process CSV data
# def process_csv_data():
#     # Read CSV data from Cloud Storage
#     gcs_uri = 'gs://animals-round2/animal_viz/data/yearly_slaughter_weight.xlsx'
#     df = pd.read_excel(gcs_uri)
    
#     # Perform data processing (e.g., cleaning, transformation)
#     # For demonstration purposes, we'll just print the dataframe
#     print(df.head())

# # Task to process CSV data
# process_data_task = PythonOperator(
#     task_id='process_data',
#     python_callable=process_csv_data,
#     dag=dag,
# )

# # Task to load data into BigQuery
# load_to_bq_task = GoogleCloudStorageToBigQueryOperator(
#     task_id='load_to_bq',
#     bucket='animals-round2',  # Your Cloud Storage bucket name
#     source_objects=['animal_viz/data/yearly_slaughter_weight.xlsx'],  # Path to your file in Cloud Storage
#     destination_project_dataset_table='healthy-earth-421818.chicken_annual.slaughter-data',  # BigQuery table where data will be loaded
#     schema_fields=[{'name': 'weight', 'type': 'DOUBLE'}, {'name': 'number_of_chickens', 'type': 'INTEGER'}],  # Schema of your data
#     write_disposition='WRITE_TRUNCATE',  # Option to truncate the table before writing data
#     skip_leading_rows=1,  # Optional: Skip the first row if it contains headers
#     dag=dag,
# )


# # Define task dependencies
# process_data_task >> load_to_bq_task
