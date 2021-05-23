from Primos import Primos 

def primo(numero):
        if (numero < 2):
            return False
        else:
            for n in range(2, numero):
                if (numero % n == 0):
                    return False
            return True

numero=int(input("insira um numero:"))
p=Primos()
if (primo(numero)):
    p.numero=numero
else:
    print('{} n é um numero primo' .format(numero))




        







        


