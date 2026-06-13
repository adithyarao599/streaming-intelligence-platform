import pandas as pd

from app.gold.engagement_score import EngagementScore


def test_engagement_score():

    dataframe = pd.DataFrame({"likes": [10], "comments": [5], "shares": [2]})

    result = EngagementScore.calculate(dataframe)

    assert result["engagement_score"][0] == 26
