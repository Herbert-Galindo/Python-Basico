#Entrada de dados e input

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')

ano_nascimento = 2022 - int(idade)      # Converter str para int

print()
print(f'{nome} tem a idade de {idade} anos e nasceu no ano de {ano_nascimento}.')
print()

# Outro exemplo

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))
print(f'O resultado é: {numero_1 + numero_2}')
