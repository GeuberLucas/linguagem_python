class Elevador():
    peso_max:None
    pessoas_max:None 
    andares:None
    pessoas_dentro:None
    andar_atual:None
    resposta:None
   
    def __init__(self,peso_max,pessoas_max,andares):
        self.peso_max=peso_max
        self.pessoas_max=pessoas_max
        self.andares=andares-1
        self.andar_atual=0
        self.pessoas_dentro=0

    def entrar(self):
       
        if (self.pessoas_dentro < self.pessoas_max):
            entraram=int(input("quantas pessoas entraram: "))
            if(entraram<=self.pessoas_max):
                self.pessoas_dentro+=entraram
            else:
                print('o numero de pessoas que desejam entrar não é suportado')
        else:
                print("o elevador atingiu a sua capacidade maxima de pessoas")

    def sair(self):
        
        dentro=self.pessoas_dentro
        if(self.pessoas_dentro > 0):
            pessoas_sairam=int(input("quantas pessoas sairam: "))
            if(pessoas_sairam<=self.pessoas_dentro):
                self.pessoas_dentro=dentro-pessoas_sairam
            else:
                print('o numero digitado ultrapassa o numero de pessoas que estão dentro do elevador')
        else:
            print('o elevador está vazio')
    def subir(self):
        if(self.andar_atual<self.andares):
            self.andar_atual+=1
            print("subimos para o andar {}" .format(self.andar_atual))
        else:
            print('estamos no ultimo andar')
    def descer(self):
        if(self.andar_atual>0):
            self.andar_atual-=1
            print("descemos para o andar {}" .format(self.andar_atual))
        else:
            print('estamos no térreo')

        
    