import app.models.dim_artist
import app.models.dim_content
import app.models.dim_country
import app.models.dim_date
import app.models.dim_genre
import app.models.dim_platform
import app.models.fact_content_performance
from app.core.database import Base, engine


def create_tables():

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":

    create_tables()

    print("Warehouse tables created.")
