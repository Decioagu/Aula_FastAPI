from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    em_oferta: bool = False

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int

    class Config:
        orm_mode = True
