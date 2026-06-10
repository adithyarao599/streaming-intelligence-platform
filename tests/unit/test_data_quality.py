from app.quality.data_quality import DataQuality


def test_row_count(sample_dataframe):

    assert DataQuality.row_count(sample_dataframe) == 3
