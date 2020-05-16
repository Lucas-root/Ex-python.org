# Este programa lê uma frase e diz se ela é um palindromo ou não
# palindromos são palavras que lidas de tras para frente são a mesma palavra

frase_original = str(input('\nDigite a palavra ou frase a ser analisada : '))
frase_original = frase_original.split()
frase_original = ''.join(frase_original)
frase_original = frase_original.strip()
frase_original = frase_original.lower()

frase_alterada = frase_original[::-1]

if frase_alterada == frase_original:
    print('Esta frase é um palíndromo!')
else:
    print('Esta frase não é um palíndromo.')

print('\nFim do código\n')



