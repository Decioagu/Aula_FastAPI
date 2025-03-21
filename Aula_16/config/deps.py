from typing import Optional
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession #  Interação Bancos de Dados assíncrona
from pydantic import BaseModel # Modelagem

# Meus módulos
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from config.conf_db import settings, get_session
from config.aut_jwt import oauth2_schema
from models.usuario_model import UsuarioModel

class TokenData(BaseModel):
    username: Optional[int] = None

# Dependência para obter usuário atual
async def get_current_user(db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_schema)) -> UsuarioModel: # type: ignore
   
    # Exceção ...
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possível autenticar a credencial',
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decodificar autenticação JWT
        payload = jwt.decode(
            token,
            settings.JWT_SECRET, # conf_db.py(JWT_SECRET)
            algorithms=[settings.ALGORITHM], # algorithm=conf_db.py(ALGORITHM)
            options={"verify_aud": False} # Parâmetro extra não obrigatório
        )

        # Buscar Token decodificada 
        username: str = payload.get("sub")

        # Se Token não existir
        if username is None:
            raise credential_exception # Exceção ...

        # Comparar Token
        token_data: TokenData = TokenData(username=username)

    except JWTError:
        raise credential_exception # Exceção ...

    # Buscar Id de usuário no Banco de Dados é o mesmo que Token decodificado
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == int(token_data.username)) # Filtro
        result = await session.execute(query) # Executar Banco de Dados
        usuario: UsuarioModel = result.scalars().unique().one_or_none() # Extrair

        # Se usuário não existir no Banco de Dados
        if usuario is None:
            raise credential_exception # Exceção ...

        return usuario
