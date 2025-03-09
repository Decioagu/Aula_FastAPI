from pydantic import BaseModel
from typing import Optional

class HotelSchema(BaseModel):
    nome: str
    estrelas: Optional[float] = None
    diaria: Optional[float] = None
    cidade: str

    class Config:
        orm_mode = True
