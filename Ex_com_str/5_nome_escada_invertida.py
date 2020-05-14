# Programa para ler um nome e imprimir ele em uma escada invertida

nome = input('Digite o seu nome : ')
nome = nome.upper()

quantidade_caracter = len(nome) # não precisou de -1 porque o 0:() sempre fatia uma casa atras

print()

while quantidade_caracter >= 0:
    print(nome[0:quantidade_caracter])
    quantidade_caracter -= 1

print('\nFim do código\n')

