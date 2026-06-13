class TrendIntelligence:

    @staticmethod
    def top_trending(dataframe):

        return dataframe.sort_values("trend_score", ascending=False)
