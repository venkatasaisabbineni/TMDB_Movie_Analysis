from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def fetch_data():
    os.system("python3 src/fetch_tmdb_data.py")

def process_data():
    os.system("python3 src/process_movie_data.py")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 12, 5),
    "retries": 1,
}

dag = DAG("tmdb_pipeline", default_args=default_args)

fetch_task = PythonOperator(
    task_id="fetch_data",
    python_callable=fetch_data,
    dag=dag,
)

process_task = PythonOperator(
    task_id="process_data",
    python_callable=process_data,
    dag=dag,
)

fetch_task >> process_task
