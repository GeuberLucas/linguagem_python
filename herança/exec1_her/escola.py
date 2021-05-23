from Aluno import Aluno
from Professor import Professor

alunos = []
aluno = {'nome': '', 'endereço': '', 'idade': '', 'matricula': '', 'curso': '', 'disciplinas': ''}
a = Aluno()
p = Professor()
professores = []
professor = {'nome': '', 'endereço': '', 'idade': '', 'salario': '', 'curriculo': ''}
d = []
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
                opcao3 = input('o que você deseja fazer ,incluir ou remover outra materia ? ')
                if opcao3 == 'incluir':
                    a.adddisciplina(d)
                else:
                    a.removedisciplina(d)
                op4 = input('deseja incluir ou remover outra materia? [s] ou [n]')
        aluno['disciplinas'] = d
        alunos.append(aluno)
        re = input('deseja incluir outro aluno? [s] ou [n]')

else:
    re4 = 's'
    while re4 == 's':
        p.setname()
        professor['nome'] = p.getname()
        p.setend()
        professor['endereço'] = p.getend()
        p.setidade()
        professor['idade'] = p.getidade()
        p.setsalario()
        professor['salario'] = p.getsalario()
        p.setcurriculo()
        professor['curriculo'] = p.getsalario()
        p.printcurriculo()
        professores.append(professor)
        re4 = input('deseja incluir outro professor? [s] ou [n]')

print(professores)
print(alunos)
