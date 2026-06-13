class ContentMetrics:

    @staticmethod
    def aggregate(dataframe):

        return (
            dataframe.groupby("content_name")
            .agg({"views": "sum", "revenue": "sum", "engagement_score": "mean"})
            .reset_index()
        )
