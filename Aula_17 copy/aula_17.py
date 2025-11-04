# ========================== CAMINHO ARQUIVO SQLite (config.py) ===========================
from pathlib import Path

caminho_do_arquivo = Path(__file__).parent
DB_URL: str = f"sqlite+aiosqlite:///{caminho_do_arquivo}/meu_hotel.db"

# ======================= CONEXÃO BANCO DE DADOS (config.py) ============================
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine: AsyncEngine = create_async_engine(DB_URL, echo=False)

Base = declarative_base() # (config.py)

# ========================= SESSÃO BANCO DE DADOS (config.py) ============================
SessionLocal = AsyncSession = sessionmaker(
    autocommit=False, # não faz "commit" automaticamente
    autoflush=False, # não executar consulta automáticas 
    expire_on_commit=False, # sessão não aspirá apos "commit"
    class_=AsyncSession, #  sessão assíncrono
    bind=engine # ativa conexão com o banco de dados
)

# Função get_db para retornar a sessão de banco de dados

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()

# ==================== MODELAGEM DO BANCO DE DADOS (models e schemas) ==========================
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional, List

class HotelModel(Base): # BANCO DE DADOS (models)
    __tablename__ = "hoteis"
    hotel_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80), nullable=False, unique=True)
    cidade = Column(String(40), nullable=False)
    hotel_usuario_id = Column(Integer, ForeignKey('usuarios.usuario_id')) # Chave estrangeira
    criador = relationship("UsuarioModel", back_populates='usuario_hotel', lazy='joined') # relacionamento

class HotelSchema(BaseModel): # MODELAGEM API (schemas)
    hotel_id: Optional[int] = None
    nome: Optional[str] = None
    cidade: Optional[str] = None
    hotel_usuario_id: Optional[int] = None    

    class Config:
        from_attributes = True

class UsuarioModel(Base): # BANCO DE DADOS (models)
    __tablename__ = 'usuarios'
    usuario_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(40), nullable=False, unique=True)
    senha = Column(String(40), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    ativado =  Column(Boolean, default=False)
    usuario_hotel = relationship("HotelModel", cascade="all, delete-orphan", back_populates="criador", uselist=True, lazy="joined") # relacionamento

class UsuarioSchema(BaseModel): # MODELAGEM API (schemas)
    usuario_id: Optional[int] = None
    nome: str
    senha: str
    email: EmailStr
    ativado: Optional[bool] = False 

    class Config:
        from_attributes = True
    
# Atualizar usuário
class UsuarioSchemaUp(BaseModel): # MODELAGEM API (schemas)
    nome: Optional[str] = None
    senha: Optional[str] = None
    email: Optional[EmailStr] = None
    ativado: Optional[bool] = None

    class Config:
        from_attributes = True

# ================================ CONFIGURAÇÃO AUTENTICAÇÃO ===========================================
#=======================================================================================================

# ---------------------- CONFIGURAÇÃO SEGURANÇA JWT (config.py) -------------------------------
SECRET_KEY = "tMhSB1OGVAQei3NP5Dho6H63_IhTbyPkFlsCwC6L-bE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Tempo de expiração do token (minutos)

# ----------------------- CRIPTOGRAFIA DE TEXTO SENHA PARA AUTENTICAÇÃO (security.py) --------------------------------
from passlib.context import CryptContext

# Configuração do hash de senha
CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Função para verificar senha (TEXTO SENHA CRIPTOGRAFADA) Vs (TEXTO SENHA DIGITADO PELO USUÁRIO)
def verificar_senha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

# Função para obter hash de senha (TEXTO SENHA CRIPTOGRAFADA)
def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)

# --------------------------- ROTA DE AUTENTICAÇÃO TOKEN DE ACESSO (auth.py) ----------------------------------
from fastapi.security import OAuth2PasswordBearer

# Endpoint para autenticação token (rota)
oauth2_schema = OAuth2PasswordBearer(tokenUrl=f"usuarios/login")

# Formulário Personalizado: OAuth2PasswordRequestForm
from fastapi import Form

# Formulário Personalizado para autenticação (POST / http://127.0.0.1:8000/usuario/login)
class Formulario_Login_Usuario:
    def __init__(
        self,
        email: str = Form(..., description="E-mail do usuário"), # Form(...) → campo obrigatório.
        senha: str = Form(..., description="Senha do usuário") # Form(...) → campo obrigatório.
    ):
        self.email = email
        self.senha = senha



