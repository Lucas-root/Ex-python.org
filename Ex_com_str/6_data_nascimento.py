# Programa para ler uma data de nascimento e imprimila por extenso 

data = str(input('\nDigite a sua data de nascimento : \n'))
data = data.split('/')

meses = {1 : 'Janeiro',
        2 : 'Fevereiro',
        3 : 'Março',
        4 : 'Abril',
        5 : 'Maio',
        6 : 'Junho',
        7 : 'Julho',
        8 : 'Agosto',
        9 : 'Setembro',
        10 : 'Outubro',
        11 : 'Novembro',
        12 : 'Dezembro'}

print('Você nasceu no dia {} do mês de {} do ano de {}.'.format(data[0], meses[int(data[1])], data[2]))

print('\nFim do código\n')





