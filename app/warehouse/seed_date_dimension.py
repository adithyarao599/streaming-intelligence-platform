from datetime import date, timedelta

from app.core.session import SessionLocal
from app.models.dim_date import DimDate


def seed_dates():

    db = SessionLocal()

    start_date = date(2020, 1, 1)
    end_date = date(2030, 12, 31)

    current = start_date

    try:

        while current <= end_date:

            date_key = int(current.strftime("%Y%m%d"))

            exists = db.query(DimDate).filter(DimDate.date_key == date_key).first()

            if not exists:

                db.add(
                    DimDate(
                        date_key=date_key,
                        full_date=current,
                        day=current.day,
                        month=current.month,
                        quarter=((current.month - 1) // 3) + 1,
                        year=current.year,
                        week=current.isocalendar()[1],
                    )
                )

            current += timedelta(days=1)

        db.commit()

        print("Date dimension loaded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_dates()
