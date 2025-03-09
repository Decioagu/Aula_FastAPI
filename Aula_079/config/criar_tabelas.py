from configs import settings ### Configuração do Banco de Dados
from database import engine ### Sessão do Banco de Dados

async def create_tables() -> None:
    import sys
    import os

    # Adicionar o caminho do diretório pai ao sys.path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from curso_model import CursoModel
    print('Criando as tabelas no banco de dados...')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all) # Apagar Tabela
        await conn.run_sync(settings.DBBaseModel.metadata.create_all) # Criar Tabela
    print('Tabelas criadas com sucesso...')

if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
