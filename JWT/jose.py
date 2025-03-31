from jose import jwt

SECRET_KEY = "tpovt7mE-X7vJFb8xfPQFf6Ife6Pxn6MEzXdJtUYojY" # Chave usada para assinar o token
ALGORITHM = "HS256" # Define o algoritmo de hashing 

# Gerando um token
data = {"sub": "user123", "name": "João"}
token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM) # Codificar
print(token)

# Decodificando o token
decoded_token = jwt.decode(token, key=None, options={"verify_signature": False}) #  Decodificar
print(decoded_token)

'''
    No entanto, ao passar "key=None" e "options={"verify_signature": False}", 
    estamos ignorando a verificação da assinatura, permitindo que apenas 
    o conteúdo do payload seja extraído
'''