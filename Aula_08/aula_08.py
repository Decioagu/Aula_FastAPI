from fastapi import FastAPI
import sys
import os

# Caminho
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from routes.rotas import router

# instanciar API
app = FastAPI(
             title='Aula_08',
             version='0.0.8',
             description= 'Alua 31'
             )

# rota
@app.get('/')
async def get_site():
    return 'http://127.0.0.1:8000/docs'

# Agrupamento de rotas 
app.include_router(router, tags=['cursos'])

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_08.aula_08:app --reload
     