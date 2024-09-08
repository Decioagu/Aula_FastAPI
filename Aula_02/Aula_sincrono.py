from time import sleep, time

start_time = time()

class BobEspoja:
    def preparar_pao(self):
        print('Preparando pão')
        sleep(3)
        print(f'Pão finalizado: {(time() - start_time):.0f} segundos')
    def preparar_hamburger(self):
        print('Fritar hamburger')
        sleep(10)
        print(f'Hamburger finalizado: {(time() - start_time):.0f} segundos')
    def montar_sanduiche(self):
        print('Montar sanduíche')
        sleep(5)
        print(f'Sanduíche finalizado: {(time() - start_time):.0f} segundos')
    def fazer_milkshake(self):
        print('Fazendo milkshake')
        sleep(10)
        print(f'Milkshake finalizado: {(time() - start_time):.0f} segundos')

    def pedido(self):
        self.preparar_pao()
        self.preparar_hamburger()
        self.montar_sanduiche()
        self.fazer_milkshake()

cliente = BobEspoja()
cliente.pedido()
print()
print(f'Tudo pronto, pedido finalizado em {(time() - start_time):.0f} segundos')