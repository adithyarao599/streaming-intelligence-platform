class FeatureEngineering:

    @staticmethod
    def create_features(dataframe):

        dataframe["engagement_rate"] = (
            dataframe["engagement_score"] / dataframe["views"]
        )

        dataframe["revenue_per_view"] = dataframe["revenue"] / dataframe["views"]

        return dataframe
