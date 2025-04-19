# ============================= CLASS =====================================
class Pessoa:
    def __init__(self, id, senha): # iniciar classe (construtor)
        self.id = id # atributo
        self.senha = senha # atributo

pessoa1 = Pessoa( 1, "dsa") ### ADICIONAR DADOS (atributo)

# =============================== CryptContext ===================================
from passlib.context import CryptContext

# Configuração do hash de senha
CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Função para verificar senha
def verificar_senha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

# Função para obter hash de senha
def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)

senha = gerar_hash_senha('dsa') ### ADICIONAR SENHA
# ================================ JWT ==================================

from jose import jwt

SECRET_KEY = "tpovt7mE-X7vJFb8xfPQFf6Ife6Pxn6MEzXdJtUYojY" # Chave usada para assinar o token
ALGORITHM = "HS256" # Define o algoritmo de hashing 

def criar_senha(senha):
    return jwt.encode(senha, SECRET_KEY, algorithm=ALGORITHM)

def ver_senha(token):
    return jwt.decode(token, SECRET_KEY, options={"verify_signature": False})

senha1 = {"id": pessoa1.id, "senha": pessoa1.senha} ### DADOS DA CLASS

senha_codificada = criar_senha(senha1) ### CODIFICAR SENHA DA CLASS
print(senha_codificada)
# ==================================================================

senha_decodificada = ver_senha(senha_codificada) ### DECODIFICAR SENHA DA CLASS
print(senha_decodificada['senha'])

# ==================================================================

### COMPARAR SENHA
if verificar_senha(senha_decodificada['senha'], senha):
    print('Verdade')
else:
    print('Falso')


