from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

from database import Session ### Sessão do Banco de Dados

import models.__all_models

# consulta no Banco de Dados
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session # Abrir sessão
    finally:
        await session.close() # Fechar sessão
