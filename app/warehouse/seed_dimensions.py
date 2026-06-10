from app.core.session import SessionLocal
from app.models.dim_platform import DimPlatform

PLATFORMS = ["Spotify", "Netflix", "YouTube", "MovieDB", "Music Charts"]


def seed_platforms():

    db = SessionLocal()

    try:

        for platform in PLATFORMS:

            exists = (
                db.query(DimPlatform)
                .filter(DimPlatform.platform_name == platform)
                .first()
            )

            if not exists:

                db.add(DimPlatform(platform_name=platform))

        db.commit()

    finally:

        db.close()


if __name__ == "__main__":

    seed_platforms()
