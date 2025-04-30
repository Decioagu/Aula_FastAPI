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
app.mount('/download', StaticFiles(directory=os.path.join(BASE_DIR, 'download')), name='download') ###

# Certifique-se de que o caminho está correto "Aula_22/download"
pasta_de_download = os.path.join(BASE_DIR, "download") ###
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

# ================= BAIXAR ARQUIVOS DO USUÁRIO =========================
from fastapi import UploadFile ###
from aiofile import async_open ###
from uuid import uuid4 ###

@app.post('/servicos')
async def cad_servicos(request: Request):
    form = await request.form() # requerimento para formulário

    servico: str = form.get('servico') # extrair formulário do usuário
    print(f"Serviço: {servico}") # exibir no terminal (texto do usuário)

    arquivo: UploadFile = form.get('arquivo') ### BUSCAR ARQUIVO
    print(f"Nome do arquivo: {arquivo.filename}") ### exibir no terminal (nome do arquivo)
    print(f"Tipo do arquivo: {arquivo.content_type}") ### exibir no terminal (tipo do arquivo)

    # Nome aleatório para arquivo (para não sobre escrever arquivo já existente: OPCIONAL)
    arquivo_ext: str = arquivo.filename.split('.')[-1] ### separar nome por pontos ([1] separa extensão)
    novo_nome: str = f"{str(uuid4())}.{arquivo_ext}" ###  identificador único gerado de forma aleatória

    context = {
        "request": request,
        "arquivo_download": novo_nome ### linha 28 de servicos.html
    }

    async with async_open(f"{pasta_de_download}/{novo_nome}", "wb") as afile: ### criar arquivo
        await afile.write(arquivo.file.read()) ### escrever arquivo
    
    return templates.TemplateResponse('servicos.html', context=context)
# ============================================================================


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

# uvicorn Aula_24.main:app --reload

'''
Observação, o uso de:
    from fastapi.staticfiles import StaticFiles
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

independe e a execução:
    Fora da pasta: uvicorn Aula_22.main:app --reload
    Dentro da pasta: uvicorn main:app --reload
'''
