from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..db_base import Base

class Slab(Base):
    __tablename__ = "slabs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    material_type = Column(String, index=True)
    total_area_m2 = Column(Float, nullable=False)
    available_area_m2 = Column(Float, nullable=False)
    price_per_m2 = Column(Float, nullable=False)
    
    # Futuramente, quando tivermos a tabela 'companies'
    # company_id = Column(Integer, ForeignKey("companies.id"))
    # company = relationship("Company", back_populates="slabs")
