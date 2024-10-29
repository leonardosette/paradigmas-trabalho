from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from config import Base

class Hero(Base):
    __tablename__ = "heroes"
    
    hero_id = Column(Integer, primary_key=True, index=True)
    nome_real = Column(String, nullable=False)
    nome_heroi = Column(String, unique=True, nullable=False)
    sexo = Column(String)
    altura = Column(Float)
    peso = Column(Float)
    data_nascimento = Column(Date)
    local_nascimento = Column(String)
    nivel_forca = Column(Integer)
    popularidade = Column(Integer)
    status = Column(String, default="Ativo")
    vitorias = Column(Integer, default=0)
    derrotas = Column(Integer, default=0)
    
    # Relações
    crimes = relationship("Crime", back_populates="heroi")
    missoes = relationship("Mission", secondary="hero_missions", back_populates="herois")
