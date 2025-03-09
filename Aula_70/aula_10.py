from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, String, Float, create_engine # Banco de Dados
from sqlalchemy.ext.declarative import declarative_base # Banco de Dados
from sqlalchemy.orm import sessionmaker, Session # Banco de Dados
from pathlib import Path
from typing import Dict


# Caminho do banco de dados
caminho_do_arquivo = Path(__file__).parent
DATABASE_URL = f"sqlite:///{caminho_do_arquivo}/banco.db"

# Configuração do SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # Conexão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Interação Banco
Base = declarative_base() # Modelagem Banco de Dados

# Modelo do Banco de Dados
class HotelModel(Base):
    __tablename__ = "hoteis"
    hotel_id = Column(String, primary_key=True)
    nome = Column(String(80), nullable=False)
    estrelas = Column(Float, nullable=True)
    diaria = Column(Float, nullable=True)
    cidade = Column(String(40), nullable=False)

    model_config = {
        "from_attributes": True  # Necessário no Pydantic v2
    }

    def json(self):
        return {
            "hotel_id": self.hotel_id,
            "nome": self.nome,
            "estrelas": self.estrelas,
            "diaria": self.diaria,
            "cidade": self.cidade,
        }
    
modelo ={
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
        }

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Instância do FastAPI
app = FastAPI()

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# rota
@app.get('/')
async def get_site():
    return 'http://127.0.0.1:8000/docs'

# Endpoints
@app.get("/hoteis")
def get_hoteis(db: Session = Depends(get_db)):
    hoteis = db.query(HotelModel).all()
    return {"hoteis": [hotel.json() for hotel in hoteis]}

@app.get("/hotel/{hotel_id}")
def get_hotel(hotel_id: str, db: Session = Depends(get_db)):
    hotel = db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
    if hotel:
        return hotel.json()
    raise HTTPException(status_code=404, detail="Hotel não encontrado")

@app.post("/hotel/{hotel_id}", status_code=201)
def post_hotel(hotel_id: str, dados: dict, db: Session = Depends(get_db)):
    hotel = db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
    if hotel:
        raise HTTPException(status_code=400, detail="Hotel já existe.")
    novo_hotel = HotelModel(hotel_id=hotel_id, **dados)
    db.add(novo_hotel)
    db.commit()
    return novo_hotel.json()

@app.put("/hotel/{hotel_id}")
def put_hotel(hotel_id: str, dados: dict, db: Session = Depends(get_db)):
    hotel = db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
    if hotel:
        for key, value in dados.items():
            setattr(hotel, key, value)
    else:
        hotel = HotelModel(hotel_id=hotel_id, **dados)
        db.add(hotel)
    db.commit()
    return hotel.json()

@app.delete("/hotel/{hotel_id}")
def delete_hotel(hotel_id: str, db: Session = Depends(get_db)):
    hotel = db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
    if hotel:
        db.delete(hotel)
        db.commit()
        return {"mensagem": "Hotel deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Hotel não encontrado")

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_10.aula_10:app --reload
