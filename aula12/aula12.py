# Operadores logicos

# and, or, not
# in e not in

usuario = input('Digite o nome do usuário: ')
senha = input('Digite a senha: ')

usuario_1 = 'Mayara'
usuario_2 = 'Herbert'
senha_1 = 123456
senha_2 = 654321

if usuario_1 or usuario_2 == usuario and senha_1 or senha_2 == senha:
    print('Você conseguiu logar no sistema!')
else:
    print('Você não logou no sistema! Tente novamente!')


