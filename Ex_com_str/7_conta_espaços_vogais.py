# Programa simples para contar os espaços e as vogais de uma frase

frase = str(input('\nDigite uma frase : '))

frase = frase.lower()
frase = frase.strip()

a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

print('\nEsta frase possui {} espaços e {} vogais.'.format(frase.count(' '), a+e+i+o+u))

print('\nFim do código\n')

