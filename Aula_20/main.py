from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='Aula_20/templates')
# templates = Jinja2Templates(directory='templates')

# Declaração de rotas para templates
@app.get('/')
async def index(request: Request, usuario: str = 'Décio Santana de Aguiar'):
    context = {
        "request": request, # objeto de requisição (obrigatório)
        "usuario": usuario # linha 14 de index.html
    }
    return templates.TemplateResponse('index.html', context=context) # conexão arquivo HTML

@app.get('/servicos')
async def servicos(request: Request):
    context = {
        "request": request # objeto de requisição (obrigatório)
    }
    return templates.TemplateResponse('servicos.html', context=context) # conexão arquivo HTML

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

# uvicorn Aula_20.main:app --reload
# uvicorn main:app --reload

'''
OBS :
    Ao executar "uvicorn Aula_20.main:app --reload" é necessário que 
    "templates = Jinja2Templates(directory='Aula_20/templates')" ou o arquivo não será encontrado.

    Caso execute o "uvicorn main:app --reload" dentro da pasta Aula_20 utilize
    "templates = Jinja2Templates(directory='templates')" ou o arquivo não será encontrado.

Aula_FastAPI/
├── Aula_20/
│   └── main.py
│   templates/
│   └── index.html
│   └── servico.html       
'''
