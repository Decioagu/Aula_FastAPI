from typing import ClassVar, Any
from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base

from pathlib import Path # Pasta

# Criando uma engine para um banco SQLite (ou pode ser MySQL, PostgreSQL etc.)
caminho_do_arquivo = Path(__file__).parent.parent

'''
Use "BaseSettings" para gerenciar configurações de aplicativos:
    - Herda todos os recursos de "BaseModel".
'''
#  Gerenciar configurações de aplicativos
class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1' # anotação rota
    DB_URL: str = f"sqlite+aiosqlite:///{caminho_do_arquivo}/faculdade.db" # (SQLite)
    '''
    O ClassVar é um tipo especial do módulo typing do Python, usado para indicar que
    um atributo dentro de uma classe não deve ser tratado como um campo de instância,
    mas sim como um atributo da classe.
    '''
    DBBaseModel: Any = declarative_base() # ORM (Object-Relational Mapping)
    
    # Define que as variáveis de ambiente no Pydantic devem ser sensíveis a maiúsculas e minúsculas.
    class Config:
        case_sensitive = True

# instanciar
settings = Settings()
