from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator
import os

with DAG(
    dag_id='update_allogistic_dag',
    default_args={
        'retries': 5,
        'retry_delay': timedelta(minutes=5)
    },
    schedule='0 * * * *',
    start_date=datetime(2022, 10, 1),
    catchup=False
) as dag_1:

    notebook_task = PapermillOperator(
        task_id="execute_ipynb",
        input_nb= os.path.join(os.path.dirname(__file__), "allogisticompiler.ipynb"),
        output_nb= os.path.join(os.path.dirname(__file__), "out-allogisticompiler.ipynb"),
        parameters={"execution_date": "{{ execution_date }}"},
        kernel_name='python3'
    )