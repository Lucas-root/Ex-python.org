#By lucasedux0@gmail.com
#in 01/07/2020

# Aqui eu gravo va variavel tinta a tinta necessária
# marco o total de latas de 3,6 e 18 litros arredondando o resto da divisão para cima
area = float(input('\nDigite a area do local a ser pintado : '))
tinta = area / 6
latasP = int((tinta / 3.6)+1)
latasG = int((tinta / 18)+1)

#True caso os litros de tinta necessários sejem menor do que 18 litros
if tinta < 18:
    print('\nO total de tinta necessário para pintar está area será de {:.1f} litros de tinta'.format(tinta))
    print('Se você comprar latas de 3.6 litros irá precisar de {} latas o total será de R${:.2f}'.format(latasP, (latasP*25)))
    print('Se comprar latas de 18 litros você presisará de 1 lata o total será de R$80,00')
    print('E sobrarão {:.1f} litros de tinta.'.format(18 - tinta))

else:
    # resto quebrado da divisão de tinta/18, arredondado para cima 
    # para então descobrir as latas de 3.6 litros necessárias 
    restoArredondado = int(((tinta/18)-(int(tinta/18)))+1)
    latasGr = int(tinta/18)

    if (tinta%18) == 0:
        restoArredondado -= 1

    print('\nSerão necessários {:.1f} litros de tinta'.format(tinta))

    print('\nSe forem comprados apenas latas de 18 litros serão necessárias {} latas de tinta'.format(latasG))
    print('Com um total de R${:.2f}\n'.format(latasG*80))

    print('Se forem compradas somente latas de 3,6 litros serão necessárias {} latas de tinta'.format(latasP))
    print('Com um total de R${:.2f}\n'.format(latasP*25))

    print('Mas se forem compradas latas mistas')
    print('Serão necessárias {} latas de tinta de 18 litros'.format(latasGr))
    print('Serão necessárias {} latas de tinta de 3,6 litros'.format(restoArredondado))
    # O total será o preço das latas grandes + o preço das latas pequenas
    total = (latasGr*80)+(restoArredondado*25)
    print('E o total será de R${:.2f}\n'.format(total))

print('\nFim do código\n')

