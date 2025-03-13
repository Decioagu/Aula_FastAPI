# Aula_FastAPI
 Framework web com Python

**Aula_01**

- O __FastAPI__ é um framework web moderno, rápido e de alto desempenho para criar APIs RESTful e GraphQL com Python. Ele é baseado em __type hints__ do Python e oferece diversas funcionalidades que facilitam o desenvolvimento de APIs robustas e escaláveis.

- O __Pydantic__ é uma biblioteca Python poderosa e versátil que oferece diversos recursos para facilitar o desenvolvimento de software, com foco principal na validação de dados

- O "__BaseModel__" no Pydantic é uma classe base que permite a criação de modelos de dados com validação e tipagem automática.

- Em Python, __"async"__ e __"await"__ são palavras-chave que trabalham juntas para habilitar a programação assíncrona. Isso é particularmente útil para operações vinculadas a solicitações de rede ou acesso ao sistema de arquivos, onde você pode passar muito tempo aguardando.

- O pacote __uvicorn__ é um servidor web ASGI (Asynchronous Server Gateway Interface), uma interface padrão para comunicação entre servidores web, frameworks e aplicações Python, com foco em funcionalidades assíncronas. para Python.

- __Rotas em FastAPI__: os decorator @app.get(path), @app.post(path), @app.put(path) e @app.delete(path) são usados para definir uma rota para aplicação web.
---

**Aula_02**

__PROJETO HOTEL__

- Tratamento de dados, resposta:
    - __HTTPException__: permite retornar respostas de erro personalizadas com códigos de status HTTP.
    - __status__: códigos de status HTTP (facilita a leitura e manutenção do código).
    - __Response__: permitindo o controle direto sobre o conteúdo, status HTTP e cabeçalhos da resposta.

- Modelagem de dados:
    - __BaseModel__: é uma classe base do Pydantic que permite definir estruturas de dados com tipagem forte (modelagem).
    - __Optional__: define campos opcionais em modelos de dados, permitindo que esses atributos sejam omitidos em requisições sem causar erro de validação.
        OBS: No Python 3.10+, podemos usar str | None como alternativa para Optional[str]:
        Exp:
            class User(BaseModel):
                email: str | None  # Equivalente a (email: Optional[str] = None)

- Operações CRUD:
    - __Create (Criar)__: Insere novos registros em uma tabela do banco de dados.
    - __Read (Ler)__: Recupera dados existentes na tabela, podendo filtrar por critérios específicos.
    - __Update (Atualizar)__: Modifica o conteúdo de registros já existentes.
    - __Delete (Excluir)__: Remove registros da tabela.

    - Rotas: @app.get(path), @app.post(path), @app.put(path) e @app.delete(path):
        - path: especifica qual __URL__ será associada para função correspondente.

    - CRUD - Create   |  Read        |  Update     |  Delete
    - =====> Criar    |  Ler         |  Atualizar  |  Excluir
    - <==========================================================>
    - SQL  - INSERT   |  SELECT      |  UPDATE     |  DELETE
    - =====> Inserir  |  Selecionar  |  Atualizar  |  Excluir
    - <==========================================================>
    - API  - __POST__ | __GET__      |  __PUT__    |  __DELETE__
    - =====> Enviar   | Selecionar   |  Atualizar  |  Excluir   
---

**Aula_03**

__PROJETO HOTEL__

- Validação de objetos pelo usuário (POST E PUT):
    - O decorador __@field_validator__ é utilizado para validar um campo específico do modelo, oferecendo uma maneira de aplicar validações personalizadas para os dados de entrada.
    - O decorador __@classmethod__ é um decorador de Python que transforma um método em um método de classe, ou seja, ele é um método que recebe a própria classe (cls) como primeiro argumento, não é obrigatório porem recomendado.

- Personalização de mensagens na pagina de documentação: 
    - __app = FastAPI()__:
        - title= 'SUA_MENSAGEM'
        - version= 'SUA_MENSAGEM'
        - description= 'SUA_MENSAGEM'

        - Exp: app = FastAPI(title='Aula 03', version='0.0.3', description= 'Alua 10 até 16')

- Personalizar mensagem da Rota na pagina de documentação:
    - __@app.get()__:
        - description= 'SUA_MENSAGEM'
        - summary= 'SUA_MENSAGEM'
        - tags=["SUA_MENSAGEM"]
        
        - Exp: @app.get('/', description='Retorna uma mensagem', summary='Mensagem')
---

**Aula_04**

__PROJETO HOTEL__

