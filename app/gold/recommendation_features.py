class RecommendationFeatures:

    @staticmethod
    def build(dataframe):

        dataframe["recommendation_score"] = (
            dataframe["engagement_score"] * 0.6 + dataframe["trend_score"] * 0.4
        )

        return dataframe
