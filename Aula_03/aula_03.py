from pydantic import BaseModel, field_validator

'''
O "BaseModel" no Pydantic é uma classe base que permite a 
criação de modelos de dados com validação e tipagem automática:
    - Definição de tipos de dados: definir os tipos de dados no modelo como: 
    int, str, bool, float, etc.
    - Validação de dados: valida automaticamente os dados a ser inserido no modelo.
    - Serialização e desserialização: converter seus modelos de dados em diferentes
    formatos como: JSON, XML e CSV.
'''
# modelagem e validação tipo
class User(BaseModel):
    # (modelo: tipo)
    nome: str # tipagem
    idade: int # tipagem
    email: str # tipagem

    '''
    O módulo "field_validator" oferece uma ferramenta poderosa para personalizar
    validações complexas e específicas para atender às suas necessidades.
    '''
    @field_validator('idade')
    def validate_idade(cls, idade_valido):
        # Verifica se o valor de idade é positivo
        if idade_valido <= 0:
            raise ValueError('<========> idade: deve ser um inteiro positivo <========> \n')
        return idade_valido

    @field_validator('email')
    def validate_email(cls, email_valido):
        # Verifica se o email contém um "@"
        if '@' not in email_valido:
            raise ValueError('<========> email: deve conter "@" <========> \n')
        return email_valido

# Criação do objeto User
user = User(nome='Décio', idade=41, email="deciosan@gmail.com")
print(f'\n{user}\n')