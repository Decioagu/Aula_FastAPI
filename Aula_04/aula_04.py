from fastapi import FastAPI, HTTPException, status, Response, Path, Query, Header, Depends
from model import Curso
from typing import Optional, Any
from time import sleep

# instanciar API
app = FastAPI()

# Simulação de abertura de um banco de dados Dependência <======================
def falso_db():
    try:
        print("Abrindo conexão banco de dados...")
        sleep(1.5)
    finally:
        print("Fechando conexão banco de dados...")
        sleep(1.5)


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
async def get_cursos(db: Any = Depends(falso_db)):
    return cursos

# Ler dados por id
@app.get('/cursos/{curso_id}')
# db: Any = Depends(falso_db) Dependência <===============================================
async def get_curso(curso_id: int = Path(title='id do curso', 
                                         description='Deve ser maior que 1 e menor que 5', 
                                         ge=1, le=5),
                    db: Any = Depends(falso_db)
                    ):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
# Criar novo curso
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
# db: Any = Depends(falso_db) Dependência <===============================================
async def post_curso(curso: Curso, db: Any = Depends(falso_db)):
    proximo_id: int = len(cursos) + 1
    cursos[proximo_id] = curso
    del curso.id # eliminar id do corpo do dados
    return cursos

# Atualizar novo curso por id
@app.put('/cursos/{curso_id}')
# db: Any = Depends(falso_db) Dependência <===============================================
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(falso_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id # eliminar id do corpo do dados
        return curso
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

    
# Deletar novo curso por id
@app.delete('/cursos/{curso_id}')
# db: Any = Depends(falso_db) Dependência <===============================================
async def delete_curso(curso_id: int, db: Any = Depends(falso_db)):
    if curso_id in cursos:
        del cursos[curso_id] # eliminar id do corpo do dados
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Curso não encontrado')
    
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
    