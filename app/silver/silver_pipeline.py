from app.silver.silver_engine import SilverEngine


class SilverPipeline:

    def run(self, dataframe):

        engine = SilverEngine()

        return engine.process(dataframe)
