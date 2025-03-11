from pydantic import BaseModel # criação de modelo 

# Modelagem ("Banco de Dados")
class Produto(BaseModel):
    # (modelo: tipo = valor)
    id: int # validação de tipo
    nome: str # validação de tipo
    preco: float # validação de tipo
    em_oferta: bool = False # validação de tipo

# Lista de produtos
produtos = [
    Produto(id=1, nome='Playstation 5', preco=5745.55, em_oferta=True), # Modelagem 
    Produto(id=2, nome='Nintendo Wii', preco=2654.12), # Modelagem 
    Produto(id=3, nome='Xbox 360', preco=1765.34, em_oferta=True), # Modelagem 
    Produto(id=4, nome='Super Nintendo', preco=234.67), # Modelagem 
    Produto(id=5, nome='Atari 2600', preco=199.90, em_oferta=True), # Modelagem 
]
