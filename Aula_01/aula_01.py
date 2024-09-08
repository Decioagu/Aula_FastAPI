import asyncio

'''
Python: "async" e "await"

Assíncrono é aguardar.

Em Python, "async" e "await" são palavras-chave que trabalham juntas 
para habilitar a programação assíncrona. Isso significa que seu programa 
pode lidar com várias tarefas simultaneamente sem bloquear o thread principal. 
Isso é particularmente útil para operações vinculadas a solicitações de rede 
ou acesso ao sistema de arquivos, onde você pode passar muito tempo aguardando.
'''

# sincrono
def soma_01(a, b):
    return a + b

resultado_01 = soma_01(1,3)
print(resultado_01)
print()
# ------------------------------------------

# assíncrono
async def soma_02(a, b):
    return a + b

resultado_02 = soma_02(1,3)
print(resultado_02)
print()

# ------------------------------------------

# assíncrono
async def soma_03(a, b):
    return a + b

resultado_03 = soma_03(1,3)
# execução de função assíncrona
event_loop_03 = asyncio.new_event_loop()
final = event_loop_03.run_until_complete(resultado_03)
print(final)

# -------------------- OU ----------------------

# assíncrono
async def soma_04(a, b):
    return a + b
# execução de função assíncrona
print(asyncio.run(soma_04(1,3)))

# ======================================================================

# assíncrono
async def soma_05(a, b):
    return a + b

async def print_soma(a, b):
    resultado_05 = await soma_05(a, b)
    print(resultado_05)

print()
# execução de função assíncrona
event_loop_05 = asyncio.new_event_loop()
final = event_loop_05.run_until_complete(print_soma(1,3))

# -------------------- OU ----------------------

# assíncrono
async def soma_06(a, b):
    return a + b

async def print_soma(a, b):
    resultado_06 = await soma_06(a, b)
    print(resultado_06)

print()
# execução de função assíncrona
asyncio.run(print_soma(1,3))
