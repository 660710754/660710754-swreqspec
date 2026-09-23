from app.db.models import Base


def upgrade(engine):
    Base.metadata.create_all(bind=engine)
