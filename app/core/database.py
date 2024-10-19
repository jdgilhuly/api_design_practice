from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://your_username:your_password@localhost:5432/event_management"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
