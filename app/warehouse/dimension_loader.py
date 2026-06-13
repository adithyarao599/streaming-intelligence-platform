from app.core.session import SessionLocal


class DimensionLoader:

    def load(self, dataframe, model):

        db = SessionLocal()

        try:

            records = dataframe.to_dict(orient="records")

            for record in records:

                db.add(model(**record))

            db.commit()

        finally:

            db.close()
