class ExecutiveKPIs:

    @staticmethod
    def generate(dataframe):

        return {
            "total_views": dataframe["views"].sum(),
            "total_revenue": dataframe["revenue"].sum(),
            "total_streams": dataframe["streams"].sum(),
            "avg_engagement": dataframe["engagement_score"].mean(),
        }
