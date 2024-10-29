from sqlalchemy import Column, Integer, String, Text, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Crime(Base):
    __tablename__ = "crimes"
    
    crime_id = Column(Integer, primary_key=True, index=True)
    nome_crime = Column(String, nullable=False)
    descricao = Column(Text)
    data_crime = Column(Date)
    severidade = Column(Integer, nullable=False)
    oculto = Column(Boolean, default=False)
    
    hero_id = Column(Integer, ForeignKey("heroes.hero_id", ondelete="SET NULL"))
    heroi = relationship("Hero", back_populates="crimes")
