# Aula_FastAPI
 Framework web com Python

**Aula_01**

- O __FastAPI__ é um framework web moderno, rápido e de alto desempenho para criar APIs RESTful e GraphQL com Python. Ele é baseado em __type hints__ do Python e oferece diversas funcionalidades que facilitam o desenvolvimento de APIs robustas e escaláveis.

- O __Pydantic__ é uma biblioteca Python poderosa e versátil que oferece diversos recursos para facilitar o desenvolvimento de software, com foco principal na validação de dados (seu tipo), não possui uma primary_key automática, não lida diretamente com Banco de Dados.

- O "__BaseModel__" no Pydantic é uma classe base que permite a criação de modelos de dados com validação e tipagem automática.

- Em Python, __"async"__ e __"await"__ são palavras-chave que trabalham juntas para habilitar a programação assíncrona. Isso é particularmente útil para operações vinculadas a solicitações de rede ou acesso ao sistema de arquivos, onde você pode passar muito tempo aguardando.

- O pacote __uvicorn__ é um servidor web ASGI (Asynchronous Server Gateway Interface), uma interface padrão para comunicação entre servidores web, frameworks e aplicações Python, com foco em funcionalidades assíncronas. para Python.

- __Rotas em FastAPI__: os decorator @app.get(path), @app.post(path), @app.put(path) e @app.delete(path) são usados para definir uma rota para aplicação web.
---

**Aula_02**

__CRUD com FastAPI e BaseModel__

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

    - O CRUD é o fundamento da persistência de dados, toda aplicação que **cria**, **lê**, **atualiza** ou **exclui** informações (em um BANCO DE DADOS ou API) está implementando é um CRUD.

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

__CRUD com FastAPI, BaseModel e SQL ALchemy__

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

__CRUD com FastAPI, BaseModel e SQL ALchemy__

- Pasta e arquivos:
    - routes:
        - __.\routes\api.py__: gerenciamento de Rotas (CRUD)
        - __.\routes\v1\curso_CRUD.py__: (recursos) => CRUD usuário
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

- __Resumo CRUD com FastAPI, BaseModel e SQL ALchemy__
---

**Aula_12**

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

**Aula_13**

__CRUD com FastAPI e SQL Model__

- Pasta e arquivos:
    - routes:
        - __.\routes\api.py__: gerenciamento de Rotas (CRUD)
        - __.\routes\v1\curso_CRUD.py__: (recursos) => CRUD usuário
    - __main.py__: adição de roteador à aplicação principal (Rotas).

- curso_CRUD.py:
    - __select__ é uma maneira mais moderna e recomendada de fazer consultas SQL no SQLAlchemy.
        - Equivalência entre os filtros:
            - query = select(CursoModel) <==> query = db.query(CursoModel).all()
    - 
---

**Aula_14**

- __Resumo da aplicação SQL MODEL em FastAPI com CRUD__
---

**Aula_15**

__Autenticação JWT com FastAPI e SQL ALchemy__

- A autenticação __JWT__ (JSON Web Token) em FastAPI é um método de autenticação baseado em tokens que permite que usuários se autentiquem de forma segura.

- Pasta e arquivos:
    - config:
        - __.\config\conf_db.py__: gerenciamento do tipo de Banco de Dados e configuração de segurança __JWT__
    - models:
        - __.\models\_all_models.py__: agrupamento de modelos (TABELAS Banco de Dados)
        - __.\models\artigos_model.py__: (modelos) => modelagem da dados (API e Banco de Dados)
        - __.\models\usuario_model.py__: (modelos) => modelagem da dados (API e Banco de Dados)
    - schemas:
        - __.\schemas\artigo_schemas.py__: (modelos) => modelagem da dados (API)
        - __.\schemas\usuario_schemas.py__: (modelos) => modelagem da dados (API)
    - __criar_tabela.py__: Ação de criar tabela do Banco de Dados
---

**Aula_16**

