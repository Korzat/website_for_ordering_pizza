from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base_model  import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    products = relationship("Product", back_populates="category")

