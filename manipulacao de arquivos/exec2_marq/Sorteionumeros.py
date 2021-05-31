class Jogo:
    numeroSorteio = None

    dataSorteio = None

    numerosSorteados = None

    qtdeDezenasSorteadas = None

    def __init__(self, qtdeDezenasSorteadas):
        self.numeroSorteio = 0

        self.dataSorteio = ""

        self.numerosSorteados = []

        self.qtdeDezenasSorteadas = qtdeDezenasSorteadas


class Cont:
    cont = {}
    def contnumeros(self, listaNumeros):
        for x in range(1, 61):
            self.cont[str(x)]= listaNumeros.count(x)
            sorted(self.cont.items())





