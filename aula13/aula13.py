# tentativas e excessões

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:    # Usado para tentativa
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:     # Usado para excessão
    print('ERRO!')

# Passar código ou deixar livre espaço para o futuro usa: pass

# exemplo
"""
valor = True

if valor:
    pass
else:
    print('Tchau')
"""