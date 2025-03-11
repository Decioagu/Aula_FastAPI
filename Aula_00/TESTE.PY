import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from routes.rotas import x
print(x)

import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from routes.rotas import router as rotas

print(x)