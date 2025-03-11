from fastapi import FastAPI, HTTPException, status
import sys
import os

# Caminho
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from routes.rotas import router as rotas

# instanciar API
app = FastAPI(
             title='Aula_07',
             version='0.0.7',
             description= 'Alua 21'
             )

# Incluir as rotas
app.include_router(rotas)

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_08.aula_08:app --reload
     