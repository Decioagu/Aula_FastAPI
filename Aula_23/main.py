from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

# ================================ CAMINHO DA URL ====================================
from fastapi.staticfiles import StaticFiles
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Certifique-se de que o caminho está correto "Aula_22/templates"
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Serve arquivos estáticos da pasta "Aula_22/static"
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# ===================================================================================

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

# ================= EXTRAÇÃO DE FORMULÁRIO DO USUÁRIO =========================
@app.post('/servicos')
async def cad_servicos(request: Request):
    form = await request.form() # requerimento de dados via formulário HTML

    servico: str = form.get('servico') # extrair formulário do usuário
    print(f"Serviço: {servico}") # exibir no terminal

    context = {
        "request": request
    }
    
    return templates.TemplateResponse('servicos.html', context=context)
# =============================================================================


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

# uvicorn Aula_23.main:app --reload

'''
Observação, o uso de:
    from fastapi.staticfiles import StaticFiles
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

independe e a execução:
    Fora da pasta: uvicorn Aula_22.main:app --reload
    Dentro da pasta: uvicorn main:app --reload
'''
