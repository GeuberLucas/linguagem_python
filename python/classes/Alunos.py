class Alunos():
    nome=None
    prova1=None
    prova2=None
    trabalho=None
    matricula=None
    nota_max_prova1=None
    nota_max_prova2=None
    peso_trabalho=None
    situacao=None
    nota_max_trab=None
    nota=None
    nota_max=None 
    def __init__(self,nota_max_prova1,nota_max_prova2,nota_max_trab,peso_trabalho,):
        self.nota_max_prova1=nota_max_prova1
        self.nota_max_prova2=nota_max_prova2
        self.peso_trabalho=float(peso_trabalho)
        self.nota_max_trab= nota_max_trab
        self.nota_max=self.nota_max_prova1+self.nota_max_prova2+self.nota_max_trab
    
    def dados(self):
        self.nome=input("insira o nome do aluno: ")
        self.matricula=int(input('insira a matricula do aluno: '))
        self.prova1=float(input('insira a nota da primeira prova deste aluno: '))
        self.prova2=float(input('insira a nota da segunda prova deste aluno: '))
        self.trabalho=float(input('insira a nota do trabalho deste aluno:'))

    def verifica(self):
        
        if (self.prova1>self.nota_max_prova1):
            print('vc inseriu a nota da primeira prova incorretamente')
            self.prova1=float(input('insira a nota da primeira prova deste aluno: '))
        if(self.prova2>self.nota_max_prova2):
            print('vc inseriu a nota da segunda prova incorretamente')
            self.prova2=float(input('insira a nota da segunda prova deste aluno: '))
        


    def media(self):
        nottrab=self.trabalho*self.peso_trabalho
        porcent_aluno=self.prova1+self.prova2+nottrab
        porcent=(self.nota_max_prova1+self.nota_max_prova2+(self.nota_max_trab*self.peso_trabalho))*60/100
        self.nota=self.prova1+self.prova2+self.trabalho
        if  ( porcent_aluno >= porcent ):
          return True

           
        


   