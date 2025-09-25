import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#  we are connecting to a MySQL database using the mysqlconnector driver.
# For a local MySQL setup, the URL format is:
# "mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database>"
DATABASE_URL = "mysql+mysqlconnector://spotifyuser:Aditya12@localhost:3306/spotify_lite"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class. 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a DeclarativeBase class.
# Think of it as the foundation upon which all our table definitions will be built.
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
