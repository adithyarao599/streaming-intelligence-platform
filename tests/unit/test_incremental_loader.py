import pandas as pd

from app.warehouse.incremental_loader import IncrementalLoader


def test_incremental_load():

    dataframe = pd.DataFrame({"id": [1, 2, 3, 4]})

    result = IncrementalLoader.filter_new_records(dataframe, [1, 2], "id")

    assert len(result) == 2
