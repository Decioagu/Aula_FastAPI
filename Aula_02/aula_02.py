from fastapi import FastAPI, HTTPException, status, Response
from model import Curso

# instanciar API
app = FastAPI()

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
        "horas": 67
    }
}

# Ler todos os dados
@app.get('/cursos')
async def get_cursos():
    return cursos

# Ler dados por id
@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
# Criar novo curso
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    proximo_id: int = len(cursos) + 1
    cursos[proximo_id] = curso
    del curso.id # eliminar id do corpo do dados
    return cursos

# Atualizar novo curso por id
@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id # eliminar id do corpo do dados
        return curso
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

    
# Deletar novo curso por id
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id] # eliminar id do corpo do dados
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Curso não encontrado')

if __name__ == 'main':
    
    from uvicorn import run # subir o servidor

    run('main:app', host="127.0.0.1", port=8000, reload=True)
    