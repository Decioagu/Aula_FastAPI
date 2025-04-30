from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

# Certifique-se de que o caminho está correto
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Declaração de rotas para templates
@app.get('/')
async def index(request: Request, usuario: str = 'Décio Santana de Aguiar'):
    context = {
        "request": request,
        "usuario": usuario
    }

    return templates.TemplateResponse('index.html', context=context)

@app.get('/servicos')
async def servicos(request: Request):
    context = {
        "request": request
    }

    return templates.TemplateResponse('servicos.html', context=context)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

# uvicorn Aula_21.main:app --reload
