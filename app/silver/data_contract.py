class DataContract:

    CONTRACTS = {
        "spotify": ["track_name", "artist_name", "streams"],
        "netflix": ["title", "release_year"],
    }

    @classmethod
    def get_contract(cls, dataset):

        return cls.CONTRACTS[dataset]
