# Operador Ternário em Python

logged_user = False
if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)
print()
print('Outro forma: exemplo')
print()

logged_user1 = True
msg1 = 'Usuário logado.' if logged_user1 else 'Usuário precisa logar.'
print(msg1)

print()
print('Outro forma: exemplo com input')
print()

idade = input('Qual é a sua idade? ')
if not idade.isnumeric():
    print('Você precisa digitar apenas números!')
else:
    idade = int (idade)
    maior_idade = (idade >= 18)
    msg = 'Pode acessar.' if maior_idade else 'Não pode acessar.'
    print(msg)