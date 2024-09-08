from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from core.configs import settings

# conexão do Banco de Dados
engine: AsyncEngine = create_async_engine(settings.DB_URL)

# cria um objeto de sessão de Banco de Dados assíncrono para interações
Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)
