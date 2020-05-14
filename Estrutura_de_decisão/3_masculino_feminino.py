# prigrama para ler uma letra f ou m e imprimir se é masculino ou feminino

letra = input('\nDigite uma letra : ')
letra = letra.lower()

if letra == 'f':
    print('A letra F corresponde ao sexo Feminino.')
elif letra == 'm':
    print('A letra M corresponde ao sexo Masculino.')
else:
    print('Por favor digite uma letra válida.')

print('\nFim do código\n')