- Em FastAPI, __Path__, __Query__ e __Header__ são funções utilizadas para declarar os __tipos de parâmetros__ que uma rota ou endpoint deve receber e como esses parâmetros são extraídos das requisições HTTP.

- __Path__: é usado para declarar parâmetros que são extraídos diretamente do caminho (URL) de uma requisição feita pelo usuário. O Path pode ser usados para limitar parâmetro de pesquisa como valores, expressões regulares, valor padrão e descrição de objetos.
[text](<Aula_04/O Path do FastAPI.pdf>)

- __Query__: é usado para declarar parâmetros que são extraídos da query string da URL. Extremamente útil para validar, restringir e documentar parâmetros na requisição do usuário. 
[text](<Aula_04/O Query do FastAPI.pdf>)

- __Header__: é usado para declarar parâmetros que são extraídos dos cabeçalhos da requisição HTTP. Esses parâmetros geralmente são usados para metadados, como autenticação ou informações do cliente.
[text](<Aula_04/O Header no FastAPI.pdf>)
---

**Aula_05**

- __Depends__ é uma ferramenta poderosa para gerenciar injeção de dependência em suas APIs. Permite __gerenciamento de conexões de Banco de Dados__ ou qualquer outra dependência que precise ser resolvida __antes de atender a uma requisição__ dentro da sua aplicação.

- __Any__ é um tipo especial que indica que uma variável pode ter qualquer tipo de dado.
[text](Any/main.py)
---

**Aula_06 & Aula_07**

- Personalizar mensagem da Rota na pagina de documentação:
    - summary: é uma breve descrição de uma rota específica. Ele aparece na lista de endpoints na documentação gerada.
    - description: é utilizado para fornecer uma descrição detalhada da API ou de uma rota específica.
    - response_description: é usado para fornecer uma descrição mais clara e amigável da resposta esperada da API.
    - response_model= define o modelo de resposta que a rota vai retornar para o usuário, para garantir que a resposta que você está retornando está no formato esperado. 
[text](Aula_06/response_model.pdf)

- Exemplos: 
    - __aula_06.py__:  Por DICIONÁRIO
    - __aula_07.py__:  Por LISTA
---

**Aula_08**

__ROTEADOR DE ROTAS__

- O método __app.include_router(rotas)__ é utilizado no FastAPI para incluir um roteador (APIRouter) dentro da aplicação principal. Isso ajuda a agrupar rotas.
- O __APIRouter__ funciona como um "mini aplicativo" dentro do FastAPI, onde você pode definir endpoints (Rotas: GET, POST, PUT e DELETE) separadamente e depois incluí-los na aplicação principal com __app.include_router()__.

Exp:
from fastapi import FastAPI, APIRouter

# Instanciar API
app = FastAPI() 

# Criando um roteador
rotas = APIRouter()

# Rota GET
@rotas.get("/")
async def listar_itens():
    return {"mensagem": "Lista de itens"}

# Rota POST
@rotas.post("/")
async def criar_item(item: dict):
    return {"mensagem": "Item criado", "item": item}

# Incluindo o roteador na aplicação principal
app.include_router(rotas)

if __name__ == 'main':
    
    from uvicorn import run 

    run('TESTE:app', host="127.0.0.1", port=8000, reload=True)

# uvicorn TESTE:app --reload
---

**Aula_09**

__CRUD com FastAPI e SQL ALchemy__

- __SQLAlchemy__ é uma biblioteca de __ORM__ (__Object-Relational Mapping__) em Python que permite interagir com bancos de dados usando classes e objetos, abstraindo as consultas SQL complexas. Além de funcionar como ORM, SQLAlchemy também oferece ferramentas para executar consultas SQL diretamente. Para usar o __SQLAlchemy de forma assíncrona__, você precisa usar sua versão com suporte assíncrono igual ou superior ao SQLAlchemy 1.4.

- O __greenlet__ é uma biblioteca que permite a execução de corrotinas (funções assíncronas) sem bloquear a execução do código. Ele é fundamental para o SQLAlchemy quando se usa asyncio.
    - __INSTALAÇÃO =>__ pip install greenlet

- Para utilizar o SQLAlchemy de forma assíncrona com __SQLite__, é necessário instalar o driver __aiosqlite__, que permite que o SQLAlchemy funcione de maneira assíncrona com o __SQLite__: 
    - __INSTALAÇÃO =>__ pip install aiosqlite
    - __USO =>__ engine = create_async_engine("sqlite+aiosqlite:///nome_do_banco.db", echo=True)

