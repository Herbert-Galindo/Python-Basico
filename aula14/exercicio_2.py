# Exercicio 2

"""
Faça  um programa que pergunte o hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada.
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora = input('Digite um horário (0-23): ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Horário deve estar entre: (0-23)')
    else:
        if hora <=11:
            print('Bom Dia!')
        elif hora <=17:
            print('Boa Tarde!')
        else:
            print('Boa Noite!')