__Autenticação JWT com FastAPI e SQL ALchemy__

- Pasta e arquivos:
    - config:
        - __.\config\security.py__: Define o esquema de autenticação (Token JWT das requisições)
        - __.\config\auth.py__: Criar autenticação do usuário (Tokens JWT)
        - __.\config\deps.py__: Verifica autenticação do usuário (Tokens JWT)
    - routes:
        - __.\routes\api.py__: gerenciamento de Rotas (CRUD)
        - __.\routes\v1\artigo.py__: (recursos) => CRUD usuário (Autenticação JWT)
        - __.\routes\v1\usuario.py__: (recursos) => CRUD usuário (Autenticação JWT)
    - __main.py__: adição de roteador à aplicação principal (Rotas).

- __security.py__:
    - O __CryptContext__ permite gerenciar diferentes algoritmos de hashing de senhas e facilita a verificação e atualização dos hashes ao longo do tempo.

- __auth.py__:
    - __OAuth2PasswordBearer__ é um esquema de segurança que espera que o cliente envie um token JWT no cabeçalho da requisição para acessar rotas protegidas. Ele define a forma como a API receberá o token, mas não realiza a autenticação por si só – você ainda precisa implementar a validação do token.
    - __EmailStr__ é um tipo de dado especializado do Pydantic que valida automaticamente se o valor fornecido é um e-mail válido.
    
- __deps.py__:
    -  __JOSE__ (JavaScript Object Signing and Encryption), que é uma biblioteca Python usada para trabalhar com tokens JWT (JSON Web Tokens), responsável por gerar e decodificar tokens JWT.
    - __JWTError__: Exceção que é levantada quando ocorre algum erro ao lidar com JWTs.

- __artigo.py__ e __usuario.py__:
    - __from config.deps import get_session, get_current_user__
        - __get_session__: Sessão ao Banco de Dados
        - __get_current_user__: Autenticar um usuário para acesso ao banco de dados (Token JWT)
---

