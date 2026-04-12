from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = "postgresql://postgres:MotDePasse@localhost:5432/coingecko"
#DATABASE_URL = "postgresql://postgres:MotDePasse@localhost:5432/coingecko"

#moteur
engine  = create_engine(DATABASE_URL)


#session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#la clase Base pour les modelels
class Base(DeclarativeBase):
    pass

#une fonction pour gérer la connexion à la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


