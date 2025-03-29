from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import Column, String, Float, Integer, Boolean,create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from passlib.context import CryptContext
from pytz import timezone 

# ======================= CONFIGURAÇÃO SEGURANÇA JWT ==============================
SECRET_KEY = "tMhSB1OGVAQei3NP5Dho6H63_IhTbyPkFlsCwC6L-bE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# =============================== SEGURANÇA =======================================
# Configuração do hash de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para verificar senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Função para obter hash de senha
def get_password_hash(password):
    return pwd_context.hash(password)

# ================================= AUTENTICAÇÃO ====================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Função para autenticar usuário
def authenticate_user(fake_db, username: str, password: str):
    user = fake_db.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

# Gerar Token de acesso 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    sp = timezone('America/Sao_Paulo')
    expire = datetime.now(tz=sp) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
# ============================ DEPENDÊNCIA ========================================

# Dependência para obter usuário atual
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    user = fake_users_db.get(username)
    if user is None:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user
# ========================== CAMINHO ARQUIVO SQLite ===========================

# Conexão SQLite
def sqlite():
    caminho_do_arquivo = Path(__file__).parent
    return f"sqlite:///{caminho_do_arquivo}/meu_hotel.db"

# ======================= CONEXÃO BANCO DE DADOS ===============================
engine = create_engine(sqlite())

# ========================= SESSÃO BANCO DE DADOS ==============================
SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)

# ================= SESSÃO COMMIT (ABERTURA E FECHAMENTO) ======================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==================== MODELAGEM DO BANCO DE DADOS =============================
Base = declarative_base()

# Modelo do Banco de Dados
class HotelModel(Base):
    __tablename__ = "hoteis"
    hotel_id = Column(String(50), primary_key=True)
    nome = Column(String(80), nullable=False)
    estrelas = Column(Float, nullable=True)
    diaria = Column(Float, nullable=True)
    cidade = Column(String(40), nullable=False)

# Modelagem da API
class HotelSchema(BaseModel):
    hotel_id: str
    nome: str
    estrelas: int
    diaria: int
    cidade: str
    
    class Config:
        from_attributes = True

class UsuarioModel(Base):
    # ESCOPO BANCO DE DADOS
    __tablename__ = 'usuarios'
    usuario_id = Column(Integer, primary_key = True, autoincrement=True) # id auto incrementado
    login = Column(String(40), nullable=False, unique=True)
    senha = Column(String(40), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    ativado =  Column(Boolean, default=False)
    '''banco.Model é equivalente a declarative_base() do SQLAlchemy'''

# Modelagem da API
class UsuarioSchema(BaseModel):
    usuario_id: int
    login: str
    email: str    
    class Config:
        from_attributes = True

class UsuarioSegredoSchema(UsuarioSchema):
    usuario_id: int
    login: str
    senha: str 
    email: str
    ativado: bool  

# ===============  CRIAR TABELA APOS MODELAGEM  =======================
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
# Rota de login
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoints protegidos
@app.get("/hoteis", dependencies=[Depends(get_current_user)])
def get_hoteis(db: Session = Depends(get_db)):
    return db.query(HotelModel).all()

@app.post("/hotel/{hotel_id}", status_code=status.HTTP_201_CREATED, response_model=HotelSchema, dependencies=[Depends(get_current_user)])
def post_hotel(hotel_id: str, dados: HotelSchema, db: Session = Depends(get_db)):
    if db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first():
        raise HTTPException(status_code=400, detail="Hotel já existe.")
    novo_hotel = HotelModel(**dados.model_dump())
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
