# Seção 3 (FastAPI - APIs Modernas e Assíncronas com Python)
from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
from typing import Optional

'''
"Optional" é um tipo genérico que representa um
valor que pode ser do tipo especificado ou None. 
Ex:
    id: Optional[int] = None
'''

# modelagem e validação tipo (tratamento de entrada do usuário)
class Hotel(BaseModel):
    # (modelo: tipo = valor)
    hotel_id: str
    nome: str
    estrelas: Optional[float] = None
    diaria: Optional[float] = None
    cidade: str

# lista de hotéis (dados hoteis)
hoteis = [
        {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
        },
        {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'Santa Catarina'
        },
        {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'Santa Catarina'
        }
]

# instanciar API (Descrição de documento)
app = FastAPI(title='Aula 02', version='0.0.2', description= 'Alua 10 até 16')

# rota
@app.get('/')
async def get_site():
    return 'http://127.0.0.1:8000/docs'

# rota (Ler todos os dados)
@app.get('/hoteis')
async def get_hoteis(): # CRUD método GET
    return hoteis

# rota (Ler dados Hotel por id)
@app.get('/hoteis/{hotel_id}')
async def get_hotel_por_id(hotel_id: str): # CRUD método GET
    try:
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
    except KeyError:
        # Tratamento de id não existente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Hotel não encontrado')
    
# rota (Criar novo Hotel)
@app.post('/hoteis', status_code=status.HTTP_201_CREATED)
async def post_hotel(hotel: Hotel): # CRUD método POST
    
    # Verificar se já existe um hotel com o mesmo ID
    for h in hoteis:
        if h["hotel_id"] == hotel.hotel_id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Hotel ID já existe")

    hoteis.append(hotel.model_dump())  # Converte o modelo Pydantic para dicionário
    return hotel

# rota (Atualizar novo Hotel por id)
@app.put('/hoteis/{hotel_id}')
async def put_hotel(hotel_id: str, hotel: Hotel): # CRUD método PUT
    for i, h in enumerate(hoteis):
        if h["hotel_id"] == hotel_id:
            hoteis[i] = hotel.model_dump() # Converte o modelo Pydantic para dicionário
            return hotel
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Hotel não encontrado')

    
# rota (Deletar novo Hotel por id)
@app.delete('/hoteis/{hotel_id}')
async def delete_hotel(hotel_id: str): # CRUD método DELETE
    for i, h in enumerate(hoteis):
        if h["hotel_id"] == hotel_id:
            del hoteis[i]
            return Response(content="Hotel deletado com sucesso!!!", status_code=status.HTTP_200_OK)
    else:
        # tratar id inexistente
        raise HTTPException(detail='Hotel não encontrado', status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# Subir o servidor: uvicorn Aula_02.aula_02:app --reload 