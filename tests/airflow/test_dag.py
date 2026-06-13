from airflow.models import DagBag


def test_dag_loaded():

    dagbag = DagBag()

    assert dagbag.get_dag("streaming_platform") is not None
