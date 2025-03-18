from passlib.context import CryptContext

# Configuração do hash de senha
CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Função para verificar senha
def verificar_senha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

# Função para obter hash de senha
def gerar_hash_senha(senha: str) -> str:

    return CRIPTO.hash(senha)
