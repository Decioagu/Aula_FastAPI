from sqlalchemy import Column, Integer, String

import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config_db3.conf_db import DBBaseModel ### Configurações Banco de Dados

class Filmes(DBBaseModel):
    __tablename__="filmes"
    titulo = Column(String(25), primary_key=True)
    genero = Column(String(25), nullable=False)
    ano = Column(Integer, nullable=False)