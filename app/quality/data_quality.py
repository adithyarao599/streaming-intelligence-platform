import pandas as pd


class DataQuality:

    @staticmethod
    def null_check(df):

        return df.isnull().sum()

    @staticmethod
    def duplicate_check(df):

        return df.duplicated().sum()

    @staticmethod
    def row_count(df):

        return len(df)
