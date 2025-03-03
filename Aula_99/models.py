from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    preco = Column(Float)
    em_oferta = Column(Boolean, default=False)
