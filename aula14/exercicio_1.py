# Exercicios 1

"""
Faça  um programa que peça ao usuário para digitar um número inteiro,
informe se esse número é par ou impar. Caso não digite um número inteiro, informe
que o número não é inteiro
"""

numero = (input('Digite um número inteiro: '))

if numero.isdigit():
    numero = int(numero)

    if numero % 2 ==0:
        print(f'{numero} É um número Par!')
    else:
        print(f'{numero} É um número Impar!')
else:
    print('Isso não é um número inteiro!')

