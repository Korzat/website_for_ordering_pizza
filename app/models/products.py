from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base_model import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)


    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")
