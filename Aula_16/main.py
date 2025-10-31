from fastapi import FastAPI

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from config.conf_db import settings
from routes.v1.api_router import api_router 

app: FastAPI = FastAPI(title='Curso API - FastAPI SQL Model')

# rota (home)
@app.get('/', description='Retorna uma mensagem', summary='Documento', tags=["Documentação"])
async def index(): # recurso GET
   return {"http://127.0.0.1:8000/docs"}

app.include_router(api_router, prefix=settings.API_V1_STR) #


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

# uvicorn Aula_16.main:app --reload

# https://jwt.io/
# "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzQzNTQyOTI4LCJpYXQiOjE3NDI5MzgxMjgsInN1YiI6IjEifQ.GQSrSDaNw0k_152bxEnQCvOO_pxlXAYsq3kDAe8hSBc"
# JWT_SECRET: str = "qS96E1oCfq5gEZH-ngD91NC2qkcl0cffhNTIDGpF4pw" 