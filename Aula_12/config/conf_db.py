# ========================= CAMINHO ARQUIVO SQLite ==============================
from pathlib import Path # Pasta

# Criando uma engine para um banco SQLite (ou pode ser MySQL, PostgreSQL etc.)
caminho_do_arquivo = Path(__file__).parent.parent

# ========================= ROTAS API (RECURSOS) ===============================
# ======================= CONEXÃO BANCO DE DADOS ===============================
from pydantic_settings import BaseSettings

#  Gerenciar configurações de aplicativos
class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1' # anotação rota
    DB_URL: str = f"sqlite+aiosqlite:///{caminho_do_arquivo}/faculdade.db" # SQLite
    # DB_URL: str = 'mysql+aiomysql://root:Enigma.1@localhost:3306/faculdade' # MySQL

    # Define que as variáveis de ambiente no Pydantic devem ser sensíveis a maiúsculas e minúsculas.
    class Config:
        case_sensitive = True

settings = Settings()

# ========================= SESSÃO BANCO DE DADOS =============================
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

# conexão do Banco de Dados (ENDEREÇO BANCO DE DADOS)
engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=False)

# Cria sessão de Banco de Dados assíncrono (INTERAÇÃO)
Session: AsyncSession = sessionmaker(
    autocommit=False, # não faz "commit" automaticamente
    autoflush=False, # não executar consulta automáticas 
    expire_on_commit=False, # sessão não aspirá apos "commit"
    class_=AsyncSession, #  sessão assíncrono
    bind=engine # ativa conexão com o banco de dados
)
# ================= SESSÃO COMMIT (ABERTURA E FECHAMENTO) ======================
from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

# consulta no Banco de Dados
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session # Abrir sessão
    finally:
        await session.close() # Fechar sessão

