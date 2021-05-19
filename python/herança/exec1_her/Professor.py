from Pessoa import Pessoa


class Professor(Pessoa):
    salario = None
    curriculo = None

    def __init__(self):
        super().__init__()
        self.salario = ("R$ " + str(0.00))
        self.curriculo = ''

    def setsalario(self):
        self.salario = ('R$' + input('insira o valor do salario do professor:'))

    def getsalario(self):
        return self.salario

    def setcurriculo(self):
        self.curriculo = input('insira o curriculo do professor')

    def getcurriculo(self):
        return self.curriculo

    def printcurriculo(self):
        print(self.curriculo)
