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
