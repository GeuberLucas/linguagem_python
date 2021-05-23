from Sorteio import Sorteio
from random import randint  

n=Sorteio()
n.numero=randint(0,100)
n.palpites =0
print(n.numero)

rep="s"
while rep == "s" :
    n.palpites +=1
    p=int(input('insira seu palpite: '))
    if p==n.numero :
        print("vc acertou!!! com {} palpites".format(n.palpites))
    else:
        if p < n.numero :
            print('o numero que vc digitou é menor que o sorteado')
        else:
            print('o numero que vc digitou é maior que o sorteado')
        r=input('deseja tentar novamente? [s]/[n]')




