class FeatureStore:

    FEATURES = [
        "views",
        "streams",
        "likes",
        "shares",
        "engagement_score",
        "trend_score",
        "engagement_rate",
        "revenue_per_view",
    ]

    @classmethod
    def get_features(cls, dataframe):

        return dataframe[cls.FEATURES]
