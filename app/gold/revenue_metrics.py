class RevenueMetrics:

    @staticmethod
    def calculate_rpm(dataframe):

        dataframe["rpm"] = (dataframe["revenue"] / dataframe["views"]) * 1000

        return dataframe
