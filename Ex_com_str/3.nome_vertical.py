# ler um nome e imprimilo na vertical

nome = input('Digite um nome para vê-lo na vertical : ')
nome = nome.upper()

n = -1 # dfine como -1 para o primeiro caracter a ser impresso ser nome[0]
carac_nome = len(nome)-1 # quantidade de caracteres que este nome possui 

print()

while n <= carac_nome:
    n += 1 # número do caracter que será impresso 
    print(nome[n]) 
    if n == carac_nome: # True se n for igual ao ultimo caracter, então ele quebra
        break

print('\nFim do código\n') 



