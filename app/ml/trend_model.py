from sklearn.linear_model import LinearRegression


class TrendModel:

    def train(self, x_train, y_train):

        model = LinearRegression()

        model.fit(x_train, y_train)

        return model
