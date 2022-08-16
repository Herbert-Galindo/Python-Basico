"""
Formatando valores com modificadores

:s Texto (strings)
:d Inteiros (int)
:f Números de pontos flutuantes (float)
:. (NÚMERO) f - Quantidade de casas decimais (float) :.2f
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

"""

nome = 'Herbert Galindo'
numero = 8428171
print(nome.lower())
print(nome.upper())
print(nome.title())
print(f'{numero:#^50f}')
