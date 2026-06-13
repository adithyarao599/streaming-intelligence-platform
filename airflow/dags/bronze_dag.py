from datetime import datetime

from airflow.operators.python import PythonOperator

from airflow import DAG
from app.bronze.bronze_loader import run_spotify_ingestion

with DAG(
    dag_id="bronze_layer",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    bronze_task = PythonOperator(
        task_id="spotify_ingestion", python_callable=run_spotify_ingestion
    )
