# Seção 3 (FastAPI - APIs Modernas e Assíncronas com Python)
# alua 17 até 19
from fastapi import FastAPI, HTTPException, status, Path, Query, Header
from typing import Optional

# instanciar API
app = FastAPI(
             title='Aula 06',
             version='0.0.1',
             description= 'Alua 17 até 19'
             )

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
async def get_cursos():
    return cursos

# rota (Ler dados por id)
@app.get('/cursos/{curso_id}')
# limitar parâmetro de pesquisa por Path | (Header) Ex: http://127.0.0.1:8000/cursos/1 <========
async def get_curso(curso_id: int = Path(title='Id do curso', 
                                         description='curso_id deve ser min=1 e max=3', 
                                         ge=1, le=3)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
# rota (Ler parâmetro com Query)
@app.get('/calculadora')
# enviar valores por Query | | (Header) Ex: http://127.0.0.1:8000/calculadora?a=5&b=3&c=2 <======
async def get_calculadora(a: int = Query(), b: int = Query(), c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma  = soma + c
    return {"resultado": soma}

# rota (Enviar mensagem por Headers) | 
@app.get('/msg')
# Clique na aba "Headers" abaixo do campo da URL <===============================================
# Ex: Name: x-msg Value: Decio Santana de Aguiar <===============================================
async def get_msg(x_msg: str = Header()):
    print(f"mensagem: {x_msg}")
    return {"mensagem": x_msg}

if __name__ == 'main':
    
    from uvicorn import run # subir o servidor: uvicorn Aula_06.aula_06:app --reload

    run('main:app', host="127.0.0.1", port=8000, reload=True)
    