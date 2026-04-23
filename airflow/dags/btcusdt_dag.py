from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import pendulum

with DAG(
    dag_id="BTCUSDT_pipeline",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule="0 * * * *",  
    catchup=False,
) as dag:
    
    run_extract = BashOperator(
        task_id="extract",
        bash_command="PYTHONPATH=/opt/airflow python -m pipelines.BTCUSDT.extract"
    )

    run_transform = BashOperator(
        task_id="transform",
        bash_command="PYTHONPATH=/opt/airflow python -m pipelines.BTCUSDT.transform"
    )

    run_load = BashOperator(
        task_id="load",
        bash_command="PYTHONPATH=/opt/airflow python -m pipelines.BTCUSDT.load"
    )

    run_extract >> run_transform >> run_load
