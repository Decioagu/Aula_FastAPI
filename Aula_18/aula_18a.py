from fastapi import FastAPI, Query

app = FastAPI()

hoteis = [
    {"id": 1, "nome": "Hotel Sol"},
    {"id": 2, "nome": "Hotel Lua"},
    {"id": 3, "nome": "Hotel Mar"},
    {"id": 4, "nome": "Hotel Céu"},
    {"id": 5, "nome": "Hotel Estrela"}
]

@app.get("/hoteis/")
async def listar_hoteis(
    skip: int = Query(0, description="Número de registros a serem pulados (para paginação)"),
    limit: int = Query(2, description="Número máximo de registros retornados por página")
):
    return hoteis[skip : skip + limit]

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_18.aula_18a:app --reload

'''
skip → inicie exibição dos itens a partir do item escolhido
limit → limita quantidade de item exibido ao usuário

Exemplo de uso:
URL	Resultado
/hoteis?skip=0&limit=2	Retorna os 2 primeiros hotéis
/hoteis?skip=2&limit=2	Retorna os hotéis 3 e 4
/hoteis?skip=4&limit=2	Retorna o hotel 5
'''