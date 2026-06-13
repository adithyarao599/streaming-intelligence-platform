class GenreMetrics:

    @staticmethod
    def aggregate(dataframe):

        return (
            dataframe.groupby("genre")
            .agg({"views": "sum", "revenue": "sum"})
            .reset_index()
        )
