from fastapi import FastAPI, APIRouter

# Instanciar API
app = FastAPI() 

# Criando um roteador
rotas = APIRouter()

# Rota GET
@rotas.get("/")
async def listar_itens():
    return {"mensagem": "Lista de itens"}

# Rota POST
@rotas.post("/")
async def criar_item(item: dict):
    return {"mensagem": "Item criado", "item": item}

# Incluindo o roteador na aplicação principal
app.include_router(rotas)

if __name__ == 'main':
    
    from uvicorn import run 

    run('TESTE:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn TESTE:app --reload