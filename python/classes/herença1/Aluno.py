from Pesoa import Pessoa


class Aluno(Pessoa):
    matricula=None 
    curso=None
    disc=[]
    disciplina=None
 
    def setmat(self,matricula):
        self.matricula=int('insira a matricula do aluno:')

    def getmat(self,matricula):
        return self.matricula 
    
    def disci(self,disciplina):
         self.disciplina=input('insira a disciplina: ')

    def adddisci(self,disc,disciplina):
        self.disci.append(self.disciplina)

    def removedisci(self,disc,disciplina):
         self.disci.remove(self.disciplina)

    