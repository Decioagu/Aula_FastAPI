# Aula_FastAPI
 Framework web com Python

 **Aula_01 & Aula_02**

- Python: __"async"__ e __"await"__

    -   Em Python, __"async"__ e __"await"__ são palavras-chave que trabalham juntas para habilitar a programação assíncrona. Isso significa que seu programa pode lidar com várias tarefas simultaneamente sem bloquear o __thread__ principal. Isso é particularmente útil para operações vinculadas a solicitações de rede ou acesso ao sistema de arquivos, onde você pode passar muito tempo aguardando.
---

**Aula_03**
- O "__BaseModel__" no Pydantic é uma classe base que permite a criação de modelos de dados com validação e tipagem automática.
- O módulo "__field_validator"__ oferece uma ferramenta poderosa para personalizar validações complexas e específicas para atender às suas necessidades.
---

**Aula_04**

 - O __Pydantic__ é uma biblioteca Python poderosa e versátil que oferece diversos recursos para facilitar o desenvolvimento de software, com foco principal na validação de dados

- O __FastAPI__ é um framework web moderno, rápido e de alto desempenho para criar APIs RESTful e GraphQL com Python. Ele é baseado em __type hints__ do Python e oferece diversas funcionalidades que facilitam o desenvolvimento de APIs robustas e escaláveis.

- O pacote __uvicorn__ é um servidor web ASGI (Asynchronous Server Gateway Interface), uma interface padrão para comunicação entre servidores web, frameworks e aplicações Python, com foco em funcionalidades assíncronas. para Python.

- O __gunicorn__, abreviação de "Green Unicorn", é um servidor HTTP assíncrono de alta performance escrito em Python. Ele é amplamente utilizado para hospedar aplicações Python na web.

- __Rotas__ de acesso são como os endereços específicos que você usa para acessar diferentes recursos
---

**Aula_05**

- Operações CRUD:
    - __Create (Criar)__: Insere novos registros em uma tabela do banco de dados.
    - __Read (Ler)__: Recupera dados existentes na tabela, podendo filtrar por critérios específicos.
    - __Update (Atualizar)__: Modifica o conteúdo de registros já existentes.
    - __Delete (Excluir)__: Remove registros da tabela.

- CRUD - Create   |  Read        |  Update     |  Delete
- =====> Criar    |  Ler         |  Atualizar  |  Excluir
- <==========================================================>
- SQL  - INSERT   |  SELECT      |  UPDATE     |  DELETE
- =====> Inserir  |  Selecionar  |  Atualizar  |  Excluir
- <==========================================================>
- API  - __POST__ | __GET__      |  __PUT__    |  __DELETE__
- =====> Enviar   | Selecionar   |  Atualizar  |  Excluir
---

**Aula_06**

- Em FastAPI, __Path__, __Query__ e __Header__ são funções utilizadas para declarar os __tipos de parâmetros__ que uma rota ou endpoint deve receber e como esses parâmetros são extraídos das requisições HTTP.

- __Path__: é usado para declarar parâmetros que são extraídos diretamente do caminho (URL) de uma requisição. Esses parâmetros são obrigatórios e fazem parte da definição do caminho da rota. Ex: limitar parâmetro de pesquisa ou apontar caminho como id de uma lista, biblioteca ou banco de dados.

- __Query__: é usado para declarar parâmetros que são extraídos da query string da URL. Esses parâmetros são opcionais por padrão, mas podem ser tornados obrigatórios. Ex: envio de valores numéricos para uma conta.

- __Header__: é usado para declarar parâmetros que são extraídos dos cabeçalhos da requisição HTTP. Esses parâmetros geralmente são usados para metadados, como autenticação ou informações do cliente.
---

**Aula_07**

- __Depends__ é uma ferramenta poderosa para gerenciar injeção de dependência em suas APIs. Permite __gerenciamento de conexões de banco de dados__ ou qualquer outra dependência que precise ser resolvida __antes de atender a uma requisição__ dentro da sua aplicação.
---

**Aula_08_D & Aula_08_L**

- __Aula_08_D__ = Por DICIONÁRIO
- __Aula_08_L__ = Por LISTA

- Descrição das rotas no link da documentação:
- Ex: __http://127.0.0.1:8000/docs__ ou __http://127.0.0.1:8000/redoc__
    - __field_validator"__: validação personalizada. 
    - __title__:  define o nome da aplicação. Ele é exibido como título principal na interface de documentação gerada pelo FastAPI.
    - __version__: define a versão da aplicação. Isso ajuda a identificar diferentes iterações do seu projeto.
    - __description__: é utilizado para fornecer uma descrição detalhada da API ou de uma rota específica.
    - __summary__: é uma breve descrição de uma rota específica. Ele aparece na lista de endpoints na documentação gerada
    - __response_model__: é utilizado para definir o modelo de dados que será retornado pela rota.
    - __response_description__: é usado para fornecer uma descrição mais clara e amigável da resposta esperada da API.
---

**Aula_09**

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