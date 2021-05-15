class Pessoa() :
    nome=None
    idade=None
    endereco=None

    def setnome(self,nome):
        self.nome=input('insira o nome: ')

    def getnome(self,nome):
        return self.nome

    def setend(self,endereco):
        self.endereco=input('insira o endereço: ')

    def getend(self,endereco):
        return self.endereco

    def setid(self,idade):
        self.idade=int(input('insira sua idade: '))
    
    def getid(self,idade):
        return self.idade 