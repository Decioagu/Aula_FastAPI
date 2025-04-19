from fastapi import FastAPI, Query
from typing import Optional, List
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: Optional[int] = 1
    horas: int

app = FastAPI(
    title='Aula_07',
    version='0.0.7',
    description='Aula 21'
)

cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=60, horas=58),
    Curso(id=2, titulo="Algoritmos e logica de programação", aulas=33, horas=67),
    Curso(id=3, titulo="Programação linguagem Python", aulas=33, horas=58),
    Curso(id=4, titulo="Programação para Leigos", aulas=68, horas=78),
    Curso(id=5, titulo="Algoritmos e logica de programação", aulas=32, horas=87),
    Curso(id=6, titulo="Programação linguagem Python", aulas=42, horas=42),
    Curso(id=7, titulo="Programação para Leigos", aulas=60, horas=57),
    Curso(id=8, titulo="Algoritmos e logica de programação", aulas=33, horas=41),
    Curso(id=9, titulo="Programação para Leigos", aulas=60, horas=58),
    Curso(id=10, titulo="Algoritmos e logica de programação", aulas=33, horas=67),
    Curso(id=11, titulo="Programação linguagem Python", aulas=33, horas=58),
]

@app.get('/')
async def get_site():
    return 'http://127.0.0.1:8000/docs'

@app.get('/cursos', 
         summary='BUSCAR listagem dos cursos',
         description='Acesso lista de todos os cursos com filtros opcionais e paginação',
         response_model=List[Curso],
         response_description='Modelo de lista com filtros e paginação'
)
async def get_cursos(
    titulo: Optional[str] = Query(None, description="Filtrar pelo título do curso"), # Filtro de pesquisa
    aulas: Optional[int] = Query(None, description="Filtrar pela quantidade de aulas"), # Filtro de pesquisa
    horas: Optional[int] = Query(None, description="Filtrar pela carga horária"), # Filtro de pesquisa
    iniciar_no_item: int = Query(0, ge=0, description="Número de itens a pular (offset)"), # Paginação
    limite: int = Query(10, gt=0, description="Número máximo de itens a retornar (limite)") # Paginação  
    ): 
    
    resultados = cursos

    # Filtros
    if titulo:
        resultados = [c for c in resultados if titulo.lower() in c.titulo.lower()]
    if aulas is not None:
        resultados = [c for c in resultados if c.aulas == aulas]
    if horas is not None:
        resultados = [c for c in resultados if c.horas == horas]

    # Paginação
    paginados = resultados[iniciar_no_item: iniciar_no_item  + limite]
    print(paginados)
    ''' 
    paginação:
    iniciar_no_item: inicie exibição dos itens a partir do item escolhido
    Exp: quantidade 11 itens, (iniciar_no_item = 3) vai iniciar exibição de 4 em diante

    limite: limita quantidade de item exibido ao usuário
    Exp: quantidade 11 itens, (limite=5) exibirá ao usuário 5 itens no total da lista
    '''

    return paginados

if __name__ == 'main':
    
    from uvicorn import run 

    run('main:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn Aula_18.aula_18:app --reload

'''
Você pode acessar a URL com filtros assim:

/cursos?titulo=python # Filtro

/cursos?aulas=112 # Filtro

/cursos?titulo=programacao&horas=58 # Filtro

Como testar no navegador ou Postman:

/cursos?iniciar_no_item=0&limite=3 → exibir item 1 com 3 cursos

/cursos?iniciar_no_item=3&limite=5 → exibir item 4 com os próximos 5 cursos
'''