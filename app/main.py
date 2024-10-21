from fastapi import FastAPI
from app.core.database import engine, Base
from app.routers import user  # Import your user router

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include your routers (for endpoints)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Event Management API"}
