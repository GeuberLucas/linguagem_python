
class Pessoa:
    nome = None
    end = None
    id = None

    def __init__(self):
        self.nome = ''
        self.end = ''
        self.id = 0

    def setname(self):
        self.nome = input('insira o nome:')

    def getname(self):
        return self.nome

    def setend(self):
        self.end = input('insira o endereço:')

    def getend(self):
        return self.end

    def setidade(self):
        self.id = int(input('insira a idade :'))

    def getidade(self):
        return self.id
