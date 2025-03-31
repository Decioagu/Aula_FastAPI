from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import Column, String, Float, Integer, Boolean, create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from passlib.context import CryptContext
from pytz import timezone

# ======================= CONFIGURAÇÃO SEGURANÇA JWT (CONFIG) ==============================
SECRET_KEY = "tMhSB1OGVAQei3NP5Dho6H63_IhTbyPkFlsCwC6L-bE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ======================= MODELO DE AUTENTICAÇÃO (SECURITY) ================================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para verificar senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Função para obter hash de senha
def get_password_hash(password):
    return pwd_context.hash(password)

# ========================== VERIFICAR (DEPENDÊNCIA) =====================================
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    user = db.query(UsuarioModel).filter(UsuarioModel.login == username).first()  # Alterado para usar o banco de dados real
    if user is None:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user

# ========================== CAMINHO ARQUIVO SQLite ===========================
def sqlite():
    caminho_do_arquivo = Path(__file__).parent
    return f"sqlite:///{caminho_do_arquivo}/meu_hotel.db"

# ======================= CONEXÃO BANCO DE DADOS ============================
engine = create_engine(sqlite())

# ========================= SESSÃO BANCO DE DADOS ============================
SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)

# Função get_db para retornar a sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==================== MODELAGEM DO BANCO DE DADOS ==========================
Base = declarative_base()

class HotelModel(Base):
    __tablename__ = "hoteis"
    hotel_id = Column(String(50), primary_key=True)
    nome = Column(String(80), nullable=False)
    estrelas = Column(Float, nullable=True)
    diaria = Column(Float, nullable=True)
    cidade = Column(String(40), nullable=False)

class HotelSchema(BaseModel):
    hotel_id: str
    nome: str
    estrelas: int
    diaria: int
    cidade: str
    
    class Config:
        from_attributes = True

class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    usuario_id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(40), nullable=False, unique=True)
    senha = Column(String(40), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    ativado =  Column(Boolean, default=False)

class UsuarioSchema(BaseModel):
    usuario_id: int
    login: str
    email: str    
    class Config:
        from_attributes = True

class UsuarioSegredoSchema(UsuarioSchema):
    senha: str
    ativado: bool  

# ================= CRIAR TABELA APOS MODELAGEM ========================
def tabela_existe(engine) -> bool:
    inspetor = inspect(engine)
    nome_tabela = HotelModel.__tablename__ if hasattr(HotelModel, "__tablename__") else HotelModel.__name__.lower()

    if not inspetor.has_table(nome_tabela):
        print(f'A tabela "{nome_tabela}" NÃO existe.')
        print(f"🔹 Criando a tabela '{nome_tabela}'...")
        Base.metadata.create_all(engine)
    else:
        print(f"✅ A tabela '{nome_tabela}' já existe.")

tabela_existe(engine)

# =================== INSTANCIAR FASTAPI ========================
app = FastAPI()

# ========================== CRUD USUÁRIOS ===============================

# 1. Registrar Usuário (Cadastro)
@app.post("/register", response_model=UsuarioSchema)
def register_user(usuario: UsuarioSegredoSchema, db: Session = Depends(get_db)):
    if db.query(UsuarioModel).filter(UsuarioModel.login == usuario.login).first():
        raise HTTPException(status_code=400, detail="Usuário já cadastrado.")
    if db.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    
    hashed_password = get_password_hash(usuario.senha)
    new_user = UsuarioModel(login=usuario.login, senha=hashed_password, email=usuario.email, ativado=usuario.ativado)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 2. Listar Usuários
@app.get("/usuarios", response_model=list[UsuarioSchema], dependencies=[Depends(get_current_user)])
def list_users(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()

# 3. Editar Usuário
@app.put("/usuario/{usuario_id}", response_model=UsuarioSchema, dependencies=[Depends(get_current_user)])
def update_user(usuario_id: int, usuario: UsuarioSegredoSchema, db: Session = Depends(get_db)):
    user = db.query(UsuarioModel).filter(UsuarioModel.usuario_id == usuario_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    user.login = usuario.login
    user.email = usuario.email
    user.senha = get_password_hash(usuario.senha)  # Atualizando senha com hash
    user.ativado = usuario.ativado
    db.commit()
    db.refresh(user)
    return user

# 4. Excluir Usuário
@app.delete("/usuario/{usuario_id}", dependencies=[Depends(get_current_user)])
def delete_user(usuario_id: int, db: Session = Depends(get_db)):
    user = db.query(UsuarioModel).filter(UsuarioModel.usuario_id == usuario_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(user)
    db.commit()
    return {"message": "Usuário excluído com sucesso"}

# ========================== CRUD HOTEIS ===============================

@app.get("/hoteis", dependencies=[Depends(get_current_user)])
def get_hoteis(db: Session = Depends(get_db)):
    return db.query(HotelModel).all()

@app.post("/hotel/{hotel_id}", status_code=status.HTTP_201_CREATED, response_model=HotelSchema, dependencies=[Depends(get_current_user)])
def post_hotel(hotel_id: str, dados: HotelSchema, db: Session = Depends(get_db)):
    if db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first():
        raise HTTPException(status_code=400, detail="Hotel já existe.")
    novo_hotel = HotelModel(**dados.dict())  # Utilizando dados.dict() para converter o Pydantic model
    db.add(novo_hotel)
    db.commit()
    return novo_hotel

@app.put("/hotel/{hotel_id}", response_model=HotelSchema, dependencies=[Depends(get_current_user)])
def put_hotel(hotel_id: str, dados: HotelSchema, db: Session = Depends(get_db)):
    hotel = db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
    if hotel:
        hotel.nome = dados.nome
        hotel.estrelas = dados.estrelas
        hotel.diaria = dados.diaria
        hotel.cidade = dados.cidade
        db.commit()
        return hotel
    raise HTTPException(status_code=404, detail='Hotel não encontrado.')

@app.delete("/hotel/{hotel_id}", dependencies=[Depends(get_current_user)])
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

# uvicorn TESTE:app --reload