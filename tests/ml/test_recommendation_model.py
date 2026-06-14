import pandas as pd

from app.ml.recommendation_model import RecommendationModel


def test_recommendations():

    dataframe = pd.DataFrame({"recommendation_score": [10, 50, 30]})

    result = RecommendationModel.recommend(dataframe, top_n=1)

    assert result.iloc[0]["recommendation_score"] == 50
