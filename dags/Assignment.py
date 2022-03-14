from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from task1 import write_csv
from task2 import create_weather_table
from task3 import read_and_load_csv

default_args = {
    "owner": "Satyaprakash",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 13),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}
# setting schedule_interval="0 6 * * *" is task4 of our Assignmet
dag = DAG("Assignment", default_args=default_args, schedule_interval="0 6 * * *")

t1 = PythonOperator(task_id='Write_into_csv', python_callable=write_csv, dag=dag)

t2 = PythonOperator(task_id="create_table", python_callable=create_weather_table, dag=dag)

t3 = PythonOperator(task_id="read_csv_load_data", python_callable=read_and_load_csv, dag=dag)

t1 >> t2 >> t3
