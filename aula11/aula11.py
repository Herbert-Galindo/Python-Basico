# Operadores Relacionais

# == > < >= <= !=

"""     # EXEMPLOS
print(2==2)
print(2>=2)
print(2>2)
print(10<=20)
print(1!=3)

var_1 = 'Mayara'
var_2 = 'Herbert'
expressao = (var_1 != var_2)
print(expressao)
"""

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
idade = int(idade)
maior_idade = 18

if idade >= maior_idade:
    print(f'{nome} Pode tirar o emprestimo')
else:
    print(f'{nome} Não pode tirar o emprestimo')

