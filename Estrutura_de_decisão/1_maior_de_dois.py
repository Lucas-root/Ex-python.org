# faça um programa que peça dois números e imprima o maior deles

numero_um = float(input('Digite o primeiro número : '))
numero_dois = float(input('Digite o segundo número : '))

print() # para melhorar a visualização

if numero_um > numero_dois:
    print('O maior número é o Primeiro ( {} ) '.format(numero_um))
else:
    print('O maior número é o segundo ( {} ) '.format(numero_dois))

print('\nFim do código\n')

