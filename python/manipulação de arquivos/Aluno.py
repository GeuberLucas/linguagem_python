
class Aluno():
    nome=None
    matricula=None
    nota_av1=None
    nota_av2=None
    media=None
    def dados(self,nome,matricula,nota_av1,nota_av2):
        self.nome=input('insira o nome do aluno: ')
        self.matricula=int(input('insira o numero da matricula: '))
        self.nota_av1=float(input('insira a nota da primeira avaliação: '))
        self.nota_av2=float(input('insira a nota da segunda avaliação: '))
          
    def med(self,media,nota_av1,nota_av2):
        self.media=(self.nota_av1+self.nota_av2)/2
        