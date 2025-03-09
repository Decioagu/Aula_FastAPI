from sqlalchemy.ext.declarative import declarative_base

# ===============================================================================
from pathlib import Path # Pasta

# Criando uma engine para um banco SQLite (ou pode ser MySQL, PostgreSQL etc.)
caminho_do_arquivo = Path(__file__).parent
# ===============================================================================

DBBaseModel = declarative_base()

# Definição direta da URL do banco de dados
DB_URL: str = f"sqlite+aiosqlite:///{caminho_do_arquivo}/faculdade.db"
# ===============================================================================

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

# conexão do Banco de Dados (ENDEREÇO BANCO DE DADOS)
engine: AsyncEngine = create_async_engine(DB_URL, echo=False)

# Cria sessão de Banco de Dados assíncrono (INTERAÇÃO)
Session: AsyncSession = sessionmaker(
    autocommit=False, # não faz commit automaticamente
    autoflush=False, # não executar consulta automáticas 
    expire_on_commit=False, # sessão não aspirá apos commit
    class_=AsyncSession, #  sessão assíncrono
    bind=engine # ativa conexão com o banco de dados
)
# ===============================================================================

from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

# consulta no Banco de Dados
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session # Abrir sessão
    finally:
        await session.close() # Fechar sessão

