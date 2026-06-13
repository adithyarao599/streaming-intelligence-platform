from app.core.session import SessionLocal


class FactLoader:

    def load(self, dataframe, model):

        db = SessionLocal()

        try:

            records = dataframe.to_dict(orient="records")

            for record in records:

                db.add(model(**record))

            db.commit()

        finally:

            db.close()
