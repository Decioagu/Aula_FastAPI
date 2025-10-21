from typing import Optional

from pydantic import BaseModel as SCBaseModel

'''
O "BaseModel" no Pydantic é uma classe base que permite a 
criação de modelos de dados com validação e tipagem.

O "SCBaseModel" neste caso é o apelido para "BaseModel"

"Optional" é um tipo genérico que representa um valor que pode ser do tipo especificado ou None
'''
# Modelagem (API)
class CursoSchema(SCBaseModel):
    # (modelo: tipo)
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int
    
    '''
    O atributo orm_mode = True permite que o Pydantic converta objetos do 
    Banco de Dados no modelos do SQLAlchemy em dicionários compatíveis com JSON.
    '''
    class Config:
        from_attributes = True

# Modelagem (API)
class CursoSchemaSemID(SCBaseModel): # Para POST => Id automático
    # (modelo: tipo)
    titulo: str
    aulas: int
    horas: int
    
    '''
    O atributo "from_attributes = True" permite que o Pydantic converta objetos do 
    Banco de Dados no modelos do SQLAlchemy em dicionários compatíveis com JSON.
    '''
    class Config:
        from_attributes = True
