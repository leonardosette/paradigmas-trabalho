from config import Base, engine
from models.hero import Hero
from models.crime import Crime
from models.mission import Mission

# Criar todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
