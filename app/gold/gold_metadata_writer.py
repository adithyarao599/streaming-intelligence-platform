from app.core.session import SessionLocal
from app.models.gold_metadata import GoldMetadata


def save_gold_metadata(dataset, rows, quality):

    db = SessionLocal()

    try:

        db.add(
            GoldMetadata(dataset_name=dataset, row_count=rows, quality_score=quality)
        )

        db.commit()

    finally:

        db.close()
