valor = float(input('\nDigite quanto este funcionário ganha por hora : '))
horas = float(input('Digite quantas horas este funcionário trabalhou no mês : '))

salarioBruto = valor * horas
impostoRenda = (salarioBruto * 11)/100
inss = (salarioBruto * 8)/100
sindicato = (salarioBruto * 5)/100
descontos = impostoRenda + inss + sindicato 

liquido = salarioBruto - descontos 

print('\n+ Salário Bruto : R${:.2f}'.format(salarioBruto))
print('- IR (11%) : R${:.2f}'.format(impostoRenda))
print('- INSS (8%) : R${:.2f}'.format(inss))
print('- sindicato (5%) : R${:.2f}'.format(sindicato))
print('= Total descontos : R${:.2f}'.format(descontos))
print('= Salário Liquido : R${:.2f}'.format(liquido))

print('\nFim do Código\n')



