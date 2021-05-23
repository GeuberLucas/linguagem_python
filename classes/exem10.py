from Automovel import Automovel

a= Automovel()
a.modelo=input('qual o modelo do Automovel: ')
a.ano_de_Fabricacao=int(input('qual o ano de Fabricacao do Automovel: '))
a.chassi=input('qual o chassi do Automovel: ')
a.cor=input('qual o cor do Automovel: ')
a.placa=input('qual o placa do Automovel: ')
a.numeroportas=int(input('qual o numero de portas do Automovel: '))
a.marca=input('qual o marca do Automovel: ')

print('modelo:'+a.modelo )
print('ano de Fabricacao:'+str(a.ano_de_Fabricacao) )
print('chassi:'+a.chassi )
print('cor:'+a.cor )
print('numero portas:'+str(a.numeroportas) )
print('marca:'+a.marca )
print('placa:'+a.placa )
