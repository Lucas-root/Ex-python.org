
str_um = input('Digite a primeira string : ')
str_dois = input('Digite a segunda string : ')

len_um = len(str_um)
len_dois = len(str_dois)
comparacao_tamanho = len_um == len_dois 
comparacao_conteudo = str_um == str_dois

print()

print('String 1 : {} '.format(str_um))
print('String 2 : {} '.format(str_dois))
print("Tamanho de '{}' {} caracteres".format(str_um, len_um))
print("Tamanho de '{}' {} carateres".format(str_dois, len_dois))

if comparacao_tamanho == True:
    print('Print as duas strings possuem o mesmo tamanho')
else:
    print('As duas strings não possuem o mesmo tamanho')

if comparacao_conteudo == True:
    print('E as duas strings possuem o mesmo conteúdo')
else:
    print('E as duas strings não possuem o mesmo conteúdo.')

print('\nFim do código\n')

