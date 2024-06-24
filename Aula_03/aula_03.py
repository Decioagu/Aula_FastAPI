from fastapi import FastAPI, HTTPException, status, Path, Query, Header
from model import Curso
from typing import Optional

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
    },
    3: {
        "titulo": "Programação linguagem Python",
        "aulas": 33,
        "horas": 47
    }
}

# Ler todos os dados
@app.get('/cursos')
async def get_cursos():
    return cursos

# Ler dados por id
@app.get('/cursos/{curso_id}')
# limitar parâmetro de pesquisa com Path <===============================================
async def get_curso(curso_id: int = Path(title='id do curso', 
                                         description='Deve ser maior que 1 e menor que 3', 
                                         ge=1, le=3)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
# Ler parâmetro com Query <===============================================
@app.get('/calculadora')
async def get_calculadora(a: int = Query(), b: int = Query(), c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma  = soma + c

    return {"resultado": soma}

# Ler parâmetro com Header <===============================================
@app.get('/msg')
async def get_msg(x_msg: str = Header()):
    print(f"mensagem: {x_msg}")
    return {"mensagem": x_msg}

if __name__ == 'main':
    
    from uvicorn import run # subir o servidor

    run('main:app', host="127.0.0.1", port=8000, reload=True)
    