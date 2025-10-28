from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel # Modelagem Banco de Dados
from schemas.curso_schemas import CursoSchema # Modelagem API (Get)
from schemas.curso_schemas import CursoSchemaSemID # Modelagem API (Post e Put)
from config.conf_db import get_session # Abrir e fechar Sessão

rota_cursos = APIRouter() # roteador

# GET cursos
@rota_cursos.get('/', response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel) # Filtro (Todos)
        result = await session.execute(query) # Executar Filtro no Banco de Dados
        cursos: List[CursoModel] = result.scalars().all() # Trazer todos como uma lista
        '''O método .scalars() é usado em consultas que retornam múltiplos objetos ou valores.
            - result.all() → Retorna uma lista de tuplas com os objetos.
            - result.scalars().all() → Retorna apenas os objetos, sem tuplas.
        '''
        return cursos


# GET curso
@rota_cursos.get('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id) # Filtro por ID
        result = await session.execute(query) # Executar Filtro no Banco de Dados
        curso = result.scalar_one_or_none() # Trazer um objeto ou None

        # Se existir (Exibir)
        if curso:
            return curso
        else:
            raise HTTPException(detail='Curso não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# POST curso
@rota_cursos.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchemaSemID)
async def post_curso(curso: CursoSchemaSemID, db: AsyncSession = Depends(get_session)):
    # variavel = Modelagem BANCO DE DADOS(Modelagem API)
    novo_curso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)

    db.add(novo_curso) # Adicionar BANCO DE DADOS
    await db.commit() # Enviar ao BANCO DE DADOS

    return novo_curso


# PUT curso
@rota_cursos.put('/{curso_id}', response_model=CursoSchemaSemID, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoSchemaSemID, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id) # Filtro por ID
        result = await session.execute(query) # Executar Filtro no Banco de Dados
        curso_up = result.scalar_one_or_none() # Trazer um objeto ou None

        # Se existir (Atualize)
        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.aulas = curso.aulas
            curso_up.horas = curso.horas

            await session.commit() # Enviar ao BANCO DE DADOS

            return curso_up
        else:
            raise HTTPException(detail='Curso não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE curso
@rota_cursos.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id) # Filtro por ID
        result = await session.execute(query) # Executar Filtro no Banco de Dados
        curso_del = result.scalar_one_or_none() # Trazer um objeto ou None

        # Se existir (Excluir)
        if curso_del:
            await session.delete(curso_del) # Deletar curso por ID
            await session.commit() # Enviar ao BANCO DE DADOS

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Curso não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)
