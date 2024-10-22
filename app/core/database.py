import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use environment variable for DATABASE_URL, with a fallback for local development
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://tester:georgie@localhost:5432/test")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
