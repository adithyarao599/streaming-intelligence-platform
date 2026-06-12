class ContentClassifier:

    @staticmethod
    def classify(source):

        mapping = {
            "spotify": "SONG",
            "netflix": "SHOW",
            "youtube": "VIDEO",
            "movies": "MOVIE",
        }

        return mapping.get(source, "UNKNOWN")
