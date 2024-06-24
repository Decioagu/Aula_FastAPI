'''
O FastAPI é um framework web moderno, rápido e de alto desempenho para criar APIs RESTful 
e GraphQL com Python. Ele é baseado em type hints do Python e oferece diversas 
funcionalidades que facilitam o desenvolvimento de APIs robustas e escaláveis.
Aula_01 copy'''
from fastapi import FastAPI

# instanciar API
app = FastAPI()

# rota 
@app.get('/') # base da pagina
async def msg(): # função da rota
    return {"msg": "Décio santana de Aguiar"} # mensagem

if __name__ == 'main':
    '''
    "import uvicorn" 
    permite que você use o servidor web ASGI para 
    executar aplicativos web Python assíncronos
    '''
    from uvicorn import run # subir o servidor

    run('main:app', host="127.0.0.1", port=8000, log_level='info', reload=True)
    # # run('main:app', host="0.0.0.0", port=8000, log_level='info', reload=True)


    '''
Parâmetros run(<nome_arquivo>:app, host, port, log_level, reload):

    # <nome_arquivo>:app (obrigatório): Este argumento representa o aplicativo ASGI 

    # host (opcional, padrão: "0.0.0.0"): endereço IP no qual o aplicativo escutará as 
    solicitações recebidas ("0.0.0.0" ou "127.0.0.1": localhost)

    # port (opcional, padrão: 8000): Este argumento define o número da porta na qual 
    o aplicativo escutará o tráfego. 

    # log_level (opcional, padrão: "info"): Este parâmetro controla o detalhamento 
    das mensagens de log emitidas pelo Uvicorn durante a execução do aplicativo. 
        Os valores possíveis incluem:
        "debug": mostra todas as mensagens de registro (mais detalhadas).
        "info"(padrão): Mostra mensagens informativas.
        "warning": mostra avisos e erros.
        "error": Mostra apenas erros.

    # reload (opcional, padrão: True): Esta configuração permite o recarregamento automático 
    '''