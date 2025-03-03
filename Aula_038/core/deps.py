from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session

# consulta no Banco de Dados
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session # iterar sobre Banco de Dados
    finally:
        await session.close() # fechar apos uso
