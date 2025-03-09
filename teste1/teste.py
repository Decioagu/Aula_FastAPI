from sqlalchemy import Column, String, Integer

from conf_db import engine, DBBaseModel

class Filmes(DBBaseModel):
    __tablename__="filmes"

    titulo = Column(String(25), primary_key=True)
    genero = Column(String(25), nullable=False)
    ano = Column(Integer, nullable=False)