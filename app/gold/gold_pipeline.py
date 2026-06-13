from app.gold.engagement_score import EngagementScore
from app.gold.feature_engineering import FeatureEngineering
from app.gold.trend_score import TrendScore


class GoldPipeline:

    def process(self, dataframe):

        dataframe = EngagementScore.calculate(dataframe)

        dataframe = TrendScore.calculate(dataframe)

        dataframe = FeatureEngineering.create_features(dataframe)

        return dataframe