# --------------------------- AUTENTICAR USUÁRIO E SENHA (auth.py) ----------------------------------
# Autentica senha e usuário por e-mail
async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email) # Filtra
        result = await session.execute(query) # Executa Banco de Dados
        usuario: UsuarioModel = result.scalars().unique().one_or_none() # Extrai

        # Se usuário não existir
        if not usuario:
            return None

        # Se senha não existir |  verificar_senha(senha envia, senha do banco)
        if not verificar_senha(senha, usuario.senha): # security
            return None

        return usuario

# --------------------------- CRIAR TOKEN DE ACESSO (auth.py) ----------------------------------
from datetime import datetime, timedelta
from jose import JWTError, jwt
from pytz import timezone

# Função (CRIAR TOKEN JWT)
def criar_token_acesso(sub: str) -> str:

    # https://jwt.io
    
    payload = {} # O payload é um dicionário que contém informações sobre o token, de acordo com o padrão JWT

    sp = timezone('America/Sao_Paulo') # Horário Global de São Paulo

    # expira = hora SP + conf_db.py(ACCESS_TOKEN_EXPIRE_MINUTES)
    expira = datetime.now(tz=sp) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Campo de autenticação (https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3)

    payload["type"] = 'access_token' # Pode ser "access" (token de acesso) ou "refresh" (token de renovação).

    payload["exp"] = expira # Define a data e hora de expiração do token.

    payload["iat"] = datetime.now(tz=sp) # Representa o horário que o token foi criado

    payload["sub"] = str(sub) # Define o identificador do usuário (geralmente o ID ou nome do usuário autenticado)

    # biblioteca(Dicionário, conf_db.py(JWT_SECRET), algorithm=conf_db.py(ALGORITHM))
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM) # Codificar autenticação JWT

# ---------------------------- VERIFICAÇÃO DE USUÁRIO ATUAL (deps.py) ----------------------------------------
from fastapi import status, Depends, HTTPException, Response

# class auxiliar para identificação do id do usuário (UsuarioModel.id)
class TokenData(BaseModel):
    username: Optional[int] = None

# Dependência (VERIFICAR SENHA E USUÁRIO)
async def get_current_user(db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_schema)) -> UsuarioModel: # type: ignore
   
    # Exceção ...
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possível autenticar a credencial',
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decodificar autenticação JWT
        payload = jwt.decode(
            token, # Senha do Banco de Dados
            SECRET_KEY, # conf_db.py(JWT_SECRET) | Chave
            algorithms=[ALGORITHM], # Algorithm=conf_db.py(ALGORITHM) | hashing 
            options={"verify_aud": False} # Parâmetro extra não obrigatório
        )

        # Buscar Token decodificada (no campo "sub" do token)
        username: str = payload.get("sub")

        # Se Token não existir
        if username is None:
            raise credential_exception # Exceção ...

        # Comparar Token
        token_data: TokenData = TokenData(username=username)

    except JWTError:
        raise credential_exception # Exceção ...

    # Buscar Id de usuário no Banco de Dados é o mesmo que Token decodificado
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.usuario_id == int(token_data.username)) # Filtro
        result = await session.execute(query) # Executar Banco de Dados
        usuario: UsuarioModel = result.scalars().unique().one_or_none() # Extrair

        # Se usuário não existir no Banco de Dados
        if usuario is None:
            raise credential_exception # Exceção ...

        return usuario
# =========================== FIM DA CONFIGURAÇÃO AUTENTICAÇÃO =========================================
#=======================================================================================================

# =================== INSTANCIAR FASTAPI (main.py) ========================
from fastapi import FastAPI
app = FastAPI()
# Função para criar a tabela, chamada no evento de inicialização

# rota (home)
@app.get('/', description='Retorna uma mensagem', summary='Documento', tags=["Documentação"])
async def index(): # recurso GET
   return "http://127.0.0.1:8000/docs"

'''
# GERENCIADOR DE ROTAS (api.py)
# ETAPA INTEGRADA NESTE PROJETO

from config import settings (configuração de modulo interno "config.py")
from routes import api_router (configuração de modulo interno "api.py")

app.include_router(api_router, prefix=settings.API_V1_STR)
'''
# ========================== GERENCIADOR DE ROTAS (api.py) ==========================

