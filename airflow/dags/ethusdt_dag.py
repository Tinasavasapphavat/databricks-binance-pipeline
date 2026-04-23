from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="ETHUSDT_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="0 * * * *",  
    catchup=False,
) as dag:
    
    run_extract = BashOperator(
        task_id="extract",
        bash_command="PYTHONPATH=/opt/airflow python -m pipelines.ETHUSDT.extract"
    )

    run_transform = BashOperator(
        task_id="transform",
        bash_command="PYTHONPATH=/opt/airflow python -m pipelines.ETHUSDT.transform"
    )

    run_load = BashOperator(
        task_id="load",
        bash_command="PYTHONPATH=/opt/airflow python -m pipelines.ETHUSDT.load"
    )

    run_extract >> run_transform >> run_load
