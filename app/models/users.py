from sqlalchemy import Column, Integer, String

from app.models.base_model  import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hash_password = Column(String, nullable=False)
