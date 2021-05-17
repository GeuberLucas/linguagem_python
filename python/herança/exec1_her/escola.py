from Aluno import Aluno

alunos = []
aluno = {'nome': '', 'endereço': '', 'idade': '', 'matricula': '', 'curso': '','disciplinas': ''}
a = Aluno()
d=[]
opcao = input('você deseja inserir um aluno ou um professor? ')
if opcao == 'aluno':
    re = 's'
    while re == 's':
        a.setname()
        aluno['nome'] = a.getname()
        a.setend()
        aluno['endereço'] = a.getend()
        a.setidade()
        aluno['idade'] = a.getidade()
        a.setmat()
        aluno['matricula'] = a.getmat()
        a.setcurso()
        aluno['curso'] = a.getcurso()
        alunos.append(aluno)
        print(aluno['disciplinas'])
        opcao2 = input('você deseja alterar as disciplinas? [s] ou [n]')
        if opcao2 == 's':
            op4 = 's'
            while op4 == 's':
                opcao3=input('vc deseja incluir ou remover alguma materia? ')
                if opcao3 == 'incluir':
                    d.append(input('qual disciplina você quer inserir? '))
                else:
                    d.remove(input('qual disciplina você quer remover? '))
                op4=input('deseja incluir ou remover outra materia? [s] ou [n]')
        aluno['disciplinas']= d
        alunos.append(aluno)
        re = input('deseja incluir outro aluno? [s] ou [n]')

print(alunos)