import joblib


class ModelRegistry:

    @staticmethod
    def save_model(model, model_name):

        joblib.dump(model, f"artifacts/models/" f"{model_name}.pkl")
