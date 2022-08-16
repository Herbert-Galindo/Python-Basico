# For / Else em Python

variavel = ['Herbert','Mayara']
comeca_com_h = True
for valor in variavel:
    if valor.lower().startswith('H'):
        comeca_com_h = False

if comeca_com_h:
    print('Existe uma palavra que começa com H')
else:
    print('Não existe uma palavra que começa com H')
