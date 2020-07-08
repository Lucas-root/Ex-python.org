# esteprograma calcula a velocidade de dowload de um arquivo

while True:
	tamanho = input('\nDigite o tamanho deste arquivo em mb : ')
	if tamanho.isnumeric():
		tamanho = float(tamanho)
		break
	else:
		print('Digite o valor somente em números!')

while True:
	velocidade = input('\nDigite a velocidade de dowload em mb : ')
	if velocidade.isnumeric():
		velocidade = float(velocidade)
		break
	else:
		print('Digite somente números!')

tempo = tamanho / velocidade
print('Este arquivo demorara {} minutos para ser baixado'.format(tempo))

print('\nFim do código\n')



