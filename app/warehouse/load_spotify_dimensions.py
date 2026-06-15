import pandas as pd

from app.core.session import SessionLocal
from app.models.dim_artist import DimArtist
from app.models.dim_content import DimContent
from app.models.dim_country import DimCountry
from app.models.dim_date import DimDate
from app.models.dim_genre import DimGenre
from app.models.dim_platform import DimPlatform


def load_dimensions():

    df = pd.read_csv("datasets/spotify.csv")

    db = SessionLocal()

    try:

        print("Loading genres...")

        genres = df["track_genre"].dropna().unique()

        for genre in genres:

            exists = db.query(DimGenre).filter(DimGenre.genre_name == genre).first()

            if not exists:

                db.add(DimGenre(genre_name=genre))

        db.commit()

        print("Genres loaded.")

        genre_map = {g.genre_name: g.genre_key for g in db.query(DimGenre).all()}

        print("Loading artists...")

        artists = df["artists"].dropna().unique()

        for artist in artists:

            artist_name = str(artist)[:255]

            artist_identifier = str(abs(hash(artist_name)))

            exists = (
                db.query(DimArtist)
                .filter(DimArtist.artist_id == artist_identifier)
                .first()
            )

            if not exists:

                db.add(
                    DimArtist(
                        artist_id=artist_identifier,
                        artist_name=artist_name,
                        country_key=1,
                    )
                )

        db.commit()

        print("Artists loaded.")

        print("Loading content...")

        for _, row in df.iterrows():

            exists = (
                db.query(DimContent)
                .filter(DimContent.content_id == row["track_id"])
                .first()
            )

            if not exists:

                genre_key = genre_map.get(row["track_genre"])

                db.add(
                    DimContent(
                        content_id=str(row["track_id"])[:100],
                        content_name=str(row["track_name"])[:255],
                        content_type="Music",
                        duration_minutes=float(row["duration_ms"]) / 60000,
                        genre_key=genre_key,
                    )
                )

        db.commit()

        print("Content loaded.")

        print("Spotify dimensions loaded successfully.")

    finally:

        db.close()


if __name__ == "__main__":
    load_dimensions()