'''
# ENDPOINTS
# ETAPA INTEGRADA NESTE PROJETO

from endpoints import usuario (configuração de modulo interno "usuario.py")
from endpoints import hotel (configuração de modulo interno "hotel.py")

# APIRouter é uma classe usada para organizar e modularizar as rotas da aplicação
from fastapi import APIRouter
api_router = APIRouter() # roteador


api_router.include_router(usuario.router, prefix='/usuarios', tags=['usuarios']) # rota
api_router.include_router(hotel.router, prefix='/hoteis', tags=['hoteis']) # rota
'''

# =================================== ENDPOINTS =======================================
# ========================== CRUD USUÁRIOS (usuario.py) ===============================

from fastapi import status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

# GET / http://127.0.0.1:8000/usuario/usuarios
@app.get("/usuario/usuarios", response_model=list[UsuarioSchema], tags=['usuario'])
async def list_usuarios(db: SessionLocal = Depends(get_db)):

    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List[UsuarioSchema] = result.scalars().unique().all() # Encapsular em lista todos os usuários

        return usuarios
    
# GET / http://127.0.0.1:8000/usuario/id
@app.get('/usuario/{usuario_id}', response_model=UsuarioSchema, status_code=status.HTTP_200_OK, tags=['usuario'])
async def get_usuario(usuario_id: int, db: SessionLocal = Depends(get_db)):
   
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.usuario_id == usuario_id)
        result = await session.execute(query)
        usuario: UsuarioSchema = result.scalars().unique().one_or_none()

        if usuario:
            return usuario
        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)

# POST / http://127.0.0.1:8000/usuario/cadastro
@app.post('/usuario/cadastro', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchema, tags=['usuario'])
async def post_usuario(usuario: UsuarioSchema, db: SessionLocal = Depends(get_db)):

    # Adicionar no Banco de Dados
    novo_usuario: UsuarioModel = UsuarioModel(nome=usuario.nome, 
                                              senha=gerar_hash_senha(usuario.senha),
                                              email=usuario.email,             
                                              ativado=usuario.ativado)
    
    async with db as session:
        try:
            session.add(novo_usuario)
            await session.commit()
            return novo_usuario
        
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Já existe um usuário com este email cadastrado.')

# POST / http://127.0.0.1:8000/usuario/login
@app.post(
    '/usuario/login',
    tags=['usuario'],
    summary='Autenticação de usuários',
    description='senha criptografada = nome do usuário',
)
async def login_usuario(formulario_de_inf: Formulario_Login_Usuario = Depends(), db: SessionLocal = Depends(get_db)):

    usuario = await autenticar(email=formulario_de_inf.email, senha=formulario_de_inf.senha, db=db)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Dados de acesso incorretos.'
        )

    return JSONResponse(
        content={"access_token": criar_token_acesso(sub=usuario.usuario_id), "token_type": "bearer"},
        status_code=status.HTTP_200_OK
    )

'''
# Trocado pelo "Formulario_Login_Usuario" acima
@app.post('/usuario/login', 
          tags=['usuario'],
          summary='Autenticação de usuários',
          description='[username = email, password = senha do usuário]',
          response_model= UsuarioSchema,
          response_description='Autenticação de usuários'
          )
async def login_usuario(formulario_de_inf: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)):

    
    usuario = await autenticar(email=formulario_de_inf.username, senha=formulario_de_inf.password, db=db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Dados de acesso incorretos.')

    return JSONResponse(content={"access_token": criar_token_acesso(sub=usuario.usuario_id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)
'''

# PUT / http://127.0.0.1:8000/usuario/id
@app.put("/usuario/{usuario_id}", response_model=UsuarioSchemaUp, tags=['usuario'])
async def update_usuario(usuario_id: int, usuario: UsuarioSchemaUp, db: SessionLocal = Depends(get_db), usuario_logado: UsuarioModel = Depends(get_current_user)):

    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.usuario_id == usuario_id).filter(
                                            usuario_logado.usuario_id == usuario_id)
        result = await session.execute(query)
        usuario_up: UsuarioSchemaUp = result.scalars().unique().one_or_none()

        if not usuario_up:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        if usuario_up:
            if usuario.nome:
                usuario_up.nome = usuario.nome
            if usuario.senha: 
                usuario_up.senha = gerar_hash_senha(usuario.senha)  # Atualizando senha com hash
            if usuario.email:
                usuario_up.email = usuario.email
            if usuario.ativado is not None:
                usuario_up.ativado = usuario.ativado

            try: 
                await session.commit()
                return usuario_up
            except IntegrityError:
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                    detail='Já existe um usuário com este email cadastrado.')
        
