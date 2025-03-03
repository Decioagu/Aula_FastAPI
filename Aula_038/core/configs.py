from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base #(desatualizado) aula 27
# from sqlalchemy.orm import DeclarativeBase # novo

# Definindo a nova classe base usando a nova API
class Base(DeclarativeBase):
    __abstract__ = True
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.__str__()}>'

'''
Use "BaseSettings" para gerenciar configurações de aplicativos:
    - Herda todos os recursos de "BaseModel".
    - Pode atribuir valores predefinidos nos modelos.
    - Projetado para gerenciar configurações de aplicativos.
    - Permite ler valores de configuração de diversas fontes.
    - Substitui valores de configurações em diferentes ambientes (desenvolvimento, produção, etc).
    - Carrega configurações de arquivos em diferentes formatos (YAML, JSON, etc).
    - Mantém configurações secretas (gerenciamento de segredos).
'''

#  gerenciar configurações de aplicativos
class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1' # anotação rota
    DB_URL: str = "postgresql+asyncpg://USUARIO:SENHA@localhost:5432/NOME_DO_BANCO" # (PostgresSQL)
    DBBaseModel = declarative_base()
    # DBBaseModel = Base()  # ponte entre Objetos e Bancos de Dados
    
    class Config:
        case_sensitive = True

# instanciar
settings = Settings()
