class WarehouseValidator:

    @staticmethod
    def validate_row_counts(source_rows, loaded_rows):

        return source_rows == loaded_rows
