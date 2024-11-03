from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

#postgresql://database_rifa_user:BbhoY84Y0jbEj8k34RwodIlcp4PT42AQ@dpg-csjrqd5ds78s7394r1s0-a.oregon-postgres.render.com/database_rifa
SQLITE_DATABASE_URL = "sqlite:///./database.db"
POSTGRESQL_DATABASE_URL = "postgresql+psycopg2://database_rifa_user:BbhoY84Y0jbEj8k34RwodIlcp4PT42AQ@dpg-csjrqd5ds78s7394r1s0-a.oregon-postgres.render.com:5432/database_rifa"
engine = create_engine(POSTGRESQL_DATABASE_URL)
#engine = create_engine(SQLITE_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    with SessionLocal() as db:
        yield db

#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#       db.close()