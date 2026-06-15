from app.ingestion.spotify_ingestor import SpotifyIngestor


def test_spotify_ingestor():

    ingestor = SpotifyIngestor("datasets/spotify.csv")

    df = ingestor.extract()

    print(df.head())

    print(f"Rows: {len(df)}")

    assert len(df) > 0


if __name__ == "__main__":
    test_spotify_ingestor()
