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

# Função get_db para retornar a sessão de banco de dados

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

class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    
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
from fastapi.responses import RedirectResponse
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
    result = await db.execute(select(Pessoa))

    pessoas: List[Pessoa] = result.scalars().all()

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
async def create_pessoa(
    nome: str = Form(...),
    idade: int = Form(...),
    cpf: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    
    # 🔍 Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        raise HTTPException(status_code=400, detail="CPF deve ter exatamente 11 dígitos")

    # 🔍 Verifica se o CPF já existe
    result = await db.execute(select(Pessoa).filter(Pessoa.cpf == cpf))
    existente = result.scalars().first()

    if existente:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")

    try:
        # ➕ Cria nova pessoa
        nova = Pessoa(nome=nome, idade=idade, cpf=cpf)
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
    result = await db.execute(select(Pessoa).filter(Pessoa.id == pessoa_id))
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
    result = await db.execute(select(Pessoa).filter(Pessoa.id == pessoa_id))
    pessoa = result.scalars().first()
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    # 🔍 Validação do CPF
    if len(cpf) != 11:
        raise HTTPException(status_code=400, detail="CPF deve ter exatamente 11 dígitos")

    if pessoa.cpf != cpf:
        result = await db.execute(select(Pessoa).filter(Pessoa.cpf == cpf))
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
async def delete_pessoa(pessoa_id: int, db: SessionLocal = Depends(get_db)):
    # ✅ 1. Busca a pessoa corretamente
    result = await db.execute(select(Pessoa).filter(Pessoa.id == pessoa_id))
    pessoa = result.scalars().first()

    # ✅ 2. Verifica se existe
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    # ✅ 3. Deleta e confirma
    await db.delete(pessoa)
    await db.commit()

    # ✅ 4. Redireciona de volta
    return RedirectResponse("/", status_code=303)

# =================== INSTANCIAR FASTAPI (main.py) ========================
if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_34.aula_34:app --reload