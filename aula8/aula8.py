#Desafio

"""
* Criar variavel com o ano atual
* Obter o ano de nascimento da pessoa
* Obter o IMC da pessoa
* Exibir um texto com todos os valores formatados usando o F-String
"""

nome = 'Herbert'
altura = 1.73
peso = 90
idade = 28
ano_atual = 2022
ano_nacimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem a idade de: {idade} anos e nasceu em {ano_nacimento - 1}.')
print(f'Peso de {peso}kg e altura de {altura} metros. Portanto seu IMC é de: {imc:.2f}.')

