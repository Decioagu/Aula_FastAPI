from typing import Optional

from pydantic import BaseModel as SCBaseModel

'''
O "BaseModel" no Pydantic é uma classe base que permite a 
criação de modelos de dados com validação e tipagem automática.

"Optional" é um tipo genérico que representa um valor que pode ser do tipo especificado ou None
'''
# modelagem e validação tipo
class CursoSchema(SCBaseModel):
    # (modelo: tipo)
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int
    
    '''
    Essa class permite que o Pydantic converta automaticamente 
    modelos do SQLAlchemy (ORM) em dicionários compatíveis com JSON
    '''
    class Config:
        orm_mode = True
