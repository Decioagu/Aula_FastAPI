

# Meus módulos
from models.usuario_model import UsuarioModel
from config.conf_db import settings

# ================== CONFIGURAÇÃO DE HASH SENHA ========================
from passlib.context import CryptContext
'''
Gera senha do usuário e armazena de forma segura no Banco de Dados (hash seguro):

Exemplo :
Se um usuário se cadastra com a senha "minha_senha123", em vez de 
salvar isso diretamente no banco o (hash seguro) salva assim:

$2b$12$z6D4JHPM1pYYtUq8kGvF6OvTswXaJLoeRctGJY3rO.z2ToihG6hE2
'''

# Configuração do hash de senha
CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')
'''
    - CryptContext(schemes=["bcrypt"]): Define que o algoritmo de hash utilizado 
    será o bcrypt (considerado seguro e amplamente usado).

    - deprecated="auto": Permite que o sistema continue aceitando senhas com 
    hashes antigos caso o esquema seja atualizado no futuro.
'''

# Função para verificar senha
def verificar_senha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

# Função para obter hash de senha
def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)

# ======================= AUTENTICAÇÃO ============================
from pytz import timezone # manipular fusos horários em Python
from typing import Optional
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer # Autorização em APIs
from sqlalchemy.future import select # Consultas assíncronas
from sqlalchemy.ext.asyncio import AsyncSession #  Interação Bancos de Dados assíncrona
from jose import jwt # Autorização (JSON Web Token)
from pydantic import EmailStr # Permitindo a validação automática de endereços de e-mail validos

# Endpoint para autenticação token
oauth2_schema = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/usuarios/login")

# Autentica senha e usuário por e-mail
async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email) # Filtra
        result = await session.execute(query) # Executa Banco de Dados
        usuario: UsuarioModel = result.scalars().unique().one_or_none() # Extrai

        # Se usuário não existir
        if not usuario:
            return None

        # Se senha não existir
        if not verificar_senha(senha, usuario.senha):
            return None

        return usuario

# Função (Regra criação de Token)
def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    # Dicionario
    payload = {}

    sp = timezone('America/Sao_Paulo') # Horário Global de São Paulo
    # expira = hora SP + conf_db.py(ACCESS_TOKEN_EXPIRE_MINUTES)
    expira = datetime.now(tz=sp) + tempo_vida

    # Campo de autenticação (https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3)
    payload["type"] = tipo_token

    payload["exp"] = expira

    payload["iat"] = datetime.now(tz=sp)

    payload["sub"] = str(sub)

    # Codificar autenticação JWT
    # biblioteca(Dicionário, conf_db.py(JWT_SECRET), algorithm=conf_db.py(ALGORITHM))
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM) 

# Gerar Token de acesso (Execução)
def criar_token_acesso(sub: str) -> str:
    """
    https://jwt.io
    """
    # Função (Regra criação de Token)
    return _criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )
