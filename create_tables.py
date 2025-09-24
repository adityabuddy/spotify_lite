from database import engine, Base
import models  # This line is crucial! It imports your models and registers them with Base

def create_all_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_all_tables()