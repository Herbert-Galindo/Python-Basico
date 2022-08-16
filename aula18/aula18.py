# while e else
# contadores
# acumuladores

contador = 0
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    if contador >= 5:
        break           # condição que para o codigo no contador 5
    acumulador = acumulador + contador
    contador += 1
else:
    print('Fim')
print('O código parou porque o contador é maior que 5')



