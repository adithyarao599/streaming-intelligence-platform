from sklearn.model_selection import train_test_split

from app.ml.model_registry import ModelRegistry
from app.ml.popularity_model import PopularityModel


class TrainingPipeline:

    def train_popularity_model(self, features, target):

        x_train, x_test, y_train, y_test = train_test_split(
            features, target, test_size=0.2, random_state=42
        )

        model = PopularityModel().train(x_train, y_train)

        ModelRegistry.save_model(model, "popularity_model")

        return model
