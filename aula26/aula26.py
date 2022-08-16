# Funções  - def em Python - 1

def saudacao(msg='Olá', nome='Usuário'):
    nome = input('Qual o seu nome?')
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '9')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)