from app.gold.feature_store import FeatureStore


class FeatureLoader:

    @staticmethod
    def load_features(dataframe):

        return FeatureStore.get_features(dataframe)
