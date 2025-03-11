from fastapi import FastAPI

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from config.conf_db import settings
from api.v1.api import api_router

# instanciar
app = FastAPI(title='Cursos API - FastAPI SQL Alchemy')

# rotas
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

# uvicorn Aula_10.main:app --reload