

# ========================= CAMINHO ARQUIVO SQLite ==============================
from pathlib import Path # Pasta

# Criando uma engine para um banco SQLite (ou pode ser MySQL, PostgreSQL etc.)
caminho_do_arquivo = Path(__file__).parent.parent

# ========================= ROTAS API (RECURSOS) ===============================
# ======================= CONEXÃO BANCO DE DADOS ===============================
from pydantic_settings import BaseSettings

#  Gerenciar configurações de aplicativos
class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1' # anotação rota
    DB_URL: str = f"sqlite+aiosqlite:///{caminho_do_arquivo}/faculdade.db" # SQLite
    # DB_URL: str = 'mysql+aiomysql://root:Enigma.1@localhost:3306/faculdade' # MySQL

    JWT_SECRET: str = 'qS96E1oCfq5gEZH-ngD91NC2qkcl0cffhNTIDGpF4pw' # senha gerada em Token_JWT.py
    '''
    HS256 (HMAC + SHA-256): define o algoritmo de criptografia utilizado 
    para assinar e verificar os tokens JWT (JSON Web Token).
    
    - HS significa HMAC (Hash-based Message Authentication Code).
    - 256 refere-se ao uso do SHA-256 (Secure Hash Algorithm 256 bits) como função de hash.
    - O HMAC usa uma chave secreta (JWT_SECRET) para assinar e validar o token.
    '''
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # Tempo de acesso ao token

    # Define que as variáveis de ambiente no Pydantic devem ser sensíveis a maiúsculas e minúsculas.
    class Config:
        case_sensitive = True

settings = Settings()

# ========================= SESSÃO BANCO DE DADOS =============================
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

# conexão do Banco de Dados (ENDEREÇO BANCO DE DADOS)
engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=False)

# Cria sessão de Banco de Dados assíncrono (INTERAÇÃO)
Session: AsyncSession = sessionmaker(
    autocommit=False, # não faz "commit" automaticamente
    autoflush=False, # não executar consulta automáticas 
    expire_on_commit=False, # sessão não aspirá apos "commit"
    class_=AsyncSession, #  sessão assíncrono
    bind=engine # ativa conexão com o banco de dados
)
# ================= SESSÃO COMMIT (ABERTURA E FECHAMENTO) ======================
from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

# consulta no Banco de Dados
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session # Abrir sessão
    finally:
        await session.close() # Fechar sessão

# ============================================================================
# async def get_current_user(db: Session = Depends(get_session), token: str = Depends(oauth2_schema)) -> UsuarioModel:
#     credential_exception: HTTPException = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail='Não foi possível autenticar a credencial',
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     try:
#         payload = jwt.decode(
#             token,
#             settings.JWT_SECRET,
#             algorithms=[settings.ALGORITHM],
#             options={"verify_aud": False}
#         )

#         username: str = payload.get("sub")
#         if username is None:
#             raise credential_exception

#         token_data: TokenData = TokenData(username=username)
#     except JWTError:
#         raise credential_exception

#     async with db as session:
#         query = select(UsuarioModel).filter(
#             UsuarioModel.id == int(token_data.username))
#         result = await session.execute(query)
#         usuario: UsuarioModel = result.scalars().unique().one_or_none()

#         if usuario is None:
#             raise credential_exception

#         return usuario

