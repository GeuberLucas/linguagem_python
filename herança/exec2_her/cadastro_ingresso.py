from Dados import Dados
from ingresso import *

a = Dados()
b = Superclasse()

'''colocando os valores basicos'''
v_ingresso = float(input('insira o valor base do ingresso: R$'))
b.setvalor(v_ingresso)
valor_ad_vip = float(input('insira o valor adicional para o VIP: R$'))
b.setvalorad(valor_ad_vip)
valor_ad_camarote = float(input('insira o valor adicional do camarote superior: R$'))

'''cadastrando o ingresso'''
nome=input('insira o nome completo : ')
evento=input('insira o evento : ')
sessao=input('insira a sessão: ')
tipo_ingresso=input('insira o tipo de ingresso : ')
a.dados(nome,evento,sessao,tipo_ingresso)


