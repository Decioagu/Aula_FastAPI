# Seção 3 (FastAPI - APIs Modernas e Assíncronas com Python)
from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel, field_validator
from typing import Optional


# modelagem e validação tipo (tratamento de entrada do usuário)
class Hotel(BaseModel): # Para o uso das funções Post e Put
    # (modelo: tipo = valor)
    hotel_id: str
    nome: str
    estrelas: Optional[float] = None
    diaria: Optional[float] = None
    cidade: str

    '''
    O módulo "field_validator" oferece uma ferramenta poderosa para personalizar
    validações complexas e específicas para atender às suas necessidades.
    '''
    @field_validator('estrelas')
    @classmethod
    def validacao_estrela(cls, valor_valido):
        # Verifica se o valor de idade é positivo
        if not (0 <= valor_valido <= 5):
            raise ValueError('<========> estrelas: deve ser entre 0 e 5 <========> \n')
        return valor_valido
    
    @field_validator('diaria')
    @classmethod
    def validacao_diaria(cls, valor_valido):
        # Verifica se o valor de idade é positivo
        if not (0 <= valor_valido):
            raise ValueError('<========> diária: deve ser maior que 0 <========> \n')
        return valor_valido


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
app = FastAPI(title='Aula 03', version='0.0.3', description= 'Alua 21 e 23')

# rota (mensagem na home da documentação)
@app.get('/', description='Retorna uma mensagem', summary='Mensagem', tags=["Documentação"] )
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

# Subir o servidor: uvicorn Aula_03.aula_03:app --reload 