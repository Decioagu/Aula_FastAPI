# ================= CONFIGURAÇÃO DE "HASH" SENHA =======================
from passlib.context import CryptContext

# Configuração do hash de senha
CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Função para verificar senha
def verificar_senha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

# Função para obter hash de senha
def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)

'''
- CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto'):

    Gera senha segura criptografada no Banco de Dados, se um 
    usuário se cadastra com a senha "minha_senha123", em vez de 
    salvar isso diretamente no Banco de Dados o "hash" salva assim:

    $2b$12$z6D4JHPM1pYYtUq8kGvF6OvTswXaJLoeRctGJY3rO.z2ToihG6hE2

    - CryptContext(schemes=["bcrypt"]): 
        Define que o algoritmo de "hash" utilizado será o bcrypt 
        (considerado seguro e amplamente usado).

    - deprecated="auto": 
        Permite que o sistema continue aceitando senhas com 
        "hash" antigos caso o esquema seja atualizado no futuro.
'''