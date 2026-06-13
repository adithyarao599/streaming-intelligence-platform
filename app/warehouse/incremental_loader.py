class IncrementalLoader:

    @staticmethod
    def filter_new_records(dataframe, loaded_ids, key_column):

        return dataframe[~dataframe[key_column].isin(loaded_ids)]
