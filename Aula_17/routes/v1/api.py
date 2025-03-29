from fastapi import APIRouter


from routes.v1.endpoints import rota_artigo
from routes.v1.endpoints import rota_usuario


api_router = APIRouter()

api_router.include_router(rota_artigo.router, prefix='/artigos', tags=['artigos'])
api_router.include_router(rota_usuario.router, prefix='/usuarios', tags=['usuarios'])
