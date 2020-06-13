# programa para ler uma temperatura em F e converter para C

f = float(input('\nDigite a temperatura em graus farenheit : '))
conversao = (5*(f-32)/9)

print('\n{} G farenheit converitidos para celsius é {:.1f}'.format(f, conversao))

print('\nFim do codigo\n')
