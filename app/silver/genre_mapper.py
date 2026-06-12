class GenreMapper:

    GENRE_MAPPING = {
        "hip hop": "HIP_HOP",
        "hip-hop": "HIP_HOP",
        "hiphop": "HIP_HOP",
        "rap": "HIP_HOP",
        "pop": "POP",
        "rock": "ROCK",
        "r&b": "RNB",
    }

    @classmethod
    def normalize(cls, genre):

        if genre is None:

            return "UNKNOWN"

        genre = str(genre).strip().lower()

        return cls.GENRE_MAPPING.get(genre, "OTHER")