# 4. Excluir / http://127.0.0.1:8000/usuario/id
@app.delete("/usuario/{usuario_id}", tags=['usuario'])
async def delete_usuario(usuario_id: int, db: SessionLocal = Depends(get_db), usuario_logado: UsuarioModel = Depends(get_current_user)):

    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.usuario_id == usuario_id).filter(
                                                         usuario_id == usuario_logado.usuario_id)
        result = await session.execute(query)
        usuario_del: UsuarioSchema = result.scalars().unique().one_or_none()
            
        if usuario_del:
            await session.delete(usuario_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)

# =================================== ENDPOINTS =======================================
# ========================== CRUD HOTÉIS (hotel.py) ===============================

# GET / http://127.0.0.1:8000/hotel/hoteis
@app.get("/hotel/hoteis", response_model=list[HotelSchema], tags=['hotel'])
async def list_hoteis(db: SessionLocal = Depends(get_db)):

    async with db as session:
        query = select(HotelModel)
        result = await session.execute(query)
        hoteis: List[HotelModel] = result.scalars().unique().all() # Encapsular em lista todos os hotéis

        return hoteis
    
# GET / http://127.0.0.1:8000/hotel/id
@app.get('/hotel/{artigo_id}', response_model=HotelSchema, status_code=status.HTTP_200_OK, tags=['hotel'])
async def get_hotel(artigo_id: int, db: SessionLocal = Depends(get_db)):
    async with db as session:
        query = select(HotelModel).filter(HotelModel.hotel_id == artigo_id)
        result = await session.execute(query)
        hotel: HotelModel = result.scalars().unique().one_or_none()

        if hotel:
            return hotel
        else:
            raise HTTPException(detail='Artigo não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)

# POST / http://127.0.0.1:8000/hotel/cadastro
@app.post('/hotel/cadastro', status_code=status.HTTP_201_CREATED, response_model=HotelSchema, tags=['hotel'])
async def post_artigo(hotel: HotelSchema, usuario_logado: UsuarioModel = Depends(get_current_user), db: SessionLocal = Depends(get_db)):
    
    novo_hotel: HotelModel = HotelModel(
                                            nome=hotel.nome, 
                                            cidade=hotel.cidade, 
                                            hotel_usuario_id=usuario_logado.usuario_id # Usando o ID do usuário logado
                                          )
    
    async with db as session:
        try:
            session.add(novo_hotel)
            await session.commit()
            await session.refresh(novo_hotel)
            return novo_hotel
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Nome já cadastrado.')

# PUT / http://127.0.0.1:8000/hotel/id
@app.put("/hotel/{hotel_id}", response_model=HotelSchema,  tags=['hotel'])
async def put_hotel(hotel_id: str, hotel: HotelSchema, db: SessionLocal = Depends(get_db), usuario_logado: UsuarioModel = Depends(get_current_user)):

    async with db as session:
        query = select(HotelModel).filter(HotelModel.hotel_id == hotel_id).filter(
                                          HotelModel.hotel_usuario_id == usuario_logado.usuario_id)
        result = await session.execute(query)
        hotel_up: HotelSchema = result.scalars().unique().one_or_none()

        if not hotel_up:
            raise HTTPException(status_code=404, detail="Hotel não encontrado")
        else:
            if hotel.nome:
                hotel_up.nome = hotel.nome
            if hotel.cidade:
                hotel_up.cidade = hotel.cidade
            if hotel_up.hotel_usuario_id:
                hotel_up.hotel_usuario_id = usuario_logado.usuario_id

            try: 
                await session.commit()
                return hotel_up
            except IntegrityError:
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                    detail='Nome já cadastrado.')
     
# 4. Excluir / http://127.0.0.1:8000/hotel/id
@app.delete("/hotel/{hotel_id}", tags=['hotel'])
async def delete_hotel(hotel_id: int, db: SessionLocal = Depends(get_db), usuario_logado: UsuarioModel = Depends(get_current_user)):

    async with db as session:
        query = select(HotelModel).filter(HotelModel.hotel_id == hotel_id).filter(
                                          HotelModel.hotel_usuario_id == usuario_logado.usuario_id)
        result = await session.execute(query)
        hotel_del: HotelSchema = result.scalars().unique().one_or_none()
            
        if hotel_del:
            await session.delete(hotel_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Hotel não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)

# =================== INSTANCIAR FASTAPI (main.py) ========================
if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_17.aula_17:app --reload