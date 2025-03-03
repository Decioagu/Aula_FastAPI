from typing import Optional

from pydantic import BaseModel as SCBaseModel

'''
O "BaseModel" no Pydantic é uma classe base que permite a 
criação de modelos de dados com validação e tipagem automática:
    - Definição de tipos de dados: definir os tipos de dados no modelo como: 
    int, str, bool, float, etc.
    - Validação de dados: valida automaticamente os dados a ser inserido no modelo.
    - Serialização e desserialização: converter seus modelos de dados em diferentes
    formatos como: JSON, XML e CSV.

"Optional" é um tipo genérico que representa um valor que pode ser do tipo especificado ou None
'''
# modelagem e validação tipo
class CursoSchema(SCBaseModel):
    # (modelo: tipo)
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True
