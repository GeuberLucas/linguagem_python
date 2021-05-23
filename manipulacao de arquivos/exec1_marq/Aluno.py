from random import *


class Aluno:
    nome = None
    matricula = None
    nota_av1 = None
    nota_av2 = None
    media = None
    nota_max_av1 = None
    nota_max_av2 = None
    porcent_media_aprov = None
    aluno_media_aprov = None
    status_aluno = None

    def inicio(self, nota_max_av1, nota_max_av2, porcent_media_aprov):
        self.nota_max_av1 = nota_max_av1
        self.nota_max_av2 = nota_max_av2
        self.porcent_media_aprov = porcent_media_aprov

    def dados(self):
        self.nome = input('insira o nome do aluno: ')
        self.matricula = randint(100000000000, 999999999999)'''matricula com 12 digítos'''
        self.nota_av1 = float(input('insira a nota da primeira avaliação: '))
        self.nota_av2 = float(input('insira a nota da segunda avaliação: '))

    def addaluno(self, alu):
        aluno = 'o nome do aluno é: '+self.nome
        alu.append(aluno)
        mat = 'a matricula do aluno é: '+str(self.matricula)
        alu.append(mat)
        nota1 = 'a nota da primeira avaliação do aluno é: '+str(self.nota_av1)
        alu.append(nota1)
        nota2 = 'a nota da segunda avaliação: '+str(self.nota_av2)
        alu.append(nota2)



    def med(self):
        self.media = (self.nota_av1 + self.nota_av2) / 2
        self.aluno_media_aprov = (self.porcent_media_aprov / 100) * ((self.nota_max_av1 + self.nota_max_av2) * 2)
        if self.media >= self.aluno_media_aprov:
            self.status_aluno = 'O aluno foi aprovado'
        else:
            self.status_aluno = 'O aluno foi reprovado'
