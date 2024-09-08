from core.configs import settings # configurações Banco de Dados

from sqlalchemy import Column, Integer, String

# modelagem e validação tipo  
class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'
    # (modelo: tipo = Coluna(tipo valor coluna))
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)