- Para utilizar o SQLAlchemy de forma assíncrona com __MySQL__, é necessário instalar o driver __aiomysql__, que permite que o SQLAlchemy funcione de maneira assíncrona com o __MySQL__:
    - __INSTALAÇÃO =>__ pip install aiomysql
    - __USO =>__ engine = create_async_engine("mysql+aiomysql://usuario:senha@localhost/nome_do_banco", echo=True)

- Para utilizar o SQLAlchemy de forma assíncrona com  __PostgreSQL__, é necessário instalar o driver __asyncpg__, que permite que o SQLAlchemy funcione de maneira assíncrona com o  __PostgreSQL__:
    - __INSTALAÇÃO =>__ pip install asyncpg
    - __USO =>__ engine = create_async_engine("postgresql+asyncpg://usuario:senha@localhost:5432/nome_do_banco", echo=True)

- OBS: O argumento __"echo=True"__ é um recurso de depuração e registro. Quando definido como True, o SQLAlchemy imprimirá todas as instruções SQL que ele executar no console (saída padrão).

- Pasta e arquivos:
    - config:
        - __.\config\conf_db.py__: gerenciamento do tipo de Banco de Dados
    - models:
        - __.\models\_all_models.py__: agrupamento de modelos (TABELAS Banco de Dados)
        - __.\models\curso_model.py__: (modelos) => modelagem da dados (Banco de Dados)
    - schemas:
        - __.\schemas\curso_schemas.py__: (modelos) => modelagem da dados (API)
    - __criar_tabela.py__: Ação de criar tabela do Banco de Dados

- __config__ (Banco de Dados): __SQLAlchemy__ é uma biblioteca de __ORM__ (__Object-Relational Mapping__) em Python que permite interagir com bancos de dados usando classes e objetos, abstraindo as consultas SQL complexas.
- __models__ (modelos): são estruturas de tabelas e colunas (Ligados diretamente ao Banco de Dados), geralmente criadas usando SQLAlchemy, também são estruturas que definem o __schemas__ das tabelas de uma API. 
- __schemas__ (modelos Pydantic): são estruturas de dados (Não ligados diretamente ao Banco de Dados) de entrada e saída de uma API  em forma de JSON, essenciais para validar, organizar e documentar informações de uma API.
---

**Aula_10**

__CRUD com FastAPI e SQL ALchemy__

- Pasta e arquivos:
    - routes:
        - __.\routes\api.py__: gerenciamento de Rotas (CRUD)
        - __.\routes\v1\curso_CRUD.py.py__: (recursos) => CRUD usuário
    - config:
        - __.\config\conf_db.py__: gerenciamento de variável de ambiente (Rotas)
    - __main.py__: adição de roteador à aplicação principal (Rotas).
    
- main.py:
    - __app.include_router()__: é o método usado para organizar e modularizar a aplicação, permitindo a inclusão de roteadores (APIRouter).
- api.py:
    - O __APIRouter()__ é um objeto que funciona como um "mini FastAPI", onde podemos definir rotas, como GET, POST, PUT e DELETE na aplicação principal com auxilio de __app.include_router()__.
- conf_db.py:
    - __BaseSettings__ serve para gerenciar configurações de forma eficiente e segura, utilizando o Pydantic para validação e carregamento de variáveis de ambiente.
---


**Aula_11**

__CRUD com FastAPI e SQL Model__

- __SQLModel__ é uma biblioteca Python que facilita a interação com bancos de dados SQL, combinando o poder do Pydantic para validação de dados com a flexibilidade do SQLAlchemy para interagir com o banco de dados.

- Pasta e arquivos:
    - config:
        - __.\config\conf_db.py__: gerenciamento do tipo de Banco de Dados
    - models:
        - __.\models\_all_models.py__: agrupamento de modelos (TABELAS Banco de Dados)
        - __.\models\curso_model.py__: (modelos) => modelagem da dados (API e Banco de Dados)
    - __criar_tabela.py__: Ação de criar tabela do Banco de Dados
---

**Aula_12**

__CRUD com FastAPI e SQL Model__

- Pasta e arquivos:
    - routes:
        - __.\routes\api.py__: gerenciamento de Rotas (CRUD)
        - __.\routes\v1\curso_CRUD.py.py__: (recursos) => CRUD usuário
    - __main.py__: adição de roteador à aplicação principal (Rotas).
---

**Aula_13**

- Escolha a instalação e manipulação de um Banco de dados SQLite ou MySQL:
    - __Resumo da aplicação SQL Alchemy em FastAPI com CRUD__
---

**Aula_14**

---

**Any**
**SQLAlchemy**
**SQLite**
**Documentos**