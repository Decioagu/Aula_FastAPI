from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rota inicial
@app.get('/')
async def index():
    return {"msg": "Décio Santana de Aguiar"}

# Rota para buscar produto por ID
@app.get('/produtos/{id}', response_model=schemas.Produto)
async def buscar_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(models.Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

# Rota para atualizar produto por ID
@app.put('/produtos/{id}', response_model=schemas.Produto)
async def atualizar_produto(id: int, produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    produto_db = db.query(models.Produto).filter(models.Produto.id == id).first()
    if not produto_db:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto_db.nome = produto.nome
    produto_db.preco = produto.preco
    produto_db.em_oferta = produto.em_oferta

    db.commit()
    db.refresh(produto_db)
    return produto_db


# 🚀 Rota POST para adicionar um novo produto
@app.post('/produtos', response_model=schemas.Produto, status_code=201)
async def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = models.Produto(
        nome=produto.nome,
        preco=produto.preco,
        em_oferta=produto.em_oferta
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto