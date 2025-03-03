# Seção 3 (FastAPI - APIs Modernas e Assíncronas com Python)
# alua 10 até 16
from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
from typing import Optional

'''
"Optional" é um tipo genérico que representa um
valor que pode ser do tipo especificado ou None. 
Ex:
    id: Optional[int] = None
'''

# modelagem e validação tipo (tratamento de entrada do usuário)
class Curso(BaseModel):
    # (modelo: tipo = valor)
    titulo: str
    aulas: Optional[int] = 1
    horas: int

# instanciar API
app = FastAPI(title='Aula 02', version='0.0.1', description= 'Alua 10 até 16')

# dados iniciais
cursos = {
            1: {
                "titulo": "Programação para Leigos",
                "aulas": 112,
                "horas": 58
            },
            2: {
                "titulo": "Algoritmos e logica de programação",
                "aulas": 87,
                "horas": 43
            }
        }

# rota
@app.get('/')
async def get_site():
    return 'Abra===> http://127.0.0.1:8000/docs'

# rota (Ler todos os dados)
@app.get('/cursos')
async def get_cursos():
    return cursos

# rota (Ler dados por id)
@app.get('/cursos/{curso_id}')
async def get_curso_por_id(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        # Tratamento de id não existente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
# rota (Criar novo curso)
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    
    # ======================================================
    # adição de novo id com maior valor existente na lista "cursos"
    proximo_id = 0 # nova chave
    for id in cursos.keys():
        print(id)
        if id > proximo_id:
            proximo_id = id
    proximo_id += 1
    # ======================================================

    cursos[proximo_id] = curso
    return cursos

# rota (Atualizar novo curso por id)
@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

    
# rota (Deletar novo curso por id)
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id] # eliminar id do corpo do dados
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Curso não encontrado')

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# Subir o servidor: uvicorn Aula_02.aula_02:app --reload 