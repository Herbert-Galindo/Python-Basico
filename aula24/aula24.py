# Enumerate - enumerar elementos de uma lista - list

#       0           1           2

lista = [
    ['Eduardo', 'João', 'Maria'],       # 0
    ['Mariana', 'Mayara', 'Herbert'],   # 1
    ['Helena', 'Joana', 'Mikaelly'],    # 2
]

# enumerada = list(enumerate(lista))
# print(enumerada[1][1][1])

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome2, nome3)