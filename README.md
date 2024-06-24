# Aula_FastAPI
 Framework web com Python

**Aula_01**

 - O __Pydantic__ é uma biblioteca Python poderosa e versátil que oferece diversos recursos para facilitar o desenvolvimento de software, com foco principal na validação de dados

- O __FastAPI__ é um framework web moderno, rápido e de alto desempenho para criar APIs RESTful e GraphQL com Python. Ele é baseado em __type hints__ do Python e oferece diversas funcionalidades que facilitam o desenvolvimento de APIs robustas e escaláveis.

- O pacote __uvicorn__ é um servidor web ASGI (Asynchronous Server Gateway Interface), uma interface padrão para comunicação entre servidores web, frameworks e aplicações Python, com foco em funcionalidades assíncronas. para Python.

- O __gunicorn__, abreviação de "Green Unicorn", é um servidor HTTP assíncrono de alta performance escrito em Python. Ele é amplamente utilizado para hospedar aplicações Python na web.

**Aula_02**

- Operações:
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
- API  - POST    |  GET          |  PUT        |  DELETE
- =====> Enviar  |  Selecionar   |  Atualizar  |  Excluir

**Aula_03**

- Path:
    - Use Path para parâmetros que identificam recursos únicos.
    - Usado para parâmetros obrigatórios na rota da API.
    - Declarado dentro dos parênteses da rota.
    - Convertido automaticamente para o tipo de dado especificado.
    - Exemplo: /users/{user_id}. O user_id é um parâmetro de caminho do tipo inteiro.

- Query:
    - Use Query para parâmetros que controlam a filtragem ou ordenação de dados.
    - Usado para parâmetros opcionais na rota da API.
    - Declarado após o ponto de interrogação (?) na rota.
    - Pode ter vários valores separados por vírgula.
    - Exemplo: /items?page=1&sort=name. page e sort são parâmetros de consulta opcionais.

- Header:
    - Use Header para metadados que não estão diretamente relacionados aos dados da API.
    - Usado para metadados adicionais na requisição HTTP.
    - Declarado usando a anotação Header no código Python.
    - Insensível a maiúsculas e minúsculas por padrão.
    - Exemplo: Authorization: Bearer <token>. O Authorization é um header HTTP que contém um token de autenticação.

**Aula_04**

- __Depends__ é uma ferramenta poderosa para gerenciar dependências e injeção de dependência em suas APIs. Permite que você obtenha objetos de diversas fontes, como bancos de dados, caches, serviços externos ou mesmo instâncias de outras classes dentro da sua aplicação.

**Aula_05**