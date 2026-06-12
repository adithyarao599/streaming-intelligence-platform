from app.core.session import SessionLocal
from app.models.silver_metadata import SilverMetadata


def save_metadata(dataset, rows, score):

    db = SessionLocal()

    try:

        metadata = SilverMetadata(
            dataset_name=dataset, row_count=rows, quality_score=score
        )

        db.add(metadata)

        db.commit()

    finally:

        db.close()
