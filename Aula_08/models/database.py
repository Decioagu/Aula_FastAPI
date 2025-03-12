from pydantic import BaseModel
from typing import Optional


# modelagem e validação tipo (tratamento de entrada do usuário)
class Curso(BaseModel):
    # (modelo: tipo = valor)
    id : Optional[int] = None
    titulo: str
    aulas: Optional[int] = 1
    horas: int

# dados iniciais (LISTA)
cursos = [
    Curso(id = 1, titulo= "Programação para Leigos", aulas= 112, horas= 58),
    Curso(id = 2, titulo= "Algoritmos e logica de programação", aulas= 87, horas= 67),
    Curso(id = 3, titulo= "Programação linguagem Python", aulas= 33, horas= 47)
]
