from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

def create_files_task():
    subprocess.run(['python', 'create_files.py'])

def count_a_task():
    subprocess.run(['python', 'count_a_parallel.py'])

def sum_results_task():
    subprocess.run(['python', 'sum_results.py'])

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 5),
    'retries': 1,
}

with DAG('text_file_processing', default_args=default_args, schedule_interval='@once') as dag:
    create_files = PythonOperator(
        task_id='create_files',
        python_callable=create_files_task,
    )

    count_a = PythonOperator(
        task_id='count_a',
        python_callable=count_a_task,
    )

    sum_results = PythonOperator(
        task_id='sum_results',
        python_callable=sum_results_task,
    )

    create_files >> count_a >> sum_results
