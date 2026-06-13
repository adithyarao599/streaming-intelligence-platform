class CohortAnalytics:

    @staticmethod
    def monthly_cohort(dataframe):

        dataframe["cohort_month"] = dataframe["release_date"].dt.to_period("M")

        return dataframe
