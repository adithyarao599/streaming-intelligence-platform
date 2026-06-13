class ArtistMetrics:

    @staticmethod
    def aggregate(dataframe):

        return (
            dataframe.groupby("artist_name")
            .agg({"views": "sum", "revenue": "sum", "streams": "sum"})
            .reset_index()
        )
