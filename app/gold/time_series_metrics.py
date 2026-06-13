class TimeSeriesMetrics:

    @staticmethod
    def daily_views(dataframe):

        return dataframe.groupby("date")["views"].sum().reset_index()
