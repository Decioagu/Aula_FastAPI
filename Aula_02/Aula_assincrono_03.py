from time import time
import asyncio

start_time = time()

class BobEsponja:

    start_time = time()
    async def preparar_pao(self):
        print('Preparando pão')
        await asyncio.sleep(3)
        print(f'Pão finalizado: {(time() - self.start_time):.0f} segundos')

    async def preparar_hamburger(self):
        print('Fritar hamburger')
        await asyncio.sleep(10)
        print(f'Hamburger finalizado: {(time() - self.start_time):.0f} segundos')

    async def montar_sanduiche(self):
        print('Montar sanduíche')
        await asyncio.sleep(5)
        print(f'Sanduíche finalizado: {(time() - self.start_time):.0f} segundos')
        print('montar_sanduiche')


    async def fazer_milkshake(self):
        print('Fazendo milkshake')
        await asyncio.sleep(7)
        print(f'Milkshake finalizado: {(time() - self.start_time):.0f} segundos')

    async def agilizar_sanduiche(self):
        await asyncio.gather(           
            self.preparar_hamburger(),
            self.preparar_pao()
        )
        '''
        "asyncio.get_running_loop()"
        Recuperando o loop de eventos atual: serve principalmente para recuperar 
        o loop de eventos que está sendo executado no momento no thread atual.
        '''
        event_loop = asyncio.get_running_loop()
        '''
        O "create_task()" é uma ferramenta poderosa para escrever código assíncrono 
        no Python. Ele permite que você execute corotinas de forma concorrente e 
        gerencie facilmente o ciclo de vida das tarefas.
        '''
        event_loop.create_task(self.montar_sanduiche())
        print(f'Agilizando...')

    async def pedido(self):
        await asyncio.gather(
            self.agilizar_sanduiche(), 
            self.fazer_milkshake()
        )
        print('Tudo pronto...')

cliente = BobEsponja()

# execução de função assíncrona
asyncio.run(cliente.pedido())


print(f'Pedido finalizado em {(time() - start_time):.0f} segundos')