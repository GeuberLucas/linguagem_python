from Palavra import Palavra

p=Palavra()
p.palavra1=input('insira uma palavra: ')
p.palavra2=input('insira uma letra: ')
repet=0
for x in p.palavra1:
    if (x==p.palavra2):
        repet +=1

print( '{} ocorre {} vezes em {} ' .format(p.palavra2,repet,p.palavra2))