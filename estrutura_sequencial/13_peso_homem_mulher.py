
sexo = input('\nDigite o seu sexo : (m ou f)')
if sexo == 'm':
	altura = float(input('Digita a sua altura : '))
	peso = (72.7*altura)-58
elif sexo == 'f':
	altura = float(input('Digite a sua altura : '))
	peso = (62.1*altura)-44.7
print('O seu peso ideal é de {:.1f} kilos'.format(peso))

print('\nFim do codigo\n')

