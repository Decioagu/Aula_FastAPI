from fastapi import HTTPException, status
from fastapi import APIRouter
from typing import List
from models.database import cursos, Curso

router = APIRouter()

# rota
@router.get('/')
async def get_site():
    return 'http://127.0.0.1:8000/docs'

# rota (Ler todos os dados)
@router.get('/cursos', 
         summary='BUSCAR listagem dos cursos ',
         description='Acesso lista de todos os cursos',
         response_model=List[Curso],
         response_description='Modelo de lista 1'
         )
async def get_cursos(): 
    return cursos

# rota (Ler dados por id)
@router.get('/cursos/{curso_id}', 
         summary='BUSCAR curso por id', 
         description='Acesso lista dos cursos por id',
         response_model=Curso,
         response_description='Modelo de lista 2'
         )
async def get_curso(curso_id: int):

    # ====================================================== 
    # filtrar "cursos" por id
    filtrar_id_curso = filter(lambda meu_id: meu_id.id == curso_id, cursos)
    curso = dict(*filtrar_id_curso)
    # ======================================================

    if curso:
        return curso
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')