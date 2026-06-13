class RevenueIntelligence:

    @staticmethod
    def top_revenue_content(dataframe):

        return (
            dataframe.groupby("content_name")["revenue"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
