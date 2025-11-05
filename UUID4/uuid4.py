from pydantic import BaseModel, UUID4
from uuid import uuid4

# Modelo Pydantic que usa UUID4
class Item(BaseModel):
    id: UUID4
    nome: str

# Gerando um item novo
novo_item = Item(id=uuid4(), nome="Exemplo_01")
print(novo_item)

# Gerando um item novo
novo_item = Item(id=uuid4(), nome="Exemplo_02")
print(novo_item)