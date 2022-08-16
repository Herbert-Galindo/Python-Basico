nome = 'Herbert Galindo'
idade = 28
altura = 1.73
peso = 90
imc = peso / altura ** 2


print(nome, 'tem', idade, 'anos', 'e pesa', peso, 'kg', 'e altura de', altura, 'metros')
print('Portanto seu IMC é:', imc)

#Fomatado com: (  f  ) na frente.
#Fazer numeros flutuantes ter duas casas: (    :.2f     )
print(f'{nome} tem {idade} anos e pesa {peso} kg e altura de {altura} metros')
print(f'Portanto seu IMC é: {imc:.2f}')