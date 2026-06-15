from decimal import Decimal

import pandas as pd

from app.core.session import SessionLocal
from app.models.dim_artist import DimArtist
from app.models.dim_content import DimContent
from app.models.dim_country import DimCountry
from app.models.dim_date import DimDate
from app.models.dim_genre import DimGenre
from app.models.dim_platform import DimPlatform
from app.models.fact_content_performance import FactContentPerformance


def load_facts():

    print("Reading Spotify dataset...")

    df = pd.read_csv("datasets/spotify.csv")

    db = SessionLocal()

    try:

        print("Building lookup maps...")

        artist_map = {
            artist.artist_name: artist.artist_key
            for artist in db.query(DimArtist).all()
        }

        genre_map = {
            genre.genre_name: genre.genre_key for genre in db.query(DimGenre).all()
        }

        content_map = {
            content.content_id: content.content_key
            for content in db.query(DimContent).all()
        }

        spotify_platform = (
            db.query(DimPlatform).filter(DimPlatform.platform_name == "Spotify").first()
        )

        global_country = (
            db.query(DimCountry).filter(DimCountry.country_code == "GLOBAL").first()
        )

        default_date = db.query(DimDate).order_by(DimDate.date_key).first()

        platform_key = spotify_platform.platform_key
        country_key = global_country.country_key
        date_key = default_date.date_key

        print("Loading facts...")

        batch = []

        for _, row in df.iterrows():

            popularity = int(row["popularity"])

            batch.append(
                FactContentPerformance(
                    date_key=date_key,
                    content_key=content_map.get(str(row["track_id"])),
                    artist_key=artist_map.get(str(row["artists"])),
                    genre_key=genre_map.get(str(row["track_genre"])),
                    platform_key=platform_key,
                    country_key=country_key,
                    views=popularity * 1500,
                    streams=popularity * 1000,
                    likes=popularity * 100,
                    comments=popularity * 10,
                    shares=popularity * 5,
                    watch_hours=float(row["duration_ms"]) / 3600000,
                    revenue=Decimal(str(round(popularity * 0.05, 2))),
                    trend_score=float(popularity),
                )
            )

            if len(batch) >= 5000:

                db.bulk_save_objects(batch)
                db.commit()

                print(f"Loaded {len(batch)} records...")

                batch = []

        if batch:

            db.bulk_save_objects(batch)
            db.commit()

        print("Fact table loaded successfully.")

    finally:

        db.close()


if __name__ == "__main__":
    load_facts()
