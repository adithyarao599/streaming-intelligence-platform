class EngagementScore:

    @staticmethod
    def calculate(dataframe):

        dataframe["engagement_score"] = (
            dataframe["likes"] * 1 + dataframe["comments"] * 2 + dataframe["shares"] * 3
        )

        return dataframe