**Aula_17**
- __Resumo de autenticação JWT com FastAPI e SQL ALchemy__
    - Em login (http://127.0.0.1:8000/usuario/login): 
        - Renomear parâmetro da documentação
            - username = email do usuário
            - password = senha do usuário
---

**Aula_18**
- __Exemplo de FILTRO e PAGINAÇÃO com Query em FastAPI__
---

**Aula_19**
- __Introdução Websites com FastAPI__

- **HTMLResponse** é um tipo especial de resposta HTTP que o FastAPI usa para enviar conteúdo HTML (como páginas da web) para o cliente.
---

**Aula_20**
- __Introdução Websites com FastAPI__

- __Templates HTML__

    - __Requests__ é uma biblioteca Python que fornece uma interface simples e elegante para __fazer solicitações HTTP__. Ela é muito popular entre desenvolvedores web e de APIs, pois permite enviar e receber dados de servidores HTTP de forma rápida e fácil.

    - __Jinja2Templates__ é uma biblioteca Python que cria uma instância configurada do __Jinja2__, que é um motor de template (template engine) usado em aplicações web Python, como Flask, FastAPI e Django. Ele permite misturar Python com HTML, criando páginas dinâmicas, apontando para a pasta onde estão os arquivos de template (HTML).

- Pasta e arquivos:
    - templates:
        - __.\templates\index.html__: templates
        - __.\templates\servico.html__: templates
    - __main.py__: Declaração de rotas para templetes 

---

**Aula_21**
- __Introdução Websites com FastAPI__

- __Layout HTML compartilhados__ 
    
    - __Compartilhamento de LAYOUT HTML__ refere-se à prática de reutilizar a estrutura fundamental (__layout base__) de um documento HTML em diferentes páginas de um website ou até mesmo em projetos distintos.

    - Usando Linguagens de Template com __Jinja2__ - Python:
        - templates:
            - __.\templates\base.html__: layout base para templetes
            - __.\templates\index.html__: herdeiro do layout base (templetes)
            - __.\templates\servico.html__: herdeiro do layout base (templetes)

    - Segue exemplo com __Jinja2__:
        - {% extends 'base.html' %}: indica que esta página usa o layout definido em base.html.
        - {% block title %} e {% endblock %} definem um bloco que pode ser substituído com o título específico da página.
        - {% block style %} e {% endblock %}: define um bloco chamado "style" dentro de um arquivo de template.
        - {% block content %} e {% endblock %}: definem a área onde o conteúdo principal da página será inserido.
        - {% include 'header.html' %} e {% include 'footer.html' %}: incluem o conteúdo dos arquivos header.html e footer.html no layout base.
        - {% if imagem %} e {% endif %}: verifica se a variável imagem existe e tem algum valor considerado para execução
---

**Aula_22**
- __Introdução Websites com FastAPI__

- __Arquivos Estáticos__

- __StaticFiles__ é uma classe da FastAPI (herdada de Starlette) que permite expor uma pasta contendo arquivos estáticos para que eles possam ser acessados via navegador.

- Pasta e arquivos:
    - static:
        - css:
            - __.\static\css\styles.css__: estilo da pagina
    - templates:
        - __.\templates\base.html__: adição de link para estilo layout base
    - __main.py__: apontar caminho para arquivos estáticos (estilo da pagina) 
---

**Aula_23**
- __Introdução Websites com FastAPI__

- __Extração de dados do USUÁRIO em texto via Website__

- Pasta e arquivos:
    - templates:
        - __.\templates\servicos.html__: adição de formulário, campo de extração e botão de ação
    - __main.py__: serviço "post", extração de dados do usuário
---

**Aula_24**
- __Introdução Websites com FastAPI__

- __Carregamento e baixar arquivos armazenado no PC__

- __UploadFile__ permite lidar com envio de arquivos (uploads) em requisições HTTP feitas para uma rota FastAPI.
- __async_open__ serve para abrir arquivos de forma assíncrona em Python usando a biblioteca __aiofile__.
- __uuid4__ é usado para gerar identificadores únicos __(UUIDs)__ em Python.

- Pasta e arquivos:
    - templates:
        - __.\templates\servicos.html__: exibir imagem na pagina se existir
    - __main.py__: Buscar e carregamento de arquivo na pasta "download"
---

**Aula_25**
- __Projeto FastAPI Website__

- __Compartilhamento de LAYOUT HTML__ com __Jinja2__ Python:

- Pasta __templates__: Gerenciamento das paginas HTML
    - Pasta __.\templates\home__: Templates das paginas de domínio publico

- Pasta e arquivos:
    - static:
        - css:
            - __.\static\css\styles.css__: estilo da pagina (layout base, linha 69)
    - templates:
        - __.\templates\base.html__: layout base para templetes (agrupamento de rotas paginas HTML)
        - home:
            - __.\templates\home\index.html__: herdeiro do layout base (inclusão de templetes)
                - __.\templates\home\header.html__: template
                - __.\templates\home\features.html__: template
                - __.\templates\home\testimonial.html__: template
                - __.\templates\home\blog_preview.html__: template
            - __.\templates\home\about\about.html__: herdeiro do layout base (inclusão de templetes)
                - __.\templates\home\about\header.html__: template
                - __.\templates\home\about\section_one.html__: template
                - __.\templates\home\about\section_two.html__: template
                - __.\templates\home\about\team_members.html__: template
            - __.\templates\home\blog_post.html__: herdeiro do layout base 
            - __.\templates\home\blog.html__: herdeiro do layout base (inclusão de templetes)
                - __.\templates\home\blog\page_content.html__: template
                - __.\templates\home\blog\news.html__: template
                - __.\templates\home\blog\preview.html__: template
            - __.\templates\home\contact.html__: herdeiro do layout base (inclusão de templetes)
                - __.\templates\home\contact\cards.html__: template
            - __.\templates\home\faq.html__: herdeiro do layout base
                - __.\templates\home\faq\sec_1.html__: template
                - __.\templates\home\faq\sec_2.html__: template
            - __.\templates\home\portfolio_item.html__: herdeiro do layout base 
            - __.\templates\home\portfolio.html__: herdeiro do layout base 
            - __.\templates\home\pricing.html__: herdeiro do layout base
                - __.\templates\home\pricing\card_free.html__: template
                - __.\templates\home\pricing\card_pro.html__: template
                - __.\templates\home\pricing\card_enterprise.html__: template
    - __main.py__: Declaração de rotas para templetes 
---

**Aula_26**
- __Projeto FastAPI Website__

- __Implementação de Banco de Dados SQLalchemy em FastAPI__

- Pasta __core__:
    - Configuração do Banco de Dados e implemento Jinja2 (HTML)
- Pasta __models__:
    - Estruturas das tabelas e colunas (Ligados diretamente ao Banco de Dados) por __configs.py__.
- Pasta __views__:
    - Gerecimento das rotas arquivo __.\templates\base.html__ para navegação das paginas em __.\templates\home__.

- Pasta e arquivos:
    - core:
        - __.\core\configs.py__: gerenciamento do tipo de Banco de Dados e implemento Jinja2 (HTML)
        - __.\core\database.py__: ação de criar tabela do Banco de Dados
    - models: pasta vazia
    - models:
        - __.\models\_all_models.py__: agrupamento de modelos (TABELAS Banco de Dados)
        - __.\models\area_model.py__: (modelos) => modelagem da dados (Banco de Dados)
        - __.\models\autor_model.py__: (modelos) => modelagem da dados (Banco de Dados)
        - __.\models\comentario_model.py__: (modelos) => modelagem da dados (Banco de Dados)
        - __.\models\duvida_model.py__: (modelos) => modelagem da dados (Banco de Dados)
        - __.\models\post_model.py__: (modelos) => modelagem da dados (Banco de Dados)
        - __.\models\projeto_model.py__: (modelos) => modelagem da dados (Banco de Dados)
        - __.\models\tag_model.py__: (modelos) => modelagem da dados (Banco de Dados)
        - __.\models\membro_model.py__: (modelos) => modelagem da dados (Banco de Dados)
    - views:
        - __home_view.py__: Gerecimento das rotas arquivo __.\templates\base.html__
    - __main.py__: Simplificação de acesso as rotas para __.\views\home_view.py__
    - __startup.db__: Banco de Dados SQLite (__.\core\database.py__)

-  OBS: Este Banco de dados é para alimentar images e dados para carregamento das paginal HTML (templates).
---

**Aula_27**
- __Projeto FastAPI Website__

__CRUD com FastAPI e SQL ALchemy__

- Pasta __controllers__:
    - São estruturas de dados (Não ligados diretamente ao Banco de Dados) de entrada e saída de uma API  em forma de JSON, essenciais para validar, organizar e documentar informações de uma API.
    - Em resumo __controllers__ utilizar __models__ para se comunicar com o Banco de Dados de forma indireta.

- Pasta e arquivos:
    - controllers:
        - __.\controllers\base_controller.py__: (recursos) => estrutura genérica CRUD (compartilhar recursos)
        - __.\controllers\area_controller.py__: (recursos) => CRUD
        - __.\controllers\autor_controller.py__: (recursos) => CRUD
        - __.\controllers\comentario_controller.py__: (recursos) => CRUD
        - __.\controllers\duvida_controller.py__: (recursos) => CRUD
        - __.\controllers\membro_controller.py__: (recursos) => CRUD
        - __.\controllers\post_controller.py__: (recursos) => CRUD
        - __.\controllers\projeto_controller.py__: (recursos) => CRUD
        - __.\controllers\tag_controller.py__: (recursos) => CRUD

- OBS: __base_controller.py__ é uma estrutura genérica para agrupar CRUD comuns aos demais recursos, em resumo é uma Classe PAI que por meio de HERANÇA permite compartilhar métodos as Classes FILHAS ou Subclasses.
---

**Aula_28**
- __Projeto FastAPI Website__

- Pasta __templates__: Gerenciamento das paginas HTML
    - Pasta __.\templates\home__: Templetes das paginas de domínio publico
    - Pasta __.\templates\admin__: Templetes das paginas de serviços administrativo
- Pasta __views__: - Gerecimento das rotas (arquivo __.\templates\base.html__) para navegação das paginas de domínio publico
    - Pasta __.\views\admin__: Faz INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__ e gerenciamento das rotas administrativas (__.\templates\admin__) para serviços ao usuário final.

- Pasta e arquivos:
    - templates:
        - __.\templates\base.html__: layout base para templetes (agrupamento de rotas para domínio publico pasta __.\templates\home__)
        - __.\templates\404.html__: templetes (resposta de erro para serviço não encontrado)
        - __.\templates\500.html__: templetes (resposta de erro para falha inesperada)
        - admin:
            - __.\templates\admin\404.html__: templetes (resposta de erro para serviço não encontrado)
            - __.\templates\admin\500.html__: templetes (resposta de erro para falha inesperada)
            - __.\templates\admin\_base.html__: layout base para templetes
            - __.\templates\admin\index.html__: templates (herdeiro do layout base)
            - __.\templates\admin\menu.html__: template (agrupamento de rotas para serviços administrativo pasta __.\templates\admin__)
            - area:
                - __.\templates\admin\area\list.html__: templates (pagina principal de serviços = listagem de dados)
                - __.\templates\admin\area\create.html__: templates (criar dados)
                - __.\templates\admin\area\details.html__: templates (exibir detalhes de dados)
                - __.\templates\admin\area\edit.html__: templates (editar dados)
            - autor:
                - __.\templates\admin\autor\list.html__: templates (pagina principal de serviços = listagem de dados)
                - __.\templates\admin\autor\create.html__: templates (criar dados)
                - __.\templates\admin\autor\details.html__: templates (exibir detalhes de dados)
                - __.\templates\admin\autor\edit.html__: templates (editar dados)
            - comentario:
                - __.\templates\admin\comentario\list.html__: templates (pagina principal de serviços = listagem de dados)
                - __.\templates\admin\comentario\create.html__: templates (criar dados)
                - __.\templates\admin\comentario\details.html__: templates (exibir detalhes de dados)
                - __.\templates\admin\comentario\edit.html__: templates (editar dados)
            - duvida:
                - __.\templates\admin\duvida\list.html__: templates (pagina principal de serviços = listagem de dados)
                - __.\templates\admin\duvida\create.html__: templates (criar dados)
                - __.\templates\admin\duvida\details.html__: templates (exibir detalhes de dados)
                - __.\templates\admin\duvida\edit.html__: templates (editar dados) 
            - menbro:
                - __.\templates\admin\membro\list.html__: templates (pagina principal de serviços = listagem de dados)
                - __.\templates\admin\membro\create.html__: templates (criar dados)
                - __.\templates\admin\membro\details.html__: templates (exibir detalhes de dados)
                - __.\templates\admin\membro\edit.html__: templates (editar dados)
            - modals:
                - __.\templates\admin\modals\delete.html__: templates (excluir registro no Banco de Dados)
            - post:
                - __.\templates\admin\post\list.html__: templates (pagina principal de serviços = listagem de dados)
                - __.\templates\admin\post\create.html__: templates (criar dados)
                - __.\templates\admin\post\details.html__: templates (exibir detalhes de dados)
                - __.\templates\admin\post\edit.html__: templates (editar dados)
            - projeto:
                - __.\templates\admin\projeto\list.html__: templates (pagina principal de serviços = listagem de dados)
                - __.\templates\admin\projeto\create.html__: templates (criar dados)
                - __.\templates\admin\projeto\details.html__: templates (exibir detalhes de dados)
                - __.\templates\admin\projeto\edit.html__: templates (editar dados)
            - tag:
                - __.\templates\admin\tag\list.html__: templates (pagina principal de serviços = listagem de dados)
                - __.\templates\admin\tag\create.html__: templates (criar dados)
                - __.\templates\admin\tag\details.html__: templates (exibir detalhes de dados)
                - __.\templates\admin\tag\edit.html__: templates (editar dados)
        - views:
            - __home_view.py__: Gerecimento das rotas paginas principais (publicas)
            - __error_view.py__: Código personalizados de exceções HTML 404 e 500.  
            - admin:
                - __admin_view.py__: Agrupa as rotas dos serviços administrativo (__.\templates\admin__)
                - __base_crud_view.py__: Estrutura genérica de INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__ (compartilha recursos)
                - __membro_admin.py__: INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__
                - __area_admin.py__: INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__
                - __autor_admin.py__: INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__
                - __comentario_admin.py__: INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__
                - __duvida_admin.py__: INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__
                - __post_admin.py__: INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__
                - __projeto_admin.py__: INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__
                - __tag_admin.py__: INTEGRAÇÃO dos serviços (CRUD) do __.\controllers__
        - __main.py__: Personalização de tratamento de erros (__.\templates\404.html__ e __.\templates\500.html__)
---

**Aula_29**
- __Projeto FastAPI Website__

- Resumo da aplicação:
    - 01 => __main.py__: Ativação da API, acesso as rotas HTML e arquivos estáticos.
    - 02 => __Pasta media__: Armazenamentos de downloads.
    - 03 => __Pasta templates__: Gerencia paginas HTML de liver acesso (publico) 
        -   03.1 => __Pasta .\templates\admin__: Gerencia paginas HTML de acesso administrativo (restrito)
    - 04 => __Pasta core__: Configuração do Banco de Dados.
    - 05 => __Pasta model__: Modelagem do Banco de dados, INTERAÇÃO DIRETA com Banco de Dados (__Pasta core__).
    - 06 => __Pasta controllers__: Gerenciamento dos recursos (CRUD) entrada e saída da API, INTERAÇÃO INDIRETA com Banco de Dados (Pasta model).
    - 07 => __Pasta views__: Gerenciamento de rotas templates HTML (Pasta templates)
        -   07.1 => __Pasta .\views\admin__: Faz INTERAÇÃO DIRETA do serviços (CRUD) da (Pasta controllers) e alimentação de dados em paginas HTML de acesso restrito (Sub pasta .\templates\admin)

- Simplificação de código:

- Pasta e arquivos:
    - controllers:
        - __.\controllers\base_controller.py__: (recursos) => Adição de (Métodos genéricos)
        - __.\controllers\autor_controller.py__: (recursos) => Implementação (Métodos genéricos) em "post_crud" e "put_crud"
        - __.\controllers\post_controller.py__: (recursos) => Implementação (Métodos genéricos) em "post_crud" e "put_crud"
    - views: 
        - admin:
            - __base_crud_view.py__: Adição de rotas na classe (BaseCrudView) para CLASSES FILHAS
            - __membro_admin.py__: Simplificação de rotas para CLASSE PAI
            - __area_admin.py__: Simplificação de rotas para CLASSE PAI
            - __autor_admin.py__: Simplificação de rotas para CLASSE PAI
            - __comentario_admin.py__: Simplificação de rotas para CLASSE PAI
            - __duvida_admin.py__: Simplificação de rotas para CLASSE PAI
            - __post_admin.py__: Simplificação de rotas para CLASSE PAI
            - __projeto_admin.py__: Simplificação de rotas para CLASSE PAI
            - __tag_admin.py__: Simplificação de rotas para CLASSE PAI
    - templates:
        - admin:
            - area:
                - __.\templates\admin\area\list.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\area\create.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\area\details.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\area\edit.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
            - autor:
                - __.\templates\admin\autor\list.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\autor\create.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\autor\details.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\autor\edit.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
            - comentario:
                - __.\templates\admin\comentario\list.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\comentario\create.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\comentario\details.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\comentario\edit.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
            - duvida:
                - __.\templates\admin\duvida\list.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\duvida\create.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\duvida\details.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\duvida\edit.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
            - menbro:
                - __.\templates\admin\membro\list.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\membro\create.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\membro\details.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\membro\edit.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
            - post:
                - __.\templates\admin\post\list.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\post\create.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\post\details.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\post\edit.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
            - projeto:
                - __.\templates\admin\projeto\list.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\projeto\create.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\projeto\details.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\projeto\edit.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
            - tag:
                - __.\templates\admin\tag\list.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\tag\create.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\tag\details.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
                - __.\templates\admin\tag\edit.html__: Alteração link's nome "obj_id" para as rotas em __base_crud_view.py__
---

**Aula_30**
- __Projeto FastAPI Website, Segurança e Autenticação__

- Adição de senha e email:

- Pasta e arquivos:
    - model:
        - __.\model\membro_model.py__: Adição de senha e email
    - controllers:
        - __.\controllers\membro_controller.py__: Adição de senha e email
    - views:
        - admin:
            - __.\views\admin\membro_admin.py__: Adição de senha e email
            - __.\views\admin\base_crud_views.py__: Substituição de Route por APIRoute
            - __.\views\admin\admin_views.py__: Eliminação de (prefix="/admin") devido mudança de Route por APIRoute
    - templates:
        - admin:
            - membro:
                - __.\templates\admin\membro\create.html__: Adição de senha e email
                - __.\templates\admin\membro\edit.html__: Adição de senha e email
                - __.\templates\admin\membro\details.html__: Adição de senha e email
                - __.\templates\admin\membro\list.html__: Adição de senha e email
---

**Aula_31**
- __Projeto FastAPI Website, Segurança e Autenticação__

- Adição de login e criptografia hash:
- Pasta e arquivos:
    - views:
        - __.\views\home_views.py__: Adição de login
    - templates:
        - __.\templates\base.html__: Adição de login
        - __.\templates\login.html__: Criação do login


**Aula_32**
- __Projeto FastAPI Website, Segurança e Autenticação__

- Adição de logout, criptografia hash e cookie de autenticação no navegador:
- Pasta e arquivos:
    - core:
        - __.\core\configs.py__: Adição de autenticação (auth_cookie) e criptografia (SALTY)
        - __.\core\auth.py__: Gerenciamento de criptografia (auth_cookie)
    - views:
            - __.\views\home_views.py__: Adição de logout, (criar e fechar) login c/ autenticação (auth_cookie)
    - templates:
        - admin:
            - modals:
                - __.\templates\admin\modals\logout.html__: Criação do logout
            - __.\templates\admin\_base.html__: Inclusão de "__.\templates\admin\modals\logout.html__"
            - __.\templates\admin\limbo.html__: Pagina para usuário não autorizados por (auth_cookie)
    - static:
        - admin:
            - img:
                - __static\admin\img\shall.jpg__: Imagem para paginal "__.\templates\admin\limbo.html__"
    - controller:
        - __.\membro_controller.py__: Gerar e validar "hash senha" do Banco de Dados
---

**Aula_33**
- __Projeto FastAPI Website, Segurança e Autenticação__

- Middlewares de seguração:
    - Middlewares: são componentes intermediários que interceptam requisições e respostas para aplicar medidas de proteção à aplicação, antes que elas cheguem às rotas ou depois que saem delas. Como autenticação por Token, controle de acesso de recursos por usuário, limitação de requisições opr usuário e etc.

- Pasta e arquivos:
    - core:
        - __.\core\deps.py__: Validação de login cadastrado no Banco de Dados
    - views: 
        - admin:
            - __.\views\admin\admin_view.py__: Adição de validação de login "__.\core\deps.py__"
            - __.\views\admin\membro_admin.py__: Adição de validação de login "__.\core\deps.py__" 
            - __.\views\admin\area_admin.py__: Adição de validação de login "__.\core\deps.py__" 
            - __.\views\admin\autor_admin.py__: Adição de validação de login "__.\core\deps.py__"
            - __.\views\admin\base_crud_view.py__: Adição de validação de login "__.\core\deps.py__" 
            - __.\views\admin\comentario_admin.py__: Adição de validação de login "__.\core\deps.py__"
            - __.\views\admin\duvida_admin.py__: Adição de validação de login "__.\core\deps.py__"
            - __.\views\admin\post_admin.py__: Adição de validação de login "__.\core\deps.py__"
            - __.\views\admin\projeto_admin.py__: Adição de validação de login "__.\core\deps.py__"
            - __.\views\admin\tag_admin.py__: Adição de validação de login "__.\core\deps.py__"
    - __main.py__: Adição de Middlewares

- __deps.py__: Limita acesso direto do usuário em paginas administrativas HTML, sem efetuar login
---

**Aula_Any_e_object**
- __Any__ faz parte do módulo typing e é usado para indicar que uma variável, argumento ou retorno de função pode ser de qualquer tipo.

- __object__ é a superclasse base de todas as classes — representa qualquer coisa.

- Portanto, quando você escreve model: object, está dizendo que model pode ser qualquer instância de qualquer classe — o tipo mais genérico possível, em resumo:

    - __object__: mais seguro, mas mais restritivo para autocompletar/verificação de tipo.

    - __Any__: mais flexível, mas perde segurança de tipo (é como desligar o verificador de tipos).
---

**SQLAlchemy**
- __SQLAlchemy__ é uma biblioteca de __ORM__ (__Object-Relational Mapping__) em Python que permite interagir com bancos de dados usando classes e objetos, abstraindo as consultas SQL complexas.
---

**SQLITE**
- Criação de banco de dados __SQLite__ via programação Python com pré-registos. 
---

**Token_JWT**
- Cria um token seguro e aleatório para "JWT_SECRET" em uma eventual autenticação "JWT".
---

**JWT**
- __JWT__ (JSON Web Tokens) é um padrão para autenticação e troca de informações de forma segura entre partes, utilizando um token assinado digitalmente.

### Link: [JWT](JWT/JWT.md)

---

**CryptContext**
- Criptografia de texto por meio de hash
- __CryptContext__ é uma classe do Passlib que facilita a configuração e o gerenciamento de algoritmos de hash de senha. Compara a senha fornecida com o hash armazenado e retorna True se forem equivalentes. Não é possível "descriptografar".
---

**CRIPTO**
- Criptografia de texto por meio de hash e autenticação.
- Uso pratico de __CryptContext__ e __JWT__:
    - from passlib.context import CryptContext
    - from jose import jwt
---

**GERADOR_de_SALTY**
- Cria um token seguro e aleatório para SALTY.
    - SALTY é uma string usada como sal criptográfico para reforçar a segurança na geração de hashes.
---

**DECIMAL_HEXADECIMAL**
- Conversão de valores decimal para exa decimal
---

**UUID4**
Gerador e validação de UUID4 (strings de 36 caracteres alfanuméricos aleatórios)
- Diferença entre uuid4() e UUID4
    - uuid4() (da biblioteca uuid) gera um novo UUID aleatório.
    - UUID4 (do Pydantic) é apenas um tipo para validação, usado principalmente em parâmetros e campos de modelo.

- Aplicação de uuid4() e UUID4 na prática
    - Esses dois são usados principalmente para identificar registros de forma única em aplicações, especialmente APIs e bancos de dados.
---

**DOCUMENTOS_EM_PDF**
- Arquivos em PDF sobre REST APIS.
---
