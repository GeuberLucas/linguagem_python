from Aluno import Aluno

re = 's'
a = Aluno()
while re == 's':
    disciplina = input('insira a disciplina que você deseja criar a lista de alunos: ')
    nota_max_av1 = float(input('insira a nota maxima da primeira avaliação: '))
    nota_max_av2 = float(input('insira a nota maxima da primeira avaliação: '))
    porcent_media_aprov = float(input('insira a porcentagem para a aprovação: '))
    a.inicio(nota_max_av1, nota_max_av2, porcent_media_aprov)
    arquivo = open(disciplina + ".txt", "w+")
    re2 = 's'
    alu = []
    mediaturma = []

    while re2 == 's':
        a.dados()
        a.addaluno(alu)
        a.med()
        mediaturma.append(a.media)
        alu.append(a.status_aluno)
        arquivo.write(str(alu)+'\n')
        re2 = input('deseja inserir outro aluno? [s] ou [n]')
        alu.clear()
    somamedia ='a media da turma foi ' +str(sum(mediaturma))
    '''apresenta a media da turma no console '''
    print(somamedia)
    '''insere o aluno na disciplina e a media da turma ao final '''

    arquivo.write('\n')
    arquivo.write(str(somamedia))
    arquivo.close()
    re = input('deseja inserir outra disciplina? [s] ou [n]')
