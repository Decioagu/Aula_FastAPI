from fastapi import FastAPI
from pydantic import BaseModel

# modelagem e validação tipo
class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False

# instanciar API
app = FastAPI()

# rotas (lista de produtos => rotas)
produtos = [
    Produto(id=1, nome='Playstation 5', preco=5745.55, em_oferta=True),
    Produto(id=2, nome='Nintendo Wii', preco=2654.12),
    Produto(id=3, nome='Xbox 360', preco=1765.34, em_oferta=True),
    Produto(id=4, nome='Super Nintendo', preco=234.67),
    Produto(id=5, nome='Atari 2600', preco=199.90, em_oferta=True),
]

# rota (home)
@app.get('/')
async def index():
   return {"msg": "Décio santana de Aguiar"}

# rota (busca por id)
@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None

# rota (atualizar produtos por id)
@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto

            return prod # receber resposta atualizada
    return None

# pip instal fastapi
# pip instal uvicorn
# Pasta Aula_01: cd .\Aula_01\
# Acesso ao terminal: uvicorn main:app --reload
# Acesso: http://127.0.0.1:8000 
# Sair: Pressionar: Ctrl+C 

'''
Acessar a API:
Acesse a URL principal: http://127.0.0.1:8000

Documentação interativa:
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc
'''