# from jose import jwt VS import jwt

## from jose import jwt

Está importando o módulo jwt da biblioteca python-jose.

Biblioteca: python-jose

Finalidade: manipulação de JWTs (JSON Web Tokens) e outras assinaturas criptográficas (JWE, JWS, JWK).

### Comando de instalação:
````
pip install python-jose
````

### Exemplo de uso:
````
from jose import jwt

SECRET_KEY = "segredo123"
ALGORITHM = "HS256"
````
### Gerar token
````
token = jwt.encode({"user_id": 1}, SECRET_KEY, algorithm=ALGORITHM)
print(token)
````
### Decodificar token
````
dados = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print(dados)
````

- Características principais:
    - Totalmente compatível com o padrão JWT.
    - Amplamente usado no FastAPI.
    - Suporta múltiplos algoritmos de criptografia (HS256, RS256, etc.).
    - Sintaxe simples e direta.

## import jwt

Está importando o módulo jwt da biblioteca PyJWT.

Biblioteca: PyJWT

Finalidade: também cria e valida JWTs, mas não é a mesma implementação.

### Comando de instalação:
````
pip install PyJWT
````

### Exemplo de uso:
````
import jwt

SECRET_KEY = "segredo123"
ALGORITHM = "HS256"
````

### Gerar token
````
token = jwt.encode({"user_id": 1}, SECRET_KEY, algorithm=ALGORITHM)
print(token)
````

### Decodificar token
dados = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print(dados)


- Características principais:
    - Biblioteca mais simples e leve.
    - Foca apenas em JWT (não JWE, JWS, etc.).
    - Muito usada em projetos Django ou Flask.

## Diferenças principais
- Aspecto	python-jose (from jose import jwt)	PyJWT (import jwt)
- Instalação	pip install python-jose	pip install PyJWT
- Namespace	from jose import jwt	import jwt
- Suporte a criptografia avançada	✅ Sim (JWE, JWS, JWK)	❌ Não
- Compatível com FastAPI (tutoriais oficiais)	✅ Sim	⚠️ Funciona, mas menos usado
- Retorno do jwt.encode()	str	str (PyJWT ≥ 2.0) ou bytes (versões antigas)
- Erros comuns	JWTError, ExpiredSignatureError	InvalidTokenError, ExpiredSignatureError
💡 
- Dica prática:
    - Se você está usando FastAPI, o mais recomendado é: from jose import jwt, JWTError
    - Isso garante compatibilidade com os exemplos oficiais e com a forma como FastAPI lida com autenticação JWT.