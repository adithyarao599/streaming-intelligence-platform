import pytest


@pytest.fixture
def sample_dataframe():

    import pandas as pd

    return pd.DataFrame({"id": [1, 2, 3], "name": ["A", "B", "C"]})
