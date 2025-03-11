from fastapi import FastAPI
import sys
import os

# Caminho
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from routes.rotas import router as rotas

# Instanciar API
app = FastAPI(title='Aula 01', version='0.0.1')


# Incluir as rotas
app.include_router(rotas)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level='info', reload=True)

# uvicorn Aula_00.main:app --reload