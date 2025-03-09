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
---

**Aula_09**

__CRUD com FastAPI e SQL ALchemy__

- __api__ (recursos): são recursos de acesso aos dados por meio de métodos, __regras de negocio__

- __config__ (Banco de Dados): configurações de integração do Banco de dados

- __Schemas__ (modelos): gerencia e valida __dados entrada e saída da API__

- __Models__ (modelos): gerencia e valida __dados de transição entre API e Banco de Dados__

- Pasta e arquivos:
    - config:
        - __.\config\configs.py__: gerenciamento de endereço e tipo de Banco de Dados
        - __.\config\criar_tabelas.py__: gerenciamento de sessão (Ação ao Banco de Dados)
        - __.\config\deps.py__: função auxiliar usada como dependência para injeção de sessão no Banco de Dados.
    - models:
        - __.\models\_all_models.py__: agrupamento de modelos (TABELAS Banco de Dados)
        - __.\models\curso_model.py__: (modelos) => modelagem da dados (Banco de Dados)
    - schemas:
        - __.\schemas\curso_schemas.py__: (modelos) => modelagem da dados (API)
---

- A separação de rotas em FastAPI por __"tags"__ é uma técnica poderosa para organizar e documentar suas APIs de forma mais intuitiva e eficiente. Ela permite agrupar rotas relacionadas na __documentação__.
---

**Aula_xxx**

- main.py: instanciar projeto

- criar_tabelas.py: 

- api: projeto

- core: pasta de utilização comum ao projeto
    - configs.py: gerenciamento e configuração Banco de Dados
    - database.py: conexão ao Banco de Dados
    - deps.py: consulta Banco de dados

- models: pasta de modelagem
    - __all_models.py: 
    - curso_model.py: modelagem do Banco de Dados

- schemas: pasta descrição da estrutura dos dados
     - curso_schema.py: modelagem do API para Banco de Dados "curso_model.py"