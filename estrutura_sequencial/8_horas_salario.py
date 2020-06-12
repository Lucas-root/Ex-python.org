# programa para ler quanto um funcionario ganha por hora e quantas horas ele trabalhou 
# no referIdo mês, em seguida calcular o seu salario

valor_hora = float(input('\nDigite quanto este funcionario ganha por hora : '))
horas_trabalhadas = int(input('Digite quantas horas este funcionario \ntrabalhou no mês referido : '))
salario = valor_hora * horas_trabalhadas

print('\nO salário deste funcionario será de R${:.2f}'.format(salario))

