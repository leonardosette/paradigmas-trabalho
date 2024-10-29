from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from config import Base

class Mission(Base):
    __tablename__ = "missions"
    
    mission_id = Column(Integer, primary_key=True, index=True)
    nome_missao = Column(String, nullable=False)
    descricao = Column(Text)
    nivel_dificuldade = Column(Integer, nullable=False)
    resultado = Column(String)
    recompensa_forca = Column(Integer)
    recompensa_popularidade = Column(Integer)
    
    herois = relationship("Hero", secondary="hero_missions", back_populates="missoes")
