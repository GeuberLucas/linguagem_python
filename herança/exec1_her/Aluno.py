from Pessoa import Pessoa


class Aluno (Pessoa):
    matricula: int = None
    curso = None

    def setmat(self):
        self.matricula = int(input('insira a matricula: '))

    def getmat(self):
        return self.matricula

    def setcurso(self):
        self.curso=input('insira o curso do aluno: ')

    def getcurso(self):
        return self.curso

    def adddisciplina(self, d):
        d.append(input('qual disciplina você deseja incluir? '))

    def removedisciplina(self,d):
        d.remove(input('qual disciplina você deseja remover?'))
