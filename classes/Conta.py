class Conta:
    numero: None
    saldo:None
    nome:None
    cpf:None
    cheque:None 
    agencia:None
    def __init__(self,numero,saldo, agencia, cpf, nome:
        self.numero=numero
        self.saldo=0.0
        self.cheque=1000.00
    def consultar_saldo(self):
         print("saldo:"+str(self.saldo))
         print("saldo do cheque:"+str(self.cheque))
    def creditar(self,valor):
        self.saldo += valor 
    def debitar(self,valor):
        if(self.saldo+self.cheque<0):
            print("vc nao possui saldo suficiente")
        else: 
            self.saldo -= valor
    def transferir(self,conta,valor):
        if(self.saldo+self.cheque<0):
            print("vc nao possui saldo suficiente")
        else: 
            self.saldo -=valor
            conta.saldo +=valor 

    

