# Programa para ler um nome e imprimí-lo em escada na vertical

nome = input('Digite o seu nome : ')
nome = nome.upper() # Para a impressão ficar mais bonita joguei todo um input para maiúsculo

quantidade_caracter = len(nome)-1

n = -1

while n <= quantidade_caracter:
    n += 1 # indica até qual posição será exibido 
    print(nome[0:n]) # exibe do primeiro caracter até n 

print('\nFim do código\n')


