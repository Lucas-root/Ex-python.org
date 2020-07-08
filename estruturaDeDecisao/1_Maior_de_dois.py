# programa para ler dois números e imprimir o maior dos dois 

numero_um = float(input('Digite o primeiro número : '))
numero_dois = float(input('Digite o segundo número : '))

if numero_um > numero_dois:
	print('O maior número é o primeiro.')
elif numero_dois > numero_um:
	print('O maior número é o segundo.')
else: 
	print('Os dois números são iguais.')


