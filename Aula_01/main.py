from fastapi import FastAPI # API
from pydantic import BaseModel # criação de modelo 

# Modelagem
class Produto(BaseModel):
    # (modelo: tipo = valor)
    id: int # validação de tipo
    nome: str # validação de tipo
    preco: float # validação de tipo
    em_oferta: bool = False # validação de tipo

# instanciar API (Descrição de documento)
app = FastAPI(title='Aula 01', version='0.0.1')

# Lista de produtos
produtos = [
    Produto(id=1, nome='Playstation 5', preco=5745.55, em_oferta=True), # Modelagem 
    Produto(id=2, nome='Nintendo Wii', preco=2654.12), # Modelagem 
    Produto(id=3, nome='Xbox 360', preco=1765.34, em_oferta=True), # Modelagem 
    Produto(id=4, nome='Super Nintendo', preco=234.67), # Modelagem 
    Produto(id=5, nome='Atari 2600', preco=199.90, em_oferta=True), # Modelagem 
]


@app.get('/')# rota (home)
async def index(): # recurso GET
   return {"http://127.0.0.1:8000/docs"}


@app.get('/produtos/') # rota (busca)
async def buscar_produtos(): # recurso GET
    return produtos


@app.get('/produtos/{id}') # rota (busca por id)
async def buscar_produto_por_id(id: int): # recurso GET
    for produto in produtos:
        if produto.id == id:
            return produto
    return None

# PACOTES:
# pip install fastapi
# pip install uvicorn
# pip install pydantic

# ACESSO:
# Pasta Aula_01: cd .\Aula_01\
# Acesso ao terminal: uvicorn main:app --reload

# Acesso ao terminal: uvicorn Aula_01.main:app --reload

# Acesso: http://127.0.0.1:8000 
# Sair: Pressionar: Ctrl+C 

'''
Acessar a API:
Acesse a URL principal: http://127.0.0.1:8000

Documentação interativa:
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc
'''

if __name__ == 'main':
    
    from uvicorn import run

    # run('main:app', host="127.0.0.1", port=8000, log_level='info', reload=True)
    run('main:app', host="0.0.0.0", port=8000, log_level='info', reload=True)

# Acesso ao terminal: uvicorn Aula_01.main:app --reload

    '''
    Parâmetros run(<nome_arquivo>:app, host, port, log_level, reload):

    # <nome_arquivo>:app (obrigatório): Este argumento representa o aplicativo ASGI 

    # host (opcional, padrão: "0.0.0.0"): endereço IP no qual o aplicativo escutará as 
    solicitações recebidas ("0.0.0.0" ou "127.0.0.1": localhost)

    # port (opcional, padrão: 8000): Este argumento define o número da porta na qual 
    o aplicativo escutará o tráfego. 

    # log_level (opcional, padrão: "info"): Este parâmetro controla o detalhamento 
    das mensagens de log emitidas pelo Uvicorn durante a execução do aplicativo. 
        Os valores possíveis incluem:
        "debug": mostra todas as mensagens de registro (mais detalhadas).
        "info"(padrão): Mostra mensagens informativas.
        "warning": mostra avisos e erros.
        "error": Mostra apenas erros.

    # reload (opcional, padrão: True): Esta configuração permite o recarregamento automático 
    '''

