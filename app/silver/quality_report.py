import json


def create_report(dataset, row_count, score):

    report = {"dataset": dataset, "rows": row_count, "quality_score": score}

    with open(f"reports/silver/" f"{dataset}_quality.json", "w") as file:

        json.dump(report, file, indent=4)
