from datetime import datetime

from airflow.operators.empty import EmptyOperator

from airflow import DAG

default_args = {"retries": 3}


with DAG(
    dag_id="streaming_platform",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    start = EmptyOperator(task_id="start")

    bronze = EmptyOperator(task_id="bronze")

    silver = EmptyOperator(task_id="silver")

    gold = EmptyOperator(task_id="gold")

    warehouse = EmptyOperator(task_id="warehouse")

    end = EmptyOperator(task_id="end")

    start >> bronze

    bronze >> silver

    silver >> gold

    gold >> warehouse

    warehouse >> end
