class TrendScore:

    @staticmethod
    def calculate(dataframe):

        dataframe["trend_score"] = (
            dataframe["views"] * 0.40
            + dataframe["likes"] * 0.30
            + dataframe["shares"] * 0.30
        )

        return dataframe
