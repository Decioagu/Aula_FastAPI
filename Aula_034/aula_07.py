from fastapi import FastAPI, HTTPException, status, Response, Depends
from typing import Optional, Any
from pydantic import BaseModel
from time import sleep

'''
O "BaseModel" no Pydantic é uma classe base que permite a 
criação de modelos de dados com validação e tipagem automática

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
app = FastAPI(
             title='Aula 07',
             version='0.0.1',
             description= 'Alua 20 até 19'
             )

# Simulação de abertura de um banco de dados Dependência <======================
def falso_db():
    try:
        print("Abrindo conexão banco de dados...")
        sleep(2)
    finally:
        print("Fechando conexão banco de dados...")
        sleep(2)


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

# rota
@app.get('/')
async def get_site():
    return 'Abra===> http://127.0.0.1:8000/docs'

# rota (Ler todos os dados)
@app.get('/cursos')
# db: Any = Depends(falso_db) <===========================================================
async def get_cursos(db: Any = Depends(falso_db)): # Dependência <========================
    return cursos

# rota (Ler dados por id)
@app.get('/cursos/{curso_id}')
# db: Any = Depends(falso_db) <===========================================================
async def get_curso(curso_id: int , db: Any = Depends(falso_db)): # Dependência <=========
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
# rota (Criar novo curso)
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
# db: Any = Depends(falso_db) <===========================================================
async def post_curso(curso: Curso, db: Any = Depends(falso_db)): # Dependência <==========

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
# db: Any = Depends(falso_db) <===========================================================
async def put_curso(curso_id: int, 
                    curso: Curso, 
                    db: Any = Depends(falso_db) # Dependência <===========================
                    ):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

    
# rota (Deletar novo curso por id)
@app.delete('/cursos/{curso_id}')
# db: Any = Depends(falso_db) <===========================================================
async def delete_curso(curso_id: int, db: Any = Depends(falso_db)): # Dependência <=======
    if curso_id in cursos:
        del cursos[curso_id] # eliminar id do corpo do dados
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Curso não encontrado')

if __name__ == 'main':
    
    from uvicorn import run # subir o servidor uvicorn Aula_07.aula_07:app --reload

    run('main:app', host="127.0.0.1", port=8000, reload=True)
     