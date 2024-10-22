from sqlalchemy.orm import Session
from app.modules.user import User

def seed_database(db: Session):
    # Check if the database is already seeded
    if db.query(User).first():
        return

    # Create initial users
    users = [
        User(username="admin", email="admin@example.com", hashed_password=User.hash_password("adminpassword"), is_admin=True),
        User(username="user", email="user@example.com", hashed_password=User.hash_password("userpassword"))
    ]

    db.add_all(users)
    db.commit()

