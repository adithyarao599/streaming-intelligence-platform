from app.warehouse.dimension_loader import DimensionLoader
from app.warehouse.fact_loader import FactLoader


class WarehousePipeline:

    def run(self, dimension_df, fact_df, dimension_model, fact_model):

        DimensionLoader().load(dimension_df, dimension_model)

        FactLoader().load(fact_df, fact_model)
