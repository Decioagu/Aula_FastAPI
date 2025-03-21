from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy import Column, String, Float, create_engine, inspect, text, select # Criar Banco de Dados
from sqlalchemy.ext.declarative import declarative_base # Modelagem do Banco de Dados
from sqlalchemy.orm import sessionmaker, Session # Interação no Banco de Dados
from pathlib import Path # Caminho do Banco de Dados SQLite
from pydantic import BaseModel # Modelagem da API (JSON)

'''OBS: escolha UMA das opções de Banco de dados em:
# =========== CONFIGURAÇÃO BANCO DE DADOS SQL ALCHEMY ===========
# Conexão
# engine = create_engine(sqlite()) # <= Retire do comentário para SQLite
# engine = create_engine(mysql())  # <= Retire do comentário para MySQL

OBS: Apenas UMA opção por vez. 
'''

# =============== CONEXÃO BANCO DE DADOS (SQLITE) ===============
def sqlite():
    # Caminho do banco de dados
    caminho_do_arquivo = Path(__file__).parent
    DATABASE_URL = f"sqlite:///{caminho_do_arquivo}/meu_hotel.db"

    return DATABASE_URL


# =========== CONFIGURAÇÃO BANCO DE DADOS SQL ALCHEMY ===========
# Conexão
engine = create_engine(sqlite()) # <= Retire do comentário para SQLite
# Interação Banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)
# Modelagem Banco de Dados
Base = declarative_base() 

# =================== INICIAR E FECHAR SESSÃO ====================
# Dependência para obter sessão do banco
def get_db():
    with Session(engine) as session:
        yield session

# ================= MODELAGEM DO BANCO DE DADOS ==================
# Modelo do Banco de Dados
class HotelModel(Base):
    __tablename__ = "hoteis"
    hotel_id = Column(String(50), primary_key=True)
    nome = Column(String(80), nullable=False)
    estrelas = Column(Float, nullable=True)
    diaria = Column(Float, nullable=True)
    cidade = Column(String(40), nullable=False)

    model_config = {
        "from_attributes": True  # Necessário no Pydantic v2
    }

# ================== MODELAGEM DA API (JSON) ====================
# Modelagem (API)
class HotelSchema(BaseModel):
    hotel_id: str
    nome: str
    estrelas: int
    diaria: int
    cidade: str
    
    class Config:
        from_attributes = True

# ======================================  CRIAR TABELA APOS MODELAGEM  =======================================
def tabela_existe(engine) -> bool:
    inspetor = inspect(engine)
    # Obtendo o nome gerado automaticamente pelo SQLModel (baseado no nome da classe)
    nome_tabela = HotelModel.__tablename__ if hasattr(HotelModel, "__tablename__") else HotelModel.__name__.lower()

    if not inspetor.has_table(nome_tabela):
        print(f'A tabela "{nome_tabela}" NÃO existe.')
        print(f"🔹 Criando a tabela '{nome_tabela}'...")
        Base.metadata.create_all(engine)
    else:
        print(f"✅ A tabela '{nome_tabela}' já existe.")

# Verifica a existência de tabela
tabela_existe(engine)

# =================== INSTANCIAR FASTAIP ========================
# Instância do FastAPI
app = FastAPI()

# ========================== CRUD ===============================
# rota
@app.get('/')
async def get_site():
    return 'http://127.0.0.1:8000/docs'

# Endpoints
@app.get("/hoteis")
def get_hoteis(db: Session = Depends(get_db)):
    query = select(HotelModel)
    hoteis = db.execute(query)  # Executa a consulta
    return hoteis.scalars().all()  # Retorna a lista de usuários

    # hoteis = db.query(HotelModel).all()
    return hoteis

@app.get("/hotel/{hotel_id}")
def get_hotel(hotel_id: str, db: Session = Depends(get_db)):
    hotel = db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
    if hotel:
        return hotel
    raise HTTPException(status_code=404, detail="Hotel não encontrado")

@app.post("/hotel/{hotel_id}", status_code=status.HTTP_201_CREATED, response_model=HotelSchema)
def post_hotel(hotel_id: str, dados: HotelSchema, db: Session = Depends(get_db)):
    
    hotel = db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()

    if hotel:
        raise HTTPException(status_code=400, detail="Hotel já existe.")
    
    # (**dados.model_dump() = HotelSchema): dicionário e o desempacota diretamente no modelo do banco
    novo_hotel = HotelModel(**dados.model_dump())
    db.add(novo_hotel)
    db.commit()

    return novo_hotel

@app.put("/hotel/{hotel_id}", response_model=HotelSchema)
def put_hotel(hotel_id: str, dados: HotelSchema, db: Session = Depends(get_db)):
    hotel = db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
    if hotel:
        hotel.nome = dados.nome
        hotel.estrelas = dados.estrelas
        hotel.diaria = dados.diaria
        hotel.cidade = dados.cidade

        db.commit()
        return hotel
    else:
            raise HTTPException(detail='Curso não encontrado.', status_code=404)

@app.delete("/hotel/{hotel_id}")
def delete_hotel(hotel_id: str, db: Session = Depends(get_db)):
    hotel = db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
    if hotel:
        db.delete(hotel)
        db.commit()
        return {"mensagem": "Hotel deletado com sucesso"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hotel não encontrado")

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_11.aula_11:app --reload
