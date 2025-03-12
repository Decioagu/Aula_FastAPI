from fastapi import FastAPI

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from config.conf_db import settings
from routes.v1.api import api_router 

app: FastAPI = FastAPI(title='Curso API - FastAPI SQL Model')

# rota (home)
@app.get('/', description='Retorna uma mensagem', summary='Documento', tags=["Documentação"])
async def index(): # recurso GET
   return {"http://127.0.0.1:8000/docs"}

app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)

# uvicorn Aula_12.main:app --reload