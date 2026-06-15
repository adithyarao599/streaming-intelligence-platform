from app.core.session import SessionLocal
from app.models.dim_country import DimCountry


def seed_countries():

    db = SessionLocal()

    countries = [{"country_code": "GLOBAL", "country_name": "Global"}]

    try:

        for country in countries:

            exists = (
                db.query(DimCountry)
                .filter(DimCountry.country_code == country["country_code"])
                .first()
            )

            if not exists:
                db.add(DimCountry(**country))

        db.commit()

        print("Country dimension loaded.")

    finally:

        db.close()


if __name__ == "__main__":
    seed_countries()
