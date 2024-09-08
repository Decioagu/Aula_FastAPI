from fastapi import APIRouter

router = APIRouter()

# rota
@router.get('/api/v1/cursos')
async def get_cursos():
    return {"info": "Todos os cursos"}