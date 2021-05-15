from Elevador import Elevador

e=Elevador(500,5,2)
e.resposta=str('s')
while (e.resposta=='s'):
    op=input('qual operação deseja realizar ? [entrar] [sair] [subir] [descer]')
    if(op=='entrar'):
        e.entrar()
    if(op=='sair'):
       e.sair()
    if(op=='subir'):
       e.subir()
    if(op=="descer"):
       e.descer()
    e.resposta=input('deseja realizar outra operção? [s] [n]')     