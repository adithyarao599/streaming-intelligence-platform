class BusinessRules:

    @staticmethod
    def validate_positive_metrics(dataframe, metric_columns):

        for column in metric_columns:

            if (dataframe[column] < 0).any():

                raise ValueError(f"Negative values found in {column}")

        return True

    @staticmethod
    def validate_streams(dataframe):

        if (dataframe["streams"] < 0).any():

            raise ValueError("Invalid streams")

        return True
