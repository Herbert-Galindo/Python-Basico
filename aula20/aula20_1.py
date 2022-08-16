# For in Python
# Interando strings com for
# Função range (start=0, stop, step=1) PADRÃO

texto = 'python'
nova_string =''

for letra in texto:
    if letra == 'p':
        nova_string = nova_string + letra.upper()
    elif letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'n':
        nova_string = nova_string + letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)