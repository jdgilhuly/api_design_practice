import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# After creating the user and database, update your application's database connection string.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://tester:georgie@localhost:5432/test")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
