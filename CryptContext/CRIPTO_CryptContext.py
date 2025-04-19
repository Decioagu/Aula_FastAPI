from passlib.context import CryptContext

# Configuração do hash de senha
CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Função para verificar senha
def verificar_senha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

# Função para obter hash de senha
def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)

gerar_hash_senha('dsa')

print(gerar_hash_senha('dsa'))

print(verificar_senha('dsa', '$2b$12$sqCVoZohUtY8E3F2ols/veMy.3F933ernJigxoYb9yo.Kmz6mJ93O'))

'''
OBS: O hash gerado pelo CryptContext é irreversível. Isso significa 
que não é possível converter o hash de volta para a senha original.
'''
