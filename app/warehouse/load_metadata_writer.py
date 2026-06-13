from app.core.session import SessionLocal
from app.models.warehouse_load_metadata import WarehouseLoadMetadata


def save_load_metadata(table_name, records, status):

    db = SessionLocal()

    try:

        db.add(
            WarehouseLoadMetadata(
                table_name=table_name, records_loaded=records, status=status
            )
        )

        db.commit()

    finally:

        db.close()
