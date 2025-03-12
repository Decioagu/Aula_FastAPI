from typing import Optional
from sqlmodel import Field, SQLModel

# Modelagem (API e BANCO DE DADOS)
class CursoModel(SQLModel, table=True):
    __tablename__: str = 'cursos' # Nome da tabela
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    aulas: int
    horas: int
    '''Define um modelo SQLModel que será convertido em uma tabela no banco de dados (pois table=True).'''

'''
Dentro do "Field()", podemos definir várias propriedades para os campos, como:

- Parâmetro:    Descrição:
- default:......Define um valor padrão para a coluna.
- primary_key:..Indica se a coluna é uma chave primária.
- index:........Cria um índice no banco de dados para otimizar buscas.
- unique:.......Garante que os valores desse campo sejam únicos.
- nullable:.....Permite valores NULL (por padrão, False).
- max_length:...Define o tamanho máximo de uma str.
- foreign_key:..Define uma chave estrangeira (relacionamento entre tabelas).

'''