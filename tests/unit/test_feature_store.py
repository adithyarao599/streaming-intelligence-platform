import pandas as pd

from app.gold.feature_store import FeatureStore


def test_feature_store():

    dataframe = pd.DataFrame(
        {
            "views": [1],
            "streams": [1],
            "likes": [1],
            "shares": [1],
            "engagement_score": [1],
            "trend_score": [1],
            "engagement_rate": [1],
            "revenue_per_view": [1],
        }
    )

    result = FeatureStore.get_features(dataframe)

    assert len(result.columns) == 8
