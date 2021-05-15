from Alunos import Alunos
aprovados=[]
reprovados=[]
media_turma=[]
r='s'
while r=="s":
    aluno=Alunos(8,8,10,4)
    aluno.dados()
    aluno.verifica()
    aluno.media()
    if(aluno.media() == True ):
        aprovados.append(aluno.nome)
    else:
        reprovados.append(aluno.nome)
    media_turma.append(aluno.nota)
    r=input('deseja inserir outro aluno? [s] [n] ')
soma=sum(media_turma)
itens=len(media_turma)
media=soma/itens

print(aprovados )
print(reprovados)
print("a media da turma foi :{} pontos de um total de {} pontos".format(media,aluno.nota_max))
