class CountryMetrics:

    @staticmethod
    def aggregate(dataframe):

        return (
            dataframe.groupby("country")
            .agg({"views": "sum", "revenue": "sum"})
            .reset_index()
        )
