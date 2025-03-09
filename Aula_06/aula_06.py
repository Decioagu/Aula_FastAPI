from fastapi import FastAPI, HTTPException, status, Response
from typing import Optional, Dict
from pydantic import BaseModel


# modelagem e validação tipo (tratamento de entrada do usuário)
class Curso(BaseModel):
    # (modelo: tipo = valor)
    titulo: str
    aulas: Optional[int] = 1
    horas: int

# instanciar API
app = FastAPI(
             title='Aula_06',
             version='0.0.6',
             description= 'Alua 21'
             )

# dados iniciais (DICIONÁRIO)
cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e logica de programação",
        "aulas": 87,
        "horas": 67
    },
    3: {
        "titulo": "Programação linguagem Python",
        "aulas": 33,
        "horas": 47
    }
}

# rota
@app.get('/')
async def get_site():
    return 'http://127.0.0.1:8000/docs'

# rota (Ler todos os dados)
@app.get('/cursos', 
         summary='BUSCAR listagem dos cursos ',
         description='Acesso lista de todos os cursos',
         response_model=Dict[int, Curso],
         response_description='Modelo de lista 1'
         )
async def get_cursos(): 
    return cursos

# rota (Ler dados por id)
@app.get('/cursos/{curso_id}', 
         summary='BUSCAR curso por id', 
         description='Acesso lista dos cursos por id',
         response_model=Curso,
         response_description='Modelo de lista 2'
         )
async def get_curso(curso_id: int): 
    try:
        curso = cursos[curso_id] # filtrar "cursos" por id
        return curso
    except KeyError:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)
     
# uvicorn Aula_06.aula_06:app --reload