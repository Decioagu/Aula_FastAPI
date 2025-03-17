from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User  # Supondo que temos um modelo User

async def get_users(session: AsyncSession):
    stmt = select(User)  # Cria uma consulta para selecionar todos os usuários
    result = await session.execute(stmt)  # Executa a consulta de forma assíncrona
    return result.scalars().all()  # Retorna a lista de usuários


Porque ocorre erro:
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User  # Supondo que temos um modelo User

async def get_users(session: AsyncSession):
    stmt = db.query(User).all() # Cria uma consulta para selecionar todos os usuários  
    result = await session.execute(stmt)  # Executa a consulta de forma assíncrona
    return result.scalars().all()  # Retorna a lista de usuários