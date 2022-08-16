# Funções  - def em Python - *args **kwargs - 3

def func(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')
    print(nome)

    sobrenome = kwargs.get('sobrenome')
    print(sobrenome)

lista = [1,2,3,4,5]
lista2 = [12,13,14,15,16]
func(*lista, *lista2, nome = 'Luiz', sobrenome = 'Miranda')