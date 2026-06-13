import json


def generate_reconciliation(source_rows, loaded_rows):

    report = {
        "source_rows": source_rows,
        "loaded_rows": loaded_rows,
        "difference": source_rows - loaded_rows,
    }

    with open("reports/warehouse/" "reconciliation.json", "w") as file:

        json.dump(report, file, indent=4)
