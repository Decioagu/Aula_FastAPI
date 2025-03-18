from fastapi import APIRouter

from routes.v1.endpoints import curso_CRUD

api_router = APIRouter() # roteador
api_router.include_router(curso_CRUD.rota_cursos, prefix='/cursos', tags=["cursos"]) # (inclusão de roteadores) 

