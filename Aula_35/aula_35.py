# ========================== CAMINHO ARQUIVO SQLite (config.py) ===========================
from pathlib import Path

caminho_do_arquivo = Path(__file__).parent
DB_URL: str = f"sqlite+aiosqlite:///{caminho_do_arquivo}/cadastro.db"

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

# ================= SESSÃO COMMIT (ABERTURA E FECHAMENTO) ======================
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()

# ==================== MODELAGEM DO BANCO DE DADOS (models e schemas) ==========================
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional, List

class PessoaModel(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    senha = Column(String(128), nullable=False)
    ativo = Column(Boolean, default=True)

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

# # Formulário Personalizado: OAuth2PasswordRequestForm
# from fastapi import Form

# # Formulário Personalizado para autenticação (POST / http://127.0.0.1:8000/usuario/login)
# class Formulario_Login_Usuario:
#     def __init__(
#         self,
#         email: str = Form(..., description="E-mail do usuário"), # Form(...) → campo obrigatório.
#         senha: str = Form(..., description="Senha do usuário") # Form(...) → campo obrigatório.
#     ):
#         self.email = email
#         self.senha = senha

# --------------------------- AUTENTICAR USUÁRIO E SENHA (auth.py) ----------------------------------
# Autentica senha e usuário por e-mail
async def autenticar(cpf: str, senha: str, db: AsyncSession) -> Optional[PessoaModel]:
    async with db as session:
        query = select(PessoaModel).filter(PessoaModel.cpf == cpf) # Filtra
        result = await session.execute(query) # Executa Banco de Dados
        usuario: PessoaModel = result.scalars().unique().one_or_none() # Extrai

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

# class auxiliar para identificação do id do usuário (PessoaModel.id)
class TokenData(BaseModel):
    username: Optional[int] = None

# Dependência (VERIFICAR SENHA E USUÁRIO)
async def get_current_user(db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_schema)) -> PessoaModel: # type: ignore
   
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
        query = select(PessoaModel).filter(PessoaModel.usuario_id == int(token_data.username)) # Filtro
        result = await session.execute(query) # Executar Banco de Dados
        usuario: PessoaModel = result.scalars().unique().one_or_none() # Extrair

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

# =================================== ENDPOINTS =======================================
# ========================== CRUD USUÁRIOS (usuario.py) ===============================

from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy import select
from contextlib import asynccontextmanager
from typing import Generator, List

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# ----------------- ROTAS -----------------

# 1. Rota para exibir todos os usuários
@app.get("/")
async def read_all(request: Request, db: SessionLocal  = Depends(get_db)):

    # 1. Buscar todas as pessoas no banco de dados
    result = await db.execute(select(PessoaModel))

    pessoas: List[PessoaModel] = result.scalars().all()

    # 2. Criar o contexto para o template
    context = {
        "request": request,
        # O nome 'pessoas' corresponde à variável usada no seu index.html
        "pessoas": pessoas
    }

    return templates.TemplateResponse('index.html', context=context)

# 2. Rota para criar um novo usuário
@app.get("/create")
def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/create")
async def create_pessoa(request: Request, db: AsyncSession = Depends(get_db)
):

    # Obter dados do formulário
    form = await request.form()
    nome: str = form.get("nome")
    idade: int = form.get("idade")
    cpf: str = form.get("cpf")
    senha: str = form.get("senha")
    hash_senha: str =  gerar_hash_senha(senha=senha) # Gera o hash da senha

    
    # 🔍 Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        raise HTTPException(status_code=400, detail="CPF deve ter exatamente 11 dígitos")

    # 🔍 Verifica se o CPF já existe
    result = await db.execute(select(PessoaModel).filter(PessoaModel.cpf == cpf))
    existente = result.scalars().first()

    if existente:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")

    try:
        # ➕ Cria nova pessoa
        nova = PessoaModel(nome=nome, idade=idade, cpf=cpf, senha=hash_senha)
        db.add(nova)
        await db.commit()
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=f"{e.__class__.__name__}: {e.orig}")

    # 🔁 Redireciona após sucesso
    return RedirectResponse("/", status_code=303)

# 3. Rota para editar um usuário
@app.get("/edit/{pessoa_id}")
async def edit_form(request: Request, pessoa_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PessoaModel).filter(PessoaModel.id == pessoa_id))
    pessoa = result.scalars().first()
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return templates.TemplateResponse("edit.html", {"request": request, "pessoa": pessoa})


@app.post("/edit/{pessoa_id}")
async def edit_pessoa(
    pessoa_id: int,
    nome: str = Form(...),
    idade: int = Form(...),
    cpf: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    # 🔍 Busca a pessoa
    result = await db.execute(select(PessoaModel).filter(PessoaModel.id == pessoa_id))
    pessoa = result.scalars().first()
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    # 🔍 Validação do CPF
    if len(cpf) != 11:
        raise HTTPException(status_code=400, detail="CPF deve ter exatamente 11 dígitos")

    if pessoa.cpf != cpf:
        result = await db.execute(select(PessoaModel).filter(PessoaModel.cpf == cpf))
        if result.scalars().first():
            raise HTTPException(status_code=400, detail="CPF já cadastrado")
        pessoa.cpf = cpf

    # ✏️ Atualiza dados
    pessoa.nome = nome
    pessoa.idade = idade

    try:
        await db.flush()
        await db.commit()
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro de integridade: {e.orig}")

    return RedirectResponse("/", status_code=303)

# 4. Rota para deletar um usuário
@app.get("/delete/{pessoa_id}")
async def delete_pessoa(pessoa_id: int, db: SessionLocal = Depends(get_db), pessoa_logada: PessoaModel = Depends(get_current_user)):

    # 1. Busca a pessoa corretamente
    result = await db.execute(select(PessoaModel).filter(PessoaModel.id == pessoa_id)).filter(pessoa_id == pessoa_logada.id)
    pessoa = result.scalars().first()

    # 2. Verifica se existe
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    # 3. Deleta e confirma
    await db.delete(pessoa)
    await db.commit()

    # 4. Redireciona de volta
    return RedirectResponse("/", status_code=303)

# Página de login
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "erro": None})

# Login (POST)
@app.post("/login")
async def login(
    request: Request,
    cpf: str = Form(...),
    senha: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    usuario = await autenticar(cpf=cpf, senha=senha, db=db)
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Dados de acesso incorretos.'
        )
    
    # 🧠 Cria o token JWT
    token = criar_token_acesso(sub=usuario.id)

    request.session["usuario"] = usuario.nome
    request.session["access_token"] = token  # <-- token salvo na sessão

    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

# 5. Rota de logout
@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=303)

# =================== INSTANCIAR FASTAPI (main.py) ========================
if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_35.aula_35:app --reload
# http://127.0.0.1:8000/docs#/default/converter_converter__from_currency__get