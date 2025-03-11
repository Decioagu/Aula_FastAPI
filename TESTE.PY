
# Modelo 1:
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# Adiciona ao sys.path o próprio diretório onde o script está sendo executado (__file__).

# Modelo 2:
import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Adiciona o diretório pai (diretório acima do diretório onde o script está) ao sys.path.

'''
Ambos os códigos Python têm o objetivo de modificar o sys.path:
Suponha a seguinte estrutura de diretórios:

projeto/
├── principal.py
├── modulo_auxiliar.py
└── subdiretorio/
    └── outro_modulo.py
Se (principal.py) usar o Modelo 1, ele poderá importar (modulo_auxiliar.py) diretamente.
Se (principal.py) usar o Modelo 2, ele poderá importar (outro_modulo.py) de subdiretorio/.
'''