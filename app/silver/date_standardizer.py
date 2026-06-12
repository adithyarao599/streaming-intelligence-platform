import pandas as pd


class DateStandardizer:

    @staticmethod
    def standardize(dataframe, column):

        dataframe[column] = pd.to_datetime(dataframe[column], errors="coerce")

        return dataframe
