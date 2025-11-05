from typing import Any

def process_data(data: Any = None) -> None:
    print(f"Recebido: {data}")

process_data()
process_data("Texto")   # Ok
process_data(123)       # Ok
process_data([1, 2, 3]) # Ok

print(f"-" * 20)

from typing import Optional

def process_data(data: Optional[object] = None) -> None:
    print(f"Recebido: {data}")

process_data()
process_data("Texto")   # Ok
process_data(123)       # Ok
process_data([1, 2, 3]) # Ok
'''
 Diferença entre object e Any


object:	Tipo base de tudo, mas o mypy e o editor não sabem o que ele pode fazer.
        Você não pode acessar atributos/métodos sem erro de tipo é mais seguro é
        mais restritivo para autocompletar/verificação de tipo.

Any:    Tipo especial que aceita tudo e permite tudo — o tipo mais permissivo.
        O verificador de tipos não faz nenhuma verificação é  mais flexível, 
        porem perde segurança de tipo (é como desligar o verificador de tipos).
'''

