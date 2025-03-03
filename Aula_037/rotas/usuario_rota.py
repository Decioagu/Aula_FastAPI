from fastapi import APIRouter

router = APIRouter()

# rota
@router.get('/api/v1/usuarios')
async def get_usuarios():
    return {"info": "Todos os usuarios"}