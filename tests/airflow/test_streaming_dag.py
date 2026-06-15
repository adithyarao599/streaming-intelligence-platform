from pathlib import Path

from airflow.models import DagBag


def test_streaming_dag():
    dag_folder = str(Path(__file__).resolve().parents[2] / "dags")

    dagbag = DagBag(
        dag_folder=dag_folder,
        include_examples=False,
    )

    assert len(dagbag.import_errors) == 0
    assert "streaming_platform" in dagbag.dags
