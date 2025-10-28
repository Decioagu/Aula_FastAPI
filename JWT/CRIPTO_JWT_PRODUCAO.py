from jose import jwt

SECRET_KEY = "tpovt7mE-X7vJFb8xfPQFf6Ife6Pxn6MEzXdJtUYojY" # Chave usada para assinar o token
ALGORITHM = "HS256" # Define o algoritmo de hashing 

# Gerando um token
dados = {"sub": "user123", "name": "João"} # DICIONARIO
token = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM) # Codificar
print(token)

'''
    GERADOR DE TOKEN

    jwt.encode(token, key, algorithms, options=None, audience=None, issuer=None)

Parâmetro	    Obrigatório?	Descrição
token	✅      Sim	           O token JWT a ser decodificado (dados).
key	✅          Sim	           Chave secreta para HS256 (SECRET_KEY).
algorithms	    Sim	            Algoritmos hashing, exemplo: ["HS256"], ["RS256"].
options         Não             Desativa a verificação da assinatura do token (exemplo: verify_exp=False para ignorar a expiração).
audience        Não             Define o campo "aud" (público-alvo do token). Serve para validar quem deve aceitar o token.
issuer          Não             Define o campo "iss" (emissor do token). Serve para validar quem deve emitir o token.
'''

# Decodificando o token
decoded_token = jwt.decode(token, SECRET_KEY, options={"verify_signature": False}) #  Decodificar
print(decoded_token)

'''
    DECODIFICADOR

    jwt.decode(token, key, algorithms, options=None, audience=None, issuer=None)

Parâmetro	    Obrigatório?	Descrição
token	✅      Sim	           O token JWT a ser decodificado (senha).
key	✅          Sim	           Chave secreta para HS256 (SECRET_KEY).
options	❌      Não	           Desativa a verificação da assinatura do token (exemplo: verify_exp=False para ignorar a expiração).
audience        Não             Define o campo "aud" (público-alvo do token). Serve para validar quem deve aceitar o token. (options={"verify_aud": False})
issuer          Não             Define o campo "iss" (emissor do token). Serve para validar quem deve emitir o token. (options={"verify_iss": False})
'''