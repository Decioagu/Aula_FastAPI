from jose import jwt

SECRET_KEY = "tpovt7mE-X7vJFb8xfPQFf6Ife6Pxn6MEzXdJtUYojY" # Chave usada para assinar o token
ALGORITHM = "HS256" # Define o algoritmo de hashing 

# Gerando um token
senha = {"senha": 123} # DICIONARIO
token = jwt.encode(senha, SECRET_KEY, algorithm=ALGORITHM) # Codificar
print(token)

# Decodificando o token
decoded_token = jwt.decode(token, SECRET_KEY, options={"verify_signature": False}) #  Decodificar
print(decoded_token)

'''
    No entanto, ao passar "SECRET_KEY" e "options={"verify_signature": False}", 
    estamos ignorando a verificação da assinatura, permitindo que apenas 
    o conteúdo do payload seja extraído

    jwt.decode(token, key, algorithms, options=None, audience=None, issuer=None)

Parâmetro	    Obrigatório?	Descrição
token	✅      Sim	           O token JWT a ser decodificado.
key	✅          Sim	           Chave secreta (para HS256) ou chave pública (para RS256).
algorithms	    Sim	            Algoritmos aceitos, ex: ["HS256"], ["RS256"].
options	❌      Não	           Dicionário com opções adicionais (exemplo: verify_exp=False para ignorar a expiração).
audience	    Não             Verifica se o aud no token corresponde ao valor esperado.
issuer	❌      Não	           Verifica se o iss no token corresponde ao valor esperado.


'''