from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_arguments = {
    'owner': 'lk',
    'schedule_interval': '@once'

}

with DAG('airflow_dag', default_args = default_arguments):
    task = BashOperator(
        task_id = 'hello_task',
        bash_command = 'echo "Hello World Dag!"'
    )