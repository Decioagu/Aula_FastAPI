from sqlalchemy import Column, Integer, String

from conf_db import DBBaseModel ### Configurações Banco de Dados

class Filmes(DBBaseModel):
    __tablename__="filmes"
    titulo = Column(String(25), primary_key=True)
    genero = Column(String(25), nullable=False)
    ano = Column(Integer, nullable=False)