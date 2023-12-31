from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base

## User Model
# This model is used to store the user information in the database.
# Only the hashed_password is stored in the database instead of the real password.
# The is_active and is_superuser are used to identify the user's role.

class User(Base):
    __tablename__ = 'user'  # type: ignore
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
