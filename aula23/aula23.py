"""
* Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate = enumerar elementos da lista # list
"""
string = 'Brasil é o melhor país para se viver, melhor ainda seria se sua Política fosse boa.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

        print(f'A palavra que apareceu mais vezes foi: {palavra} ({contagem}x)')
print()
print('#########')
print()

string_2 = 'O Brasil é pentacampeão'
lista_3 = string_2.split(' ')
string_2_1 = '.'.join(lista_3)

print(string_2)
print(string_2_1)
print(lista_3)