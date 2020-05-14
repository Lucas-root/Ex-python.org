# programa para ler um número e imprimir se ele é positivo ou negativo 

numero = float(input('\nDigite um número para ver se ele é positivo ou negativo : '))

print()

if numero == 0:
    print('Este número é  igual a 0.')
elif numero < 0:
    print('Este número é negativo.')
else:
    print('Este número é positivo.')

print('\nFim do código\n')


