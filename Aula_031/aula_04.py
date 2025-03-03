# Seção 2 (FastAPI - APIs Modernas e Assíncronas com Python)
from fastapi import FastAPI

# instanciar API
app = FastAPI()

# rota 
@app.get('/', description='Retorna uma mensagem', summary='Mensagem') # (home)
async def msg(): # função da rota
    return {"msg": "Décio santana de Aguiar"} # mensagem

if __name__ == 'main':
    
    from uvicorn import run # subir o servidor: uvicorn Aula_04.aula_04:app --reload

    # run('main:app', host="127.0.0.1", port=8000, log_level='info', reload=True)
    run('main:app', host="0.0.0.0", port=8000, log_level='info', reload=True)
