from fastapi import APIRouter
from dados.database import produtos # Modelagem ("Banco de Dados")

router = APIRouter()

@router.get('/')
async def index():
    return {"message": "http://127.0.0.1:8000/docs"}


@router.get('/produtos/')
async def buscar_produtos(): # recurso GET
    return produtos


@router.get('/produtos/{id}') # rota (busca por id)
async def buscar_produto_por_id(id: int): # recurso GET
    for produto in produtos:
        if produto.id == id:
            return produto
    return None