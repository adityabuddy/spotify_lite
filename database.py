import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database URL. This can be stored in environment variables for security.
# For a local MySQL setup, the URL format is:
# "mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database>"
DATABASE_URL = "mysql+mysqlconnector://spotifyuser:Aditya12@localhost:3306/spotify_lite"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class. Each instance of this class will be a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a DeclarativeBase class. This is the base class for all our database models.
# Think of it as the foundation upon which all our table definitions will be built.
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()