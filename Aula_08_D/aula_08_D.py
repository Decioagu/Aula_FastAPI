from fastapi import FastAPI, HTTPException, status, Response
from typing import Optional, Dict
from pydantic import BaseModel, field_validator
from time import sleep

# modelagem e validação tipo (tratamento de entrada do usuário)
class Curso(BaseModel):
    # (modelo: tipo = valor)
    titulo: str
    aulas: Optional[int] = 1
    horas: int

    @field_validator('titulo')
    def validate_titulo(cls, titulo_valido):
        # Verifica se o valor de aulas é positivo
        if not len(titulo_valido):
            raise ValueError('<========> titulo: deve conter almenos um carácter  <========> \n')
        return titulo_valido

    @field_validator('aulas')
    def validate_aulas(cls, aulas_valido):
        # Verifica se o valor de aulas é positivo
        if aulas_valido < 1:
            raise ValueError('<========> aulas: deve ser maior que 1 (um) <========> \n')
        return aulas_valido
    
    @field_validator('horas')
    def validate_horas(cls, horas_valido):
        # Verifica se o valor de horas é positivo
        if horas_valido < 0:
            raise ValueError('<========> horas: deve ser maior que 0 (zero) <========> \n')
        return horas_valido

# instanciar API
app = FastAPI(
             title='Aula 08',
             version='0.0.1',
             description= 'Alua 21'
             )

# dados iniciais (DICIONÁRIO)
cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e logica de programação",
        "aulas": 87,
        "horas": 67
    },
    3: {
        "titulo": "Programação linguagem Python",
        "aulas": 33,
        "horas": 47
    }
}

# rota
@app.get('/', summary='documentos', 
         description='Link inicial para acesso documento: http://127.0.0.1:8000/docs'
        )
async def get_site():
    return 'Abra===> http://127.0.0.1:8000/docs'

# rota (Ler todos os dados)
@app.get('/cursos', 
         summary='BUSCAR listagem dos cursos ',
         description='Acesso lista de todos os cursos',
         response_model=Dict[int, Curso],
         response_description='Cursos encontrados com sucesso!!!'
         )
async def get_cursos(): 
    return cursos

# rota (Ler dados por id)
@app.get('/cursos/{curso_id}', 
         summary='BUSCAR curso por id', 
         description='Acesso lista dos cursos por id',
         response_model=Curso
         )
async def get_curso(curso_id: int): 
    try:
        curso = cursos[curso_id] # filtrar "cursos" por id
        return curso
    except KeyError:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
# rota (Criar novo curso)
@app.post('/cursos', status_code=status.HTTP_201_CREATED, 
          summary='POST adicionar curso', 
          description='Adicione novo curso na listagem cursos'
        )
async def post_curso(curso: Curso):

    # ======================================================
    # adição de novo id com maior valor existente na lista "cursos"
    proximo_id = 0 # nova chave
    # filtrar "cursos" por id
    for id in cursos.keys():
        print(id)
        if id > proximo_id:
            proximo_id = id
    proximo_id += 1
    # ======================================================

    cursos[proximo_id] = curso # <======= novo id
    return cursos

# rota (Atualizar novo curso por id)
@app.put('/cursos/{curso_id}', summary='PUT atualizar curso por id', description='Altere informações do curso escolhido por id')
async def put_curso(curso_id: int, 
                    curso: Curso, 
                    ):
    if curso_id in cursos:
        cursos[curso_id] = curso # filtrar "cursos" por id
        return curso
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

    
# rota (Deletar novo curso por id)
@app.delete('/cursos/{curso_id}', 
            summary='DELETE excluir curso por id', 
            description='Excluir curso por id na listagem cursos',
            response_description='Excluído com sucesso!!!'
            )
async def delete_curso(curso_id: int):
    
    if curso_id in cursos: # se id existir em "cursos" (filtro)
        del cursos[curso_id] # eliminar id do corpo do dados
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Curso não encontrado')

if __name__ == 'main':
    
    from uvicorn import run # subir o servidor: uvicorn Aula_08_D.aula_08_D:app --reload

    run('main:app', host="127.0.0.1", port=8000, reload=True)
     