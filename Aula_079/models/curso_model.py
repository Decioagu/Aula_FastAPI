from sqlalchemy import Column, Integer, String
from config.configs import settings ### Configurações Banco de Dados

# modelagem e validação tipo  
class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'
    # (modelo: tipo = Coluna(tipo valor coluna))
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)
