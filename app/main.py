from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base, SessionLocal
from app.routers import user  # Import your user router
from sqlalchemy import text
from app.core.seed import seed_database

# Create the database tables
Base.metadata.create_all(bind=engine)

# Seed the database
with SessionLocal() as db:
    seed_database(db)

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change this for production to specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Include your routers (for endpoints)
app.include_router(user.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the Event Management API"}

@app.get("/test-db")
async def test_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users LIMIT 1"))
        return {"result": [dict(r) for r in result]}
