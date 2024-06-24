from pydantic import BaseModel
from typing import Optional

'''
O "BaseModel" no Pydantic é uma classe base que permite a 
criação de modelos de dados com validação e tipagem automática

"Optional" é um tipo genérico que representa um valor que pode ser do tipo especificado ou None
'''
# estrutura para criação de curso
class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int