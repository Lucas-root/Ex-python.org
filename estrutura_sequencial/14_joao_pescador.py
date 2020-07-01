
peso = float(input('\nDigite o peso dos peixes : '))
exedente = (peso-50)
multa = exedente*4

if peso > 50:
    print(f'\npeso total do peixe foi {peso} kilos')
    print(f'Você passou {exedente} kilos do limite')
    print(f'E tera que pagar R${multa:.2f} de multa.\n')
else:
    print(f'\nO peso total do peixe foi de {peso} kilos')
    print('E não presisará pagar multa nenhuma.\n')

print('Fim do código.\n')



