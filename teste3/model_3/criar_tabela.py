import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config_db3.conf_db import engine, DBBaseModel

async def create_tables() -> None:
    
    
    # Importando modelos antes da criação das tabelas
    import model
    print('Criando as tabelas no banco de dados...')

    async with engine.begin() as conn:
        print(DBBaseModel.metadata.tables.keys())
        await conn.run_sync(DBBaseModel.metadata.drop_all) # Apagar Tabela
        await conn.run_sync(DBBaseModel.metadata.create_all) # Criar Tabela
    print('Tabelas criadas com sucesso...')

if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())