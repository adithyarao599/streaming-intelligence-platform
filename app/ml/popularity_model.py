from sklearn.ensemble import RandomForestRegressor


class PopularityModel:

    def train(self, x_train, y_train):

        model = RandomForestRegressor(n_estimators=100, random_state=42)

        model.fit(x_train, y_train)

        return model
