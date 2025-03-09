from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

from pathlib import Path # Pasta

# Criando uma engine para um banco SQLite (ou pode ser MySQL, PostgreSQL etc.)
caminho_do_arquivo = Path(__file__).parent

'''
Use "BaseSettings" para gerenciar configurações de aplicativos:
    - Herda todos os recursos de "BaseModel".
'''
DBBaseModel = declarative_base()

#  Gerenciar configurações de aplicativos
class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1' # anotação rota
    DB_URL: str = f"sqlite+aiosqlite:///{caminho_do_arquivo}/faculdade.db" # (SQLite)
    '''
    O ClassVar é um tipo especial do módulo typing do Python, usado para indicar que
    um atributo dentro de uma classe não deve ser tratado como um campo de instância,
    mas sim como um atributo da classe.
    '''    
    # Define que as variáveis de ambiente no Pydantic devem ser sensíveis a maiúsculas e minúsculas.
    class Config:
        case_sensitive = True

# instanciar
settings = Settings()


from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

# conexão do Banco de Dados (ENDEREÇO BANCO DE DADOS)
engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=False)

# Cria sessão de Banco de Dados assíncrono (INTERAÇÃO)
Session: AsyncSession = sessionmaker(
    autocommit=False, # não faz commit automaticamente
    autoflush=False, # não executar consulta automáticas 
    expire_on_commit=False, # sessão não aspirá apos commit
    class_=AsyncSession, #  sessão assíncrono
    bind=engine # ativa conexão com o banco de dados
)

# from sqlalchemy import Column, String, Integer

# class Filmes(DBBaseModel):
#     __tablename__="filmes"

#     titulo = Column(String(25), primary_key=True)
#     genero = Column(String(25), nullable=False)
#     ano = Column(Integer, nullable=False)


from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

# consulta no Banco de Dados
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session # Abrir sessão
    finally:
        await session.close() # Fechar sessão


async def create_tables() -> None:
 
    print('Criando as tabelas no banco de dados...')

    async with engine.begin() as conn:
        await conn.run_sync(DBBaseModel.metadata.drop_all) # Apagar Tabela
        await conn.run_sync(DBBaseModel.metadata.create_all) # Criar Tabela
    print('Tabelas criadas com sucesso...')

if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())