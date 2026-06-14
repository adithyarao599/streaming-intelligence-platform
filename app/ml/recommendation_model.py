class RecommendationModel:

    @staticmethod
    def recommend(dataframe, top_n=10):

        return dataframe.sort_values("recommendation_score", ascending=False).head(
            top_n
        )
