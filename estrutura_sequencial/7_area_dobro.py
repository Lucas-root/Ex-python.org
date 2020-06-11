# Programa para calcular a area de um quadrado e e seguida 
# imprimir o seu dobro

aresta1 = float(input('\nDigite a primeira aresta deste quadrado : '))
aresta2 = float(input('Digite a segunda aresta deste quadrado : '))

area = aresta1 * aresta2 
dobro = area * 2

print('\nA area deste quadrado é de {}'.format(area))
print('E o seu drobro {:.2f}'.format(dobro))

print('\nFim do Codigo\n')
