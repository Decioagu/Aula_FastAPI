from fastapi import FastAPI, HTTPException, Depends, status
from sqlmodel import SQLModel, Field, Session, create_engine, select
from sqlalchemy import inspect
from pathlib import Path

# ================== CONFIGURAÇÃO BANCO DE DADOS ==================
# Caminho do banco de dados
caminho_do_arquivo = Path(__file__).parent
DATABASE_URL = f"sqlite:///{caminho_do_arquivo}/meu_hotel.db"

# ===================== CRIAR BANCO DE DADOS ======================
# Conexão
engine = create_engine(DATABASE_URL)

# =================== INICIAR E FECHAR SESSÃO ====================
def get_db():
    with Session(engine) as session:
        yield session

# ============= MODELAGEM DO BANCO DE DADOS SQL MODEL =============
class Hotel(SQLModel, table=True):
    hotel_id: str = Field(primary_key=True, max_length=50)
    nome: str = Field(max_length=80)
    estrelas: float | None = None
    diaria: float | None = None
    cidade: str = Field(max_length=40)

# ======================================  CRIAR TABELA APOS MODELAGEM  =======================================
# Função para verificar a existência de uma tabela de forma síncrona
def tabela_existe(engine) -> bool:
    inspetor = inspect(engine)
    # Obtendo o nome gerado automaticamente pelo SQLModel (baseado no nome da classe)
    nome_tabela = Hotel.__tablename__ if hasattr(Hotel, "__tablename__") else Hotel.__name__.lower()

    if not inspetor.has_table(nome_tabela):
        print(f'A tabela "{nome_tabela}" NÃO existe.')
        print(f"🔹 Criando a tabela '{nome_tabela}'...")
        SQLModel.metadata.create_all(engine)
    else:
        print(f"✅ A tabela '{nome_tabela}' já existe.")

# Verifica a existência de tabela
tabela_existe(engine)

# =================== INICIAR FASTAPI ====================
app = FastAPI()

# ========================== CRUD ===============================
@app.get("/")
def get_site():
    return {"docs": "http://127.0.0.1:8000/docs"}

@app.get("/hoteis", response_model=list[Hotel])
def get_hoteis(db: Session = Depends(get_db)):
    return db.exec(select(Hotel)).all()

@app.get("/hotel/{hotel_id}", response_model=Hotel)
def get_hotel(hotel_id: str, db: Session = Depends(get_db)):
    hotel = db.get(Hotel, hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel não encontrado")
    return hotel

@app.post("/hotel/{hotel_id}", status_code=status.HTTP_201_CREATED, response_model=Hotel)
def post_hotel(hotel_id: str, hotel: Hotel, db: Session = Depends(get_db)):
    if db.get(Hotel, hotel_id):
        raise HTTPException(status_code=400, detail="Hotel já existe.")
    db.add(hotel)
    db.commit()
    db.refresh(hotel)
    return hotel

@app.put("/hotel/{hotel_id}", response_model=Hotel)
def put_hotel(hotel_id: str, hotel: Hotel, db: Session = Depends(get_db)):
    db_hotel = db.get(Hotel, hotel_id)
    if not db_hotel:
        raise HTTPException(status_code=404, detail="Hotel não encontrado")
    # .model_dump(): dicionário
    hotel_dict = hotel.model_dump(exclude_unset=True)
    for key, value in hotel_dict.items():
        setattr(db_hotel, key, value)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

@app.delete("/hotel/{hotel_id}")
def delete_hotel(hotel_id: str, db: Session = Depends(get_db)):
    hotel = db.get(Hotel, hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel não encontrado")
    db.delete(hotel)
    db.commit()
    return {"mensagem": "Hotel deletado com sucesso"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_14.aula_14:app --reload