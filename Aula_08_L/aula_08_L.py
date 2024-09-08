from fastapi import FastAPI, HTTPException, status, Response
from typing import Optional, List
from pydantic import BaseModel, field_validator

# modelagem e validação tipo (tratamento de entrada do usuário)
class Curso(BaseModel):
    # (modelo: tipo = valor)
    id : Optional[int] = None
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

class Curso_sem_id(BaseModel):
    titulo: str
    aulas: Optional[int] = 1
    horas: int

# instanciar API
app = FastAPI(
             title='Aula 08_1',
             version='0.0.1',
             description= 'Alua 23'
             )

# dados iniciais (LISTA)
cursos = [
    Curso(id = 1, titulo= "Programação para Leigos", aulas= 112, horas= 58),
    Curso(id = 2, titulo= "Algoritmos e logica de programação", aulas= 87, horas= 67),
    Curso(id = 3, titulo= "Programação linguagem Python", aulas= 33, horas= 47)
]

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
         response_model=List[Curso])
async def get_cursos(): 
    return cursos

# rota (Ler dados por id)
@app.get('/cursos/{curso_id}', 
         summary='BUSCAR curso por id', 
         description='Acesso lista dos cursos por id'
        #  response_model=Curso
         )
async def get_curso(curso_id: int):

    # ====================================================== 
    # filtrar "cursos" por id
    filtrar_id_curso = filter(lambda meu_id: meu_id.id == curso_id, cursos)
    curso = dict(*filtrar_id_curso)
    # ======================================================

    if curso:
        return curso
    else:
        # tratar id inexistente
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
# rota (Criar novo curso)
@app.post('/cursos', 
          status_code=status.HTTP_201_CREATED, 
          summary='POST adicionar curso', 
          description='Adicione novo curso na listagem cursos'
          )
async def post_curso(curso: Curso):

    # ======================================================
    # adição de novo id com maior valor existente na lista "cursos"
    proximo_id = 0
    # filtrar "cursos" por id
    for id in cursos:
        if id.id > proximo_id:
            proximo_id = id.id
    proximo_id += 1
    # ======================================================

    curso.id = proximo_id # <===== novo id
    cursos.append(curso)
    return curso

# rota (Atualizar novo curso por id)
@app.put('/cursos/{curso_id}', 
         summary='PUT atualizar curso por id', 
         description='Altere informações do curso escolhido por id')
async def put_curso(curso_id: int, curso: Curso):
    
    # filtrar "cursos" por id
    for filtrar_curso in cursos: 
        if filtrar_curso.id == curso_id:
            filtrar_curso.titulo = curso.titulo # atualizar
            filtrar_curso.aulas = curso.aulas # atualizar
            filtrar_curso.horas = curso.horas # atualizar
            return curso
    
    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

    
# rota (Deletar novo curso por id)
@app.delete('/cursos/{curso_id}', 
            summary='DELETE excluir curso por id', 
            description='Excluir curso por id na listagem cursos'
            )
async def delete_curso(curso_id: int):
    # filtro "cursos" por id
    for index, filtrar_curso in enumerate(cursos): 
        if filtrar_curso.id == curso_id:
            cursos.pop(index) # eliminar por posição na lista "cursos"
            return Response(status_code=status.HTTP_204_NO_CONTENT)
               
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Curso não encontrado')


if __name__ == 'main':
    
    from uvicorn import run # subir o servidor: uvicorn Aula_08_L.aula_08_L:app --reload

    run('main:app', host="127.0.0.1", port=8000, reload=True)
     