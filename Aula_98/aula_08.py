from fastapi import FastAPI

from Aula_08.rotas import curso_rota
from Aula_08.rotas import usuario_rota

# instanciar API
app = FastAPI(
    title='Aula 08',
    version='0.0.1',
    description= 'Aula 22'
)

# rota
@app.get('/', tags=['Link'], summary='documentos')
async def get_site():
    return 'http://127.0.0.1:8000/docs'

# rotas
app.include_router(curso_rota.router, tags=['cursos'])
app.include_router(usuario_rota.router, tags=['usuarios'])

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_08.aula_08:app --reload